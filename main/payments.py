from payme.views import MerchantAPIView
from payme.models import MerchantTransactionsModel

from main.models import Order


class PaymeCallBackAPIView(MerchantAPIView):
    def create_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"create_transaction for order_id: {order_id}, response: {action}")
        transaction = MerchantTransactionsModel.objects.filter(id=action['result']['transaction'])
        if transaction.exists():
            order = Order.objects.filter(id=order_id).first()
            order.status = Order.Status.PENDING
            order.save(update_fields=['status'])

    def perform_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"perform_transaction for order_id: {order_id}, response: {action}")
        transaction = MerchantTransactionsModel.objects.filter(id=action['result']['transaction'])
        if transaction.exists():
            order = Order.objects.filter(id=order_id).first()
            order.status = Order.Status.PAID
            order.save(update_fields=['status'])

    def cancel_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"cancel_transaction for order_id: {order_id}, response: {action}")
        transaction = MerchantTransactionsModel.objects.filter(id=action['result']['transaction'])
        if transaction.exists():
            order = Order.objects.filter(id=order_id).first()
            order.status = Order.Status.CANCELED
            order.save(update_fields=['status'])
