"""
Django Oscar settings.
"""

import os

from pathlib import Path

from django.utils.translation import ugettext_lazy as _

from oscar.defaults import *  # noqa

from .custom_settings import *


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r9np-c6ze(i4ay)nuut0)pzur1o-#^+oxj1nrp*%)yg5112^!&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'shop.thenaturexperts.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'tropipay',

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',

    'apps.checkout.apps.CheckoutConfig',

    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
]

SITE_ID = 1

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # oscar middleware
    'oscar.apps.basket.middleware.BasketMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'sandbox.urls'

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # oscars context processors
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.core.context_processors.metadata',
            ),
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


#####################################################
########### OSCAR CONFIGURATION VARIABLES ###########
#####################################################


OSCAR_DEFAULT_CURRENCY = "USD"

# Order pipeline
OSCAR_INITIAL_ORDER_STATUS = 'new'  # The main object
OSCAR_INITIAL_LINE_STATUS = 'new'   # The individual lines
OSCAR_ORDER_STATUS_PIPELINE = {
    # Possible states of an order, and the transitions.
    'new': ('pending', 'paid', 'cancelled'),  # docdata started
    'pending': ('paid', 'cancelled'),
    'paid': ('shipping', 'delivered', 'charged back', 'refunded'),
    'refunded': (),       # Merchant refunded
    'charged back': (),   # Customer asked for charge back
    'cancelled': (),
    'expired': (),
    'shipping': ('delivered', 'refunded', 'charged back'),
    'delivered': ('refunded', 'charged back'),
}

OSCAR_ORDER_STATUS_PIPELINE['unknown'] = OSCAR_ORDER_STATUS_PIPELINE.keys()

OSCAR_LINE_STATUS_PIPELINE = OSCAR_ORDER_STATUS_PIPELINE

OSCAR_ORDER_STATUS_CASCADE = {
    # Let global states cascade to the order lines too.
    'paid': 'paid',
    'cancelled': 'cancelled',
    'charged back': 'charged back',
    'expired': 'expired',
}

########################################################
########### TROPIPAY CONFIGURATION VARIABLES ###########
########################################################

# Test:
DOCDATA_MERCHANT_NAME = os.environ.get("DOCDATA_MERCHANT_NAME", "")
DOCDATA_MERCHANT_PASSWORD = os.environ.get("DOCDATA_MERCHANT_PASSWORD", "")
DOCDATA_TESTING = True

# The payment-methods profile that is created in the Docdata Backoffice. By default, this is named "standard".
DOCDATA_PROFILE = os.environ.get("DOCDATA_PROFILE", "standard")

# URLs
DOCDATA_SUCCESS_URL = reverse_lazy('checkout:thank-you')
DOCDATA_PENDING_URL = reverse_lazy('checkout:thank-you')
DOCDATA_CANCELLED_URL = '/'
DOCDATA_ERROR_URL = '/'

# Extend dashboard
OSCAR_DASHBOARD_NAVIGATION[2]['children'].insert(1, {
    'label': _('Docdata Orders'),
    'url_name': 'docdata-order-list',
})

# Payment choices
WEBSHOP_PAYMENT_CHOICES = (
    ('IDEAL', 'iDEAL'),
    ('VISA', 'Visa'),
    ('MASTERCARD', 'MasterCard'),
    ('AMEX', 'American Express'),
    ('PAYPAL_EXPRESS_CHECKOUT', 'PayPal'),  # NOTE: has additional hack in checkout code for US.
)

# Don't show the payment selection form during the checkout process: leave it up to the docdata
# payment menu
SKIP_PAYMENT_CHOICES = bool(os.environ.get("SKIP_PAYMENT_CHOICES") == "1")

DOCDATA_ORDER_STATUS_MAPPING = {
    # DocdataOrder status values: new, in_progress, pending, paid, charged_back, cancelled, refunded, unknown
    # Map to our order pipeline, just remove the underscores. All other values are identical.
    'in_progress': "pending",         # Redirect phase
    'charged_back': "charged back",
}

SHIPPING_EVENT_STATUS_MAPPING = {
    # Translate shipping event type to OSCAR_ORDER_STATUS_PIPELINE/OSCAR_LINE_STATUS_PIPELINE
    'shipping': 'shipping',
    'delivered': 'delivered',
}
