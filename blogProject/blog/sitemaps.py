from typing import Protocol
from django.contrib import sitemaps
from django.urls import reverse
from django.conf import settings
from zloggr.settings import SITE_ID

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    protocol = 'https'
    SITE_ID = 1

    def items(self):
        return ['homepage', 'homepage1', 'about', 'success', 'contact', 'blog1', 'blog2', 'blog3', 'blog4', 'blog5', 'blog6', 'blog7', 'blog8', 'blog9', 'sony', 'huawei', 'amazon', 'internetvpn', 'blackfridaydeal']

    def location(self, item):
        return reverse(item)