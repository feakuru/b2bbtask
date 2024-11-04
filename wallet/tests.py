import json

from django.test import TestCase
from rest_framework.test import APIClient

from wallet.models import Transaction, Wallet


class WalletTestCase(TestCase):
    def setUp(self):
        self.wallets = [
            Wallet.objects.create(label="my_cool_wallet"),
            Wallet.objects.create(label="wallet_2"),
        ]
        self.client = APIClient()

    def test_get_wallets(self):
        response = self.client.get("/wallets/")
        self.assertEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {"id": 1, "label": "my_cool_wallet", "balance": 0},
                    {"id": 2, "label": "wallet_2", "balance": 0},
                ],
            },
        )

    def test_create_wallet(self):
        create_wallet_response = self.client.post(
            "/wallets/", data={"label": "new_wallet"}
        )
        self.assertEqual(
            create_wallet_response.status_code,
            201,
        )
        get_wallets_response = self.client.get("/wallets/")
        self.assertEqual(
            json.loads(get_wallets_response.content.decode("utf-8")),
            {
                "count": 3,
                "next": None,
                "previous": None,
                "results": [
                    {"id": 1, "label": "my_cool_wallet", "balance": 0},
                    {"id": 2, "label": "wallet_2", "balance": 0},
                    {"id": 3, "label": "new_wallet", "balance": 0},
                ],
            },
        )


class TransactionTestCase(TestCase):
    def setUp(self):
        self.wallets = [
            Wallet.objects.create(label="my_cool_wallet"),
            Wallet.objects.create(label="wallet_2"),
        ]
        self.transactions = [
            Transaction.objects.create(
                wallet=self.wallets[0], txid="0x123456789", amount=20
            ),
            Transaction.objects.create(
                wallet=self.wallets[0], txid="0x123456790", amount=30
            ),
            Transaction.objects.create(
                wallet=self.wallets[1], txid="0x123456788", amount=20
            ),
        ]
        self.client = APIClient()

    def test_get_transactions(self):
        response = self.client.get("/transactions/")
        self.assertEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "count": 3,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "amount": 20,
                        "id": 1,
                        "txid": "0x123456789",
                        "wallet": "http://testserver/wallets/1/",
                    },
                    {
                        "amount": 30,
                        "id": 2,
                        "txid": "0x123456790",
                        "wallet": "http://testserver/wallets/1/",
                    },
                    {
                        "amount": 20,
                        "id": 3,
                        "txid": "0x123456788",
                        "wallet": "http://testserver/wallets/2/",
                    },
                ],
            },
        )

    def test_create_transactions_forces_txid_uniqueness(self):
        response = self.client.post(
            "/transactions/",
            data={
                "txid": "0x123456789",
                "wallet": "http://testserver/wallets/2/",
                "amount": 1,
            },
        )
        assert response.status_code == 400
        assert json.loads(response.content.decode()) == {
            "txid": ["transaction with this txid already exists."]
        }

    def test_create_transactions_does_not_allow_negative_balance(self):
        response = self.client.post(
            "/transactions/",
            data={
                "txid": "0x123456783",
                "wallet": "http://testserver/wallets/2/",
                "amount": -300,
            },
        )
        assert response.status_code == 400
        assert json.loads(response.content.decode()) == {
            "amount": "Transaction must not result in negative balance"
        }
