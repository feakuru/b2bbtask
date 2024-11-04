from rest_framework import permissions, viewsets

from wallet.models import Transaction, Wallet
from wallet.serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    # NOTE: for this test task, I did not implement or check auth.
    # However, in a real application it would quite likely be required,
    # and would be handled by:

    # permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # NOTE: it does not seem logical for users to be able to update transactions,
    # so I restricted the available HTTP methods here
    http_method_names = ["get", "post", "head"]
