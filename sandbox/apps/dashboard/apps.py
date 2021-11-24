"""
checkout views and urls
"""

from django.conf.urls import url

from oscar.apps.checkout.apps import CheckoutConfig as OscarCheckoutConfig
from oscar.core.loading import get_class


TropiPayCallbackRedirectView = get_class('tropipay.views', 'TropiPayCallbackRedirectView')
TropiPayNotificationView = get_class('tropipay.views', 'TropiPayNotificationView')

class CheckoutConfig(OscarCheckoutConfig):


    def get_urls(self):
        urls = super().get_urls()
        urls += [
            url(
                r'^return/$',
                TropiPayCallbackRedirectView.as_view(),
                name='tropipay_callback_redirect_url'),
            url(
                r'^update_order/$',
                TropiPayNotificationView.as_view(),
                name='status_changed'),
        ]
        return self.post_process_urls(urls)
