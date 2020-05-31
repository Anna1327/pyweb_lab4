from django.urls import path
from .views import *




urlpatterns = [
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view(), name='shop'),
    path('shop/veget', ShopView.as_view(), name='vegetables'),
    path('product-single/', ProductSingleView.as_view(), name='product_single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
	path('blog/<int:page_id>', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
	path('wishlist/', WishlistView.as_view(), name='wishlist'),
	path('wishlist/pic/', lambda request: redirect("https://picsum.photos/100"), name='wishlist-pic')
]
