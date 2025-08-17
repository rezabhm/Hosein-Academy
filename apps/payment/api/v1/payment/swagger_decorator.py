from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.payment.serializers.payment import PaymentSerializer

# TransactionAdminAPIView Decorators
admin_create_transaction_swagger = swagger_auto_schema(
    operation_summary='Create a New Transaction (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new transaction record. '
        'The request must include required fields such as user_id, amount, and other transaction details. '
        'The response returns the created transaction details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    request_body=PaymentSerializer,
    responses={
        201: PaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_transaction_swagger = swagger_auto_schema(
    operation_summary='Retrieve Transaction Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific transaction by ID. '
        'The response includes details such as ID, user, amount, and other transaction information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the transaction to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: PaymentSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Transaction with the specified ID does not exist.'
    }
)

admin_update_transaction_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Transaction (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing transaction identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated transaction details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    request_body=PaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the transaction to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: PaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Transaction with the specified ID does not exist.'
    }
)

admin_partial_update_transaction_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Transaction (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing transaction identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated transaction details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    request_body=PaymentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the transaction to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: PaymentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Transaction with the specified ID does not exist.'
    }
)

admin_destroy_transaction_swagger = swagger_auto_schema(
    operation_summary='Delete a Transaction (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a transaction record by its ID. '
        'The operation permanently removes the transaction from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the transaction to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Transaction successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Transaction with the specified ID does not exist.'
    }
)

admin_list_transaction_swagger = swagger_auto_schema(
    operation_summary='List All Transactions (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all transaction records. '
        'The response includes details for each transaction, such as ID, user, amount, and other transaction information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.transaction'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter transactions by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: PaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# TransactionUserAPIView Decorators
user_retrieve_transaction_swagger = swagger_auto_schema(
    operation_summary='Retrieve Own Transaction',
    operation_description=(
        'This endpoint allows authenticated users to retrieve their own transaction by ID. '
        'The response includes details such as ID, user, amount, and other transaction information. '
        'This operation requires JWT authentication.'
    ),
    tags=['transaction'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the transaction to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: PaymentSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own transactions.',
        404: 'Not Found: Transaction with the specified ID does not exist.'
    }
)

user_list_transaction_swagger = swagger_auto_schema(
    operation_summary='List Own Transactions',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of their own transaction records. '
        'The response includes details for each transaction, such as ID, user, amount, and other transaction information. '
        'This operation requires JWT authentication.'
    ),
    tags=['transaction'],
    responses={
        200: PaymentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own transactions.'
    }
)