from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.package.serializers.insights import CategorySerializer, FAQSerializer, CommentSerializer

# CategoryAdminAPIView Decorators
admin_create_category_swagger = swagger_auto_schema(
    operation_summary='Create a New Category (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new category record. '
        'The request must include required fields such as name and other category details. '
        'The response returns the created category details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    request_body=CategorySerializer,
    responses={
        201: CategorySerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_category_swagger = swagger_auto_schema(
    operation_summary='Retrieve Category Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific category by ID. '
        'The response includes details such as ID, name, and other category information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the category to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CategorySerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Category with the specified ID does not exist.'
    }
)

admin_update_category_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Category (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing category identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated category details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    request_body=CategorySerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the category to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CategorySerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Category with the specified ID does not exist.'
    }
)

admin_partial_update_category_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Category (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing category identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated category details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    request_body=CategorySerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the category to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CategorySerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Category with the specified ID does not exist.'
    }
)

admin_destroy_category_swagger = swagger_auto_schema(
    operation_summary='Delete a Category (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a category record by its ID. '
        'The operation permanently removes the category from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the category to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Category successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Category with the specified ID does not exist.'
    }
)

admin_list_category_swagger = swagger_auto_schema(
    operation_summary='List All Categories (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all category records. '
        'The response includes details for each category, such as ID, name, and other category information. '
        'Optional search functionality is available using the "search" query parameter to filter by name. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.category'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter categories by name (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CategorySerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# CategoryPublicAPIView Decorators
public_retrieve_category_swagger = swagger_auto_schema(
    operation_summary='Retrieve Category Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific category by ID. '
        'The response includes details such as ID, name, and other category information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.category'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the category to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CategorySerializer,
        404: 'Not Found: Category with the specified ID does not exist.'
    }
)

public_list_category_swagger = swagger_auto_schema(
    operation_summary='List All Categories (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all category records. '
        'The response includes details for each category, such as ID, name, and other category information. '
        'Optional search functionality is available using the "search" query parameter to filter by name. '
        'No authentication is required for this operation.'
    ),
    tags=['public.category'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter categories by name (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CategorySerializer(many=True)
    }
)

# FAQAdminAPIView Decorators
admin_create_faq_swagger = swagger_auto_schema(
    operation_summary='Create a New FAQ (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new FAQ record. '
        'The request must include required fields such as question, answer, and other FAQ details. '
        'The response returns the created FAQ details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    request_body=FAQSerializer,
    responses={
        201: FAQSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_faq_swagger = swagger_auto_schema(
    operation_summary='Retrieve FAQ Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific FAQ by ID. '
        'The response includes details such as ID, question, answer, and other FAQ information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the FAQ to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: FAQSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: FAQ with the specified ID does not exist.'
    }
)

admin_update_faq_swagger = swagger_auto_schema(
    operation_summary='Fully Update a FAQ (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing FAQ identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated FAQ details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    request_body=FAQSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the FAQ to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: FAQSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: FAQ with the specified ID does not exist.'
    }
)

admin_partial_update_faq_swagger = swagger_auto_schema(
    operation_summary='Partially Update a FAQ (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing FAQ identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated FAQ details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    request_body=FAQSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the FAQ to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: FAQSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: FAQ with the specified ID does not exist.'
    }
)

admin_destroy_faq_swagger = swagger_auto_schema(
    operation_summary='Delete a FAQ (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a FAQ record by its ID. '
        'The operation permanently removes the FAQ from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the FAQ to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'FAQ successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: FAQ with the specified ID does not exist.'
    }
)

admin_list_faq_swagger = swagger_auto_schema(
    operation_summary='List All FAQs (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all FAQ records. '
        'The response includes details for each FAQ, such as ID, question, answer, and other FAQ information. '
        'Optional search functionality is available using the "search" query parameter to filter by question. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.faq'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter FAQs by question (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: FAQSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# FAQPublicAPIView Decorators
public_retrieve_faq_swagger = swagger_auto_schema(
    operation_summary='Retrieve FAQ Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific FAQ by ID. '
        'The response includes details such as ID, question, answer, and other FAQ information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.faq'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the FAQ to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: FAQSerializer,
        404: 'Not Found: FAQ with the specified ID does not exist.'
    }
)

public_list_faq_swagger = swagger_auto_schema(
    operation_summary='List All FAQs (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all FAQ records. '
        'The response includes details for each FAQ, such as ID, question, answer, and other FAQ information. '
        'Optional search functionality is available using the "search" query parameter to filter by question. '
        'No authentication is required for this operation.'
    ),
    tags=['public.faq'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter FAQs by question (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: FAQSerializer(many=True)
    }
)

# CommentAdminAPIView Decorators
admin_create_comment_swagger = swagger_auto_schema(
    operation_summary='Create a New Comment (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new comment record. '
        'The request must include required fields such as content and other comment details. '
        'The response returns the created comment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    request_body=CommentSerializer,
    responses={
        201: CommentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_comment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Comment Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific comment by ID. '
        'The response includes details such as ID, content, and other comment information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the comment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CommentSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Comment with the specified ID does not exist.'
    }
)

admin_update_comment_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Comment (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing comment identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated comment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    request_body=CommentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the comment to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CommentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Comment with the specified ID does not exist.'
    }
)

admin_partial_update_comment_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Comment (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing comment identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated comment details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    request_body=CommentSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the comment to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CommentSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Comment with the specified ID does not exist.'
    }
)

admin_destroy_comment_swagger = swagger_auto_schema(
    operation_summary='Delete a Comment (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a comment record by its ID. '
        'The operation permanently removes the comment from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the comment to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Comment successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Comment with the specified ID does not exist.'
    }
)

admin_list_comment_swagger = swagger_auto_schema(
    operation_summary='List All Comments (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all comment records. '
        'The response includes details for each comment, such as ID, content, and other comment information. '
        'Optional search functionality is available using the "search" query parameter to filter by content. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.comment'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter comments by content (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CommentSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# CommentPublicAPIView Decorators
public_retrieve_comment_swagger = swagger_auto_schema(
    operation_summary='Retrieve Comment Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific comment by ID. '
        'The response includes details such as ID, content, and other comment information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.comment'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the comment to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CommentSerializer,
        404: 'Not Found: Comment with the specified ID does not exist.'
    }
)

public_list_comment_swagger = swagger_auto_schema(
    operation_summary='List All Comments (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all comment records. '
        'The response includes details for each comment, such as ID, content, and other comment information. '
        'Optional search functionality is available using the "search" query parameter to filter by content. '
        'No authentication is required for this operation.'
    ),
    tags=['public.comment'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter comments by content (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CommentSerializer(many=True)
    }
)