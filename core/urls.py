from django.urls import path
from .views import DetailView, homeview, CheckoutView, add_to_cart, remove_single_item_from_cart, OrderSummaryView, remove_from_cart, PaymentView, AddCouponView, RequestRefundView

app_name = 'core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/<slug>', DetailView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment')
]
