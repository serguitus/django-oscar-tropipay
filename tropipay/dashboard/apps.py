from django.conf.urls import url

from oscar.core.application import OscarDashboardConfig

from . import views


class TropiPayDashboardConfig(OscarDashboardConfig):
    label = 'tropipay_dashboard'
    name = 'apps.dashboard.tropipay'
    verbose_name = _('TropiPay')

    default_permissions = ['is_staff', ]

    def ready(self):
        self.list_view = views.DocdataOrderListView
        self.detail_view = views.DocdataOrderDetailView
        self.update_status_view = views.DocdataOrderUpdateStatusView
        self.cancel_view = views.DocdataOrderCancelView

    def get_urls(self):
        """
        Get URL patterns defined for flatpage management application.
        """
        urls = [
            url(r'^$', self.list_view.as_view(), name='docdata-order-list'),
            url(r'^detail/(?P<pk>[-\w]+)/$', self.detail_view.as_view(), name='docdata-order-detail'),
            url(r'^update-status/(?P<pk>[-\w]+)/$', self.update_status_view.as_view(), name='docdata-order-update-status'),
            url(r'^cancel/(?P<pk>[-\w]+)/$', self.cancel_view.as_view(), name='docdata-order-cancel'),
        ]
        return self.post_process_urls(urls)
