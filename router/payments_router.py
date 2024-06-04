import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
import stripe
router = APIRouter()


stripe.api_key = 'sk_test_51PEHtQRuE32NAoOjrVMXtKwv3Qwt7Mw0jV7fwWFTRUqUma2i3NVdBGY3ygRuPrWdaIb0mNAm4sgd8BSfYGsIz8gf00ZOL7Px6I'


@router.post("/create-payment",
             response_model=schema.orders_scheme.OrdersGetResponse,
             summary="Create payment",
             response_description="Create payment",
             description="Create payment",
             operation_id="CreatePayment")
async def service(values: schema.orders_scheme.OrdersPostStripe):
    user = database.user_database.return_user_by_id(values.user_id)
    if user is not None:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(values.amount * 100),
            currency=values.currency,
            customer=user['stripe_id']
        )
        if payment_intent.client_secret is not None:
            database.orders_database.add_payment(values)
            return {"msg": "success", "data": {"cliente_secret": payment_intent.client_secret}}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
                msg="Payment not created, check values",
                type="error",
                data="Payment not created, check values"
            )))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.post("/create-payment-no-account",
             response_model=schema.orders_scheme.OrdersGetResponse,
             summary="Create payment no account",
             response_description="Create payment no account",
             description="Create payment no account",
             operation_id="CreatePaymentNoAccount")
async def service(request: schema.orders_scheme.OrdersPostStripe):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(request.amount * 100),
            currency=request.currency
        )
        database.orders_database.add_payment(request)
        return {"msg": "success", "data": {"cliente_secret": payment_intent.client_secret}}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Payment not created",
            type="error",
            data="Payment not created"
        )))


@router.post("/create-subscription",
             response_model=schema.orders_scheme.OrdersGetResponse,
             summary="Create subscription",
             response_description="Create subscription",
             description="Create subscription",
             operation_id="CreateSubscription")
async def service(values: schema.orders_scheme.CreateSubscriptionRequest):
    user = database.user_database.return_user_by_email(values.email)
    if user is not None:
        stripe.PaymentMethod.attach(
            values.payment_method_id,
            customer=user['stripe_id'],
        )
        stripe.Customer.modify(
            user['stripe_id'],
            invoice_settings={
                'default_payment_method': values.payment_method_id,
            },
        )
        subscription = stripe.Subscription.create(
            customer=user['stripe_id'],
            items=[
                {
                    'price': values.price_id,
                },
            ],
            expand=['latest_invoice.payment_intent'],
        )
        if subscription is not None:
            database.user_database.update_is_subscribed_by_email(values.email, True)
            database.user_database.update_subscription_id_by_email(values.email, subscription.id)
            return {"msg": "success", "data": {
                "subscription_id": subscription.id,
                "client_secret": subscription.latest_invoice.payment_intent.client_secret
            }}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.post("/cancel-subscription",
             response_model=schema.orders_scheme.OrdersGetResponse,
             summary="Cancel subscription",
             response_description="Cancel subscription",
             description="Cancel subscription",
             operation_id="CancelSubscription"
             )
async def service(values: schema.orders_scheme.CancelSubscriptionRequest):
    user = database.user_database.return_user_by_email(values.email)
    if user is not None:
        canceled_subscription = stripe.Subscription.delete(values.subscription_id)
        database.user_database.update_is_subscribed_by_email(values.email, False)
        database.user_database.update_subscription_id_by_email(values.email, "")
        return {"msg": "success", "data": {
            "subscription": canceled_subscription
        }}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))