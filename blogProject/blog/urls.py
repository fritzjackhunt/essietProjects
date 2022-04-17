from django.urls import path
from . import views
from .views import NewsletterView
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='homepage'),
    path('next', views.home1, name='homepage1'),
    path('about', NewsletterView.as_view(), name='about'),
    path('success', views.success, name='success'),
    path('contact', views.contact, name='contact'),
    path('blog1', views.blog1, name='blog1'),
    path('blog2', views.blog2, name='blog2'),
    path('blog3', views.blog3, name='blog3'),
    path('blog4', views.blog4, name='blog4'),
    path('blog5', views.blog5, name='blog5'),
    path('blog6', views.blog6, name='blog6'),
    path('blog7', views.blog7, name='blog7'),
    path('blog8', views.blog8, name='blog8'),
    path('blog9', views.blog9, name='blog9'),
    path('sony', views.sony, name='sony'),
    path('huawei', views.huawei, name='huawei'),
    path('amazon', views.amazon, name='amazon'),
    path('internetvpn', views.internetvpn, name='internetvpn'),
    path('blackfridaydeal', views.blackfridaydeal, name='blackfridaydeal'),
    path('expressvpn', views.expressvpn, name='expressvpn'),
    path('security', views.security, name='security'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'), #sitemap
]