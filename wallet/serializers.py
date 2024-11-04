from rest_framework import serializers

from wallet.models import Transaction, Wallet


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "label", "balance"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "txid", "wallet", "amount"]

    def create(self, validated_data):
        wallet = validated_data["wallet"]
        if wallet.balance + validated_data["amount"] < 0:
            raise serializers.ValidationError(
                {"amount": "Transaction must not result in negative balance"}
            )
        # NOTE: The operation below is the reason for enabling ATOMIC_REQUESTS,
        # otherwise this might result in race conditions.
        # In a real application, we would most likely apply the decorator
        # @transaction.atomic on a per-request basis
        wallet.balance += validated_data["amount"]
        wallet.save()
        return Transaction.objects.create(**validated_data)
