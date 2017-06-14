# -*- coding: utf-8 -*-

import logging
import math

from billing.models import Order

from portal.models import UserProfile

from iugu.customer import Customer, PaymentMethod
from iugu.subscription import Subscription
from iugu.token import Token
from iugu.transfer import Transfer

from django.conf import settings
from django.utils import timezone


class BillingService:
    def create_remote_customer(self, user):

        try:
            profile = user.userprofile
        except:
            profile = UserProfile()
            profile.user = user
            profile.save()

        if not profile.remote_customer_id:
            data = {
                'email': user.email,
            }

            customer = Customer()
            res = customer.create(data)

            if res['id']:
                user.userprofile.remote_customer_id = res['id']
                user.userprofile.save()

        if user.userprofile.remote_customer_id:
            return user

        return False

    def transfer(self, product):

        percent_commission = settings.IUGU_COMMISSION_MARKET_PLACE

        math_result = math.ceil(float(product.price) * float(percent_commission))
        amount_cents = math_result * 100

        data_commission = {
            'receiver_id': settings.IUGU_ACCOUNT_ID,
            'amount_cents': amount_cents,
        }

        transfer = Transfer().create(data_commission)

        return transfer

    def charge(self, user, product, payment_data):
        remote_user = self.create_remote_customer(user)
        data_token = {
            'account_id': settings.IUGU_ACCOUNT_ID,
            'method': 'credit_card',
            'data': payment_data['data']
        }

        token = Token().create(data_token)
        logging.warning(token)

        if 'errors' in token:
            return False

        data = {
            'items': {
                'description': product.name + ' - Setup',
                'quantity': 1,
                'price_cents': str(product.price).replace(".", ""),
            },
            'token': token['id'],
            'email': user.email,
            'customer_id': user.userprofile.remote_customer_id,
        }

        charge = Token().charge(data)
        logging.warning(charge)
        if 'success' in charge:
            if charge['success']:
                logging.warning("sucesso")
                order = Order()
                order.user = user
                order.merchant = product.user
                order.product = product
                order.status = "Approved"
                order.payment_date = timezone.now()
                order.total = product.price

                if not settings.DEBUG:
                    transfer_commission = self.transfer(product)
                    order.commission = transfer_commission['amount_localized']

                order.save()
                return order
        else:
            return False
