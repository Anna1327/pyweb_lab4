from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from .models import Vegetables


# Create your views here.


class IndexView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                   'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                   'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class ShopView(View):

    def get(self, request, page_id=1):

        products = Vegetables.objects.all()
        paginator = Paginator(products, 4)
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))

        except:
            return redirect(reverse('shop'))
        return render(request, 'shop/shop.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                  'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                  'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT,
                                                  'products': products})

    def vegetables(self, request):
        products = Vegetables.objects.all.filter(type=Vegetables)
        paginator = Paginator(products, 4)
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))

        except:
            return redirect(reverse('vegetables'))
        return render(request, 'shop/shop.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                  'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                  'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT,
                                                  'products': products})


class ContactView(View):

    def get(self, request):
        return render(request, 'shop/contact.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                     'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                     'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT,
                                                     'website': WEBSITE})


wishlist_count = 0


class WishlistView(View):

    def get(self, request):
        return render(request, 'shop/wishlist.html',
                      {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                       'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                       'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})

    def post(self, request):
        global wishlist_count
        if request.is_ajax():
            message = f'WishlistView: {wishlist_count}'
            wishlist_count += 1
            print(message)
        else:
            message = 'Not AJAX request'

        return HttpResponse(message)


class ProductSingleView(View):

    def get(self, request):
        return render(request, 'shop/product-single.html',
                      {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                       'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                       'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class CheckoutView(View):

    def get(self, request):
        return render(request, 'shop/checkout.html',
                      {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                       'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                       'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class CartView(View):

    def get(self, request):
        return render(request, 'shop/cart.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                  'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                  'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class BlogSingleView(View):

    def get(self, request):
        return render(request, 'shop/blog-single.html',
                      {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                       'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                       'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class BlogView(View):

    def get(self, request, page_id=1):
        blog = [{'title': 'Salads and snacks',
                 'image': 'shop/images/image_1.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'Article on the benefits of good nutrition'},
                {'title': 'What is the use of beans?',
                 'image': 'shop/images/image_2.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'The article talks about the benefits of beans'},
                {'title': 'Culinary duel',
                 'image': 'shop/images/image_3.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'Article about culinary duel'},
                {'title': 'Table setting',
                 'image': 'shop/images/image_4.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'How beautiful serving affects your mood'},
                {'title': 'Separate food',
                 'image': 'shop/images/image_5.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'Article about product Compatibility '},
                {'title': 'Choosing the Right salad sauce',
                 'image': 'shop/images/image_6.jpg',
                 'data': '20.06.19',
                 'author': 'Administrator',
                 'description': 'What can be combined and what not? Taste and benefit'}]

        paginator = Paginator(blog, 1)
        try:
            blog = paginator.page(page_id)
            blog.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('blog'))
        return render(request, 'shop/blog.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                  'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                  'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})


class AboutView(View):

    def get(self, request):
        return render(request, 'shop/about.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'delivery': DELIVERY,
                                                   'shop_name': SHOP_NAME, 'questions': QUESTIONS, 'address': ADDRESS,
                                                   'phone': PHONE, 'mail_q': MAIL_FOR_QUESTIONS, 'about_us': ABOUT})
