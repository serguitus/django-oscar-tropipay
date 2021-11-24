"""
Views to suport TropiPay callbacks
"""

import logging
from tropipay.exceptions import InvalidSignatureException

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from tropipay.facade import Facade


LOGGER = logging.getLogger(__name__)


class PaymentSuccessView(ThankYouView):
    """
    TropiPay redirect success payment view
    """

    template_name='tropipay/payment_success.html'

    def get(self, request, *args, **kwargs):
        """
        TropiPay success payment http GET processing
        """
        LOGGER.debug('PaymentSuccessView.get request: %s', request)

        payment_data = request.GET.get('data')
        Facade().process_payment_success(
            payment_data=payment_data
        )
        return 


class PaymentFailedView(ThankYouView):
    """
    TropiPay redirect failed payment view
    """

    template_name='tropipay/payment_failed.html'

    def get_context_data(self, **kwargs):

        LOGGER.debug('PaymentFailedView.get request: %s', self.request)

        payment_data = self.request.GET.get('data')
        Facade().process_payment_failed(
            payment_data=payment_data
        )
        return order


class PaymentNotificationView(View):
    """
    TropiPay notification view
    """

    def post(self, request, *args, **kwargs):
        """
        TropiPay notification http POST processing
        """
        LOGGER.debug('PaymentNotificationView.post request: %s', request)

        signature = request.GET.get('signature')
        notification_status = request.POST.get('status')
        notification_data = request.POST.get('data')
        try:
            Facade().handle_notification(
                received_signature=signature,
                notification_status=notification_status,
                notification_data=notification_data
            )
            return HttpResponse()
        except InvalidSignatureException:
            return HttpResponseBadRequest()
        except Exception:
            return HttpResponseBadRequest()
s