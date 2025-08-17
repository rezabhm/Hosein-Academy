from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.payment.serializers.subscription import SubscriptionSerializer, InstallmentPaymentSerializer, ImmediatePaymentSerializer

# SubscriptionAdminAPIView Decorators
admin_create_subscription_swagger = swagger_auto_schema(
    operation_summary='Create a New Subscription (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new subscription record. '
        'The request must include required fields such as user_id, plan details, and other subscription information. '
        'The response returns the created subscription details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    request_body=SubscriptionSerializer,
    responses={
        201: SubscriptionSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_subscription_swagger = swagger_auto_schema(
    operation_summary='Retrieve Subscription Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific subscription by ID. '
        'The response includes details such as ID, user, plan, and other subscription information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the subscription to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SubscriptionSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Subscription with the specified ID does not exist.'
    }
)

admin_update_subscription_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Subscription (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing subscription identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated subscription details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    request_body=SubscriptionSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the subscription to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SubscriptionSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Subscription with the specified ID does not exist.'
    }
)

admin_partial_update_subscription_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Subscription (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing subscription identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated subscription details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    request_body=SubscriptionSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the subscription to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SubscriptionSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Subscription with the specified ID does not exist.'
    }
)

admin_destroy_subscription_swagger = swagger_auto_schema(
    operation_summary='Delete a Subscription (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a subscription record by its ID. '
        'The operation permanently removes the subscription from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the subscription to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Subscription successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Subscription with the specified ID does not exist.'
    }
)

admin_list_subscription_swagger = swagger_auto_schema(
    operation_summary='List All Subscriptions (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all subscription records. '
        'The response includes details for each subscription, such as ID, user, plan, and other subscription information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.subscription'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter subscriptions by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: SubscriptionSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# SubscriptionUserAPIView Decorators
user_retrieve_subscription_swagger = swagger_auto_schema(
    operation_summary='Retrieve Own Subscription',
    operation_description=(
        'This endpoint allows authenticated users to retrieve their own subscription by ID. '
        'The response includes details such as ID, user, plan, and other subscription information. '
        'This operation requires JWT authentication.'
    ),
    tags=['subscription'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the subscription to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SubscriptionSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own subscriptions.',
        404: 'Not Found: Subscription with the specified ID does not exist.'
    }
)

user_list_subscription_swagger = swagger_auto_schema(
    operation_summary='List Own Subscriptions',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of their own subscription records. '
        'The response includes details for each subscription, such as ID, user, plan, and other subscription information. '
        'This operation requires JWT authentication.'
    ),
    tags=['subscription'],
    responses={
        200: SubscriptionSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own subscriptions.'
    }
)

# InstallmentPaymentAdminAPIView Decorators
admin_create_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Create a New Installment Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new installment payment record. '
        'The request must include required fields such as user_id, subscription_id, amount, and other payment details. '
        'The response returns the created installment payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    request_body=InstallmentPaymentSerializer,
    responses={
        201: InstallmentPaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Installment Payment Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific installment payment by ID. '
        'The response includes details such as ID, user, subscription, amount, and other payment information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the installment payment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: InstallmentPaymentSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Installment payment with the specified ID does not exist.'
    }
)

admin_update_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Fully Update an Installment Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing installment payment identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated installment payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    request_body=InstallmentPaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the installment payment to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: InstallmentPaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Installment payment with the specified ID does not exist.'
    }
)

admin_partial_update_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Partially Update an Installment Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing installment payment identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated installment payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    request_body=InstallmentPaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the installment payment to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: InstallmentPaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Installment payment with the specified ID does not exist.'
    }
)

admin_destroy_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Delete an Installment Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete an installment payment record by its ID. '
        'The operation permanently removes the installment payment from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the installment payment to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Installment payment successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Installment payment with the specified ID does not exist.'
    }
)

admin_list_installment_payment_swagger = swagger_auto_schema(
    operation_summary='List All Installment Payments (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all installment payment records. '
        'The response includes details for each payment, such as ID, user, subscription, amount, and other payment information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.installment_payment'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter installment payments by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: InstallmentPaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# InstallmentPaymentUserAPIView Decorators
user_retrieve_installment_payment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Own Installment Payment',
    operation_description=(
        'This endpoint allows authenticated users to retrieve their own installment payment by ID. '
        'The response includes details such as ID, user, subscription, amount, and other payment information. '
        'This operation requires JWT authentication.'
    ),
    tags=['installment_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the installment payment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: InstallmentPaymentSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own installment payments.',
        404: 'Not Found: Installment payment with the specified ID does not exist.'
    }
)

user_list_installment_payment_swagger = swagger_auto_schema(
    operation_summary='List Own Installment Payments',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of their own installment payment records. '
        'The response includes details for each payment, such as ID, user, subscription, amount, and other payment information. '
        'This operation requires JWT authentication.'
    ),
    tags=['installment_payment'],
    responses={
        200: InstallmentPaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own installment payments.'
    }
)

# ImmediatePaymentAdminAPIView Decorators
admin_create_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Create a New Immediate Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new immediate payment record. '
        'The request must include required fields such as user_id, subscription_id, amount, and other payment details. '
        'The response returns the created immediate payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    request_body=ImmediatePaymentSerializer,
    responses={
        201: ImmediatePaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Immediate Payment Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific immediate payment by ID. '
        'The response includes details such as ID, user, subscription, amount, and other payment information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the immediate payment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: ImmediatePaymentSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Immediate payment with the specified ID does not exist.'
    }
)

admin_update_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Fully Update an Immediate Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing immediate payment identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated immediate payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    request_body=ImmediatePaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the immediate payment to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: ImmediatePaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Immediate payment with the specified ID does not exist.'
    }
)

admin_partial_update_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Partially Update an Immediate Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing immediate payment identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated immediate payment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    request_body=ImmediatePaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the immediate payment to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: ImmediatePaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Immediate payment with the specified ID does not exist.'
    }
)

admin_destroy_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Delete an Immediate Payment (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete an immediate payment record by its ID. '
        'The operation permanently removes the immediate payment from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the immediate payment to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Immediate payment successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Immediate payment with the specified ID does not exist.'
    }
)

admin_list_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='List All Immediate Payments (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all immediate payment records. '
        'The response includes details for each payment, such as ID, user, subscription, amount, and other payment information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.immediate_payment'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter immediate payments by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: ImmediatePaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# ImmediatePaymentUserAPIView Decorators
user_retrieve_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Own Immediate Payment',
    operation_description=(
        'This endpoint allows authenticated users to retrieve their own immediate payment by ID. '
        'The response includes details such as ID, user, subscription, amount, and other payment information. '
        'This operation requires JWT authentication.'
    ),
    tags=['immediate_payment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the immediate payment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: ImmediatePaymentSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own immediate payments.',
        404: 'Not Found: Immediate payment with the specified ID does not exist.'
    }
)

user_list_immediate_payment_swagger = swagger_auto_schema(
    operation_summary='List Own Immediate Payments',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of their own immediate payment records. '
        'The response includes details for each payment, such as ID, user, subscription, amount, and other payment information. '
        'This operation requires JWT authentication.'
    ),
    tags=['immediate_payment'],
    responses={
        200: ImmediatePaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own immediate payments.'
    }
)