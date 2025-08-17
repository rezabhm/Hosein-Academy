from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.textbook.serializers import TextBookSerializer

# TextBookAdminAPIView Decorators
admin_create_textbook_swagger = swagger_auto_schema(
    operation_summary='Create a New Textbook (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new textbook record. '
        'The request must include required fields such as title and other textbook details. '
        'The response returns the created textbook details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    request_body=TextBookSerializer,
    responses={
        201: TextBookSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_textbook_swagger = swagger_auto_schema(
    operation_summary='Retrieve Textbook Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific textbook by ID. '
        'The response includes details such as ID, title, and other textbook information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the textbook to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TextBookSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Textbook with the specified ID does not exist.'
    }
)

admin_update_textbook_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Textbook (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing textbook identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated textbook details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    request_body=TextBookSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the textbook to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TextBookSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Textbook with the specified ID does not exist.'
    }
)

admin_partial_update_textbook_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Textbook (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing textbook identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated textbook details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    request_body=TextBookSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the textbook to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TextBookSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Textbook with the specified ID does not exist.'
    }
)

admin_destroy_textbook_swagger = swagger_auto_schema(
    operation_summary='Delete a Textbook (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a textbook record by its ID. '
        'The operation permanently removes the textbook from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the textbook to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Textbook successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Textbook with the specified ID does not exist.'
    }
)

admin_list_textbook_swagger = swagger_auto_schema(
    operation_summary='List All Textbooks (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all textbook records. '
        'The response includes details for each textbook, such as ID, title, and other textbook information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.textbook'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter textbooks by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: TextBookSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# TextBookPublicAPIView Decorators
user_retrieve_textbook_swagger = swagger_auto_schema(
    operation_summary='Retrieve Textbook Details (Authenticated)',
    operation_description=(
        'This endpoint allows authenticated users to retrieve detailed information about a specific textbook by ID. '
        'The response includes details such as ID, title, and other textbook information. '
        'This operation requires JWT authentication.'
    ),
    tags=['textbook'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the textbook to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TextBookSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        404: 'Not Found: Textbook with the specified ID does not exist.'
    }
)

user_list_textbook_swagger = swagger_auto_schema(
    operation_summary='List All Textbooks (Authenticated)',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of all textbook records. '
        'The response includes details for each textbook, such as ID, title, and other textbook information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'This operation requires JWT authentication.'
    ),
    tags=['textbook'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter textbooks by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: TextBookSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.'
    }
)