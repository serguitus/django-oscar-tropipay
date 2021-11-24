====================
django-oscar-tropipay
====================

Payment gateway integration for `TropiPay <http://tropipay.com/>`_ in django-oscar_.
TropiPay is a large payment gateway that supports international payment methods.

.. _django-oscar: https://github.com/django-oscar/django-oscar

TODO
.. image:: https://travis-ci.org/django-oscar/django-oscar-tropipay.svg?branch=master
    :target: https://travis-ci.org/django-oscar/django-oscar-tropipay

TODO
.. image:: https://badge.fury.io/py/django-oscar-tropipay.svg
   :alt: Latest PyPi release
   :target: https://pypi.python.org/pypi/django-oscar-tropipay


Installation
============

Install via pip:

.. code-block:: bash

    pip install django-oscar-tropipay


Configuration
-------------

Configure the application:

`TROPIPAY_SELLER_EMAIL`
    Credentials as supplied by the payment provider.

`TROPIPAY_SELLER_PASSWORD`
    Credentials as supplied by the payment provider.

`TROPIPAY_TESTING`
    Whether or not to run in testing mode. Defaults to `True`.

Add to ``urls.py``:

.. code-block:: python

    from tropipay.dashboard.app import application as tropipay_dashboard_app

    urlpatterns += [
        url(r'^api/tropipay/', include('tropipay.urls')),
        url(r'^dashboard/tropipay/', include(tropipay_dashboard_app.urls)),
    ]

Add to ``settings.py``:

.. code-block:: python

    OSCAR_DASHBOARD_NAVIGATION[2]['children'].insert(1, {
        'label': _('TropiPay Orders'),
        'url_name': 'tropipay-order-list',
    })

While developing, enabling logging for `requests` and `tropipay` is recommended to see
detailed information:

.. code-block:: python

    LOGGING = {
        # ...
        'loggers': {
            # ...
            'requests': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'tropipay': {
                'handlers': ['mail_admins', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }


Integration into your project
-----------------------------

Please view the `sandbox application`_ how to integrate the application.
This includes the project-specific decisions such as:

* How to create payment events.
* How to create a custom facade class
* Whether to cancel an order when the customer aborted the payment.
* When to submit confirmation emails.


Local development and running the tests
---------------------------------------

You can use the included Makefile to install a development environment and to run the flake8 checker and the testrunner.
Make sure you do this inside a virtualenv:

.. code-block:: bash

    TODO
    git clone git@github.com:django-oscar/django-oscar-tropipay.git

    cd django-oscar-tropipay
    make install
    make lint
    make test


Running the Sandbox application
-------------------------------

It is possible to run the `sandbox application`_ to test this package and to see if your TropiPay credentials work.
You can set the `TROPIPAY_SELLER_NAME` and `TROPIPAY_SELLER_PASSWORD` environment variables before running `manage.py`:

.. code-block:: bash

    # creates a local sqlite database
    ./sandbox/manage.py migrate

    # loads some sample products (books)
    ./sandbox/manage.py oscar_import_catalogue sandbox/fixtures/books.csv

    # so you can fill out your shipping address
    ./sandbox/manage.py loaddata sandbox/fixtures/countries.json

    # run the sandbox installation with the tropipay seller email and password
    TROPIPAY_SELLER_NAME=seller@email TROPIPAY_SELLER_PASSWORD=seller_password ./sandbox/manage.py runserver


Configuration of the TropiPay Backoffice
---------------------------------------

Make sure the following settings are configured:

* The "Payment Method names" need to be added.
* The notification URL and return URL need to be set. Example values:

 * Success: ``http://example.org/api/tropipay/update_order/?callback=SUCCESS&order_id=``
 * Failed: ``http://example.org/api/tropipay/update_order/?callback=FAILED&order_id=``
 * Notification: ``http://example.org/api/tropipay/update_order/?callback=NOTIFICATION&order_id=``


TropiPay Service Specification
-------------------------------------

See the `<https://tpp.stoplight.io/docs/tropipay-api-doc/reference/>` for detailed technical information.
