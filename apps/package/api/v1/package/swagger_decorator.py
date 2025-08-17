from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.package.serializers.package import CourseSerializer, SeasonSerializer, LessonSerializer

# CourseAdminAPIView Decorators
admin_create_course_swagger = swagger_auto_schema(
    operation_summary='Create a New Course (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new course record. '
        'The request must include required fields such as title and other course details. '
        'The response returns the created course details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    request_body=CourseSerializer,
    responses={
        201: CourseSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_course_swagger = swagger_auto_schema(
    operation_summary='Retrieve Course Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific course by ID. '
        'The response includes details such as ID, title, and other course information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the course to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CourseSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Course with the specified ID does not exist.'
    }
)

admin_update_course_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Course (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing course identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated course details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    request_body=CourseSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the course to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CourseSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Course with the specified ID does not exist.'
    }
)

admin_partial_update_course_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Course (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing course identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated course details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    request_body=CourseSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the course to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CourseSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Course with the specified ID does not exist.'
    }
)

admin_destroy_course_swagger = swagger_auto_schema(
    operation_summary='Delete a Course (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a course record by its ID. '
        'The operation permanently removes the course from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the course to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Course successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Course with the specified ID does not exist.'
    }
)

admin_list_course_swagger = swagger_auto_schema(
    operation_summary='List All Courses (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all course records. '
        'The response includes details for each course, such as ID, title, and other course information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.course'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter courses by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CourseSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# CoursePublicAPIView Decorators
public_retrieve_course_swagger = swagger_auto_schema(
    operation_summary='Retrieve Course Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific course by ID. '
        'The response includes details such as ID, title, and other course information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.course'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the course to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: CourseSerializer,
        404: 'Not Found: Course with the specified ID does not exist.'
    }
)

public_list_course_swagger = swagger_auto_schema(
    operation_summary='List All Courses (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all course records. '
        'The response includes details for each course, such as ID, title, and other course information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'No authentication is required for this operation.'
    ),
    tags=['public.course'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter courses by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: CourseSerializer(many=True)
    }
)

# SeasonAdminAPIView Decorators
admin_create_season_swagger = swagger_auto_schema(
    operation_summary='Create a New Season (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new season record. '
        'The request must include required fields such as course_id, title, and other season details. '
        'The response returns the created season details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    request_body=SeasonSerializer,
    responses={
        201: SeasonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_season_swagger = swagger_auto_schema(
    operation_summary='Retrieve Season Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific season by ID. '
        'The response includes details such as ID, course, title, and other season information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the season to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SeasonSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Season with the specified ID does not exist.'
    }
)

admin_update_season_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Season (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing season identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated season details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    request_body=SeasonSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the season to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SeasonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Season with the specified ID does not exist.'
    }
)

admin_partial_update_season_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Season (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing season identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated season details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    request_body=SeasonSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the season to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SeasonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Season with the specified ID does not exist.'
    }
)

admin_destroy_season_swagger = swagger_auto_schema(
    operation_summary='Delete a Season (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a season record by its ID. '
        'The operation permanently removes the season from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the season to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Season successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Season with the specified ID does not exist.'
    }
)

admin_list_season_swagger = swagger_auto_schema(
    operation_summary='List All Seasons (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all season records. '
        'The response includes details for each season, such as ID, course, title, and other season information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.season'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter seasons by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: SeasonSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# SeasonPublicAPIView Decorators
public_retrieve_season_swagger = swagger_auto_schema(
    operation_summary='Retrieve Season Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific season by ID. '
        'The response includes details such as ID, course, title, and other season information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.season'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the season to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: SeasonSerializer,
        404: 'Not Found: Season with the specified ID does not exist.'
    }
)

public_list_season_swagger = swagger_auto_schema(
    operation_summary='List All Seasons (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all season records. '
        'The response includes details for each season, such as ID, course, title, and other season information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'No authentication is required for this operation.'
    ),
    tags=['public.season'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter seasons by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: SeasonSerializer(many=True)
    }
)

# LessonAdminAPIView Decorators
admin_create_lesson_swagger = swagger_auto_schema(
    operation_summary='Create a New Lesson (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new lesson record. '
        'The request must include required fields such as season_id, title, and other lesson details. '
        'The response returns the created lesson details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    request_body=LessonSerializer,
    responses={
        201: LessonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_lesson_swagger = swagger_auto_schema(
    operation_summary='Retrieve Lesson Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific lesson by ID. '
        'The response includes details such as ID, season, title, and other lesson information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the lesson to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: LessonSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Lesson with the specified ID does not exist.'
    }
)

admin_update_lesson_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Lesson (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing lesson identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated lesson details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    request_body=LessonSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the lesson to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: LessonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Lesson with the specified ID does not exist.'
    }
)

admin_partial_update_lesson_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Lesson (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing lesson identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated lesson details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    request_body=LessonSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the lesson to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: LessonSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Lesson with the specified ID does not exist.'
    }
)

admin_destroy_lesson_swagger = swagger_auto_schema(
    operation_summary='Delete a Lesson (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a lesson record by its ID. '
        'The operation permanently removes the lesson from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the lesson to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Lesson successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Lesson with the specified ID does not exist.'
    }
)

admin_list_lesson_swagger = swagger_auto_schema(
    operation_summary='List All Lessons (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all lesson records. '
        'The response includes details for each lesson, such as ID, season, title, and other lesson information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.lesson'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter lessons by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: LessonSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# LessonPublicAPIView Decorators
public_retrieve_lesson_swagger = swagger_auto_schema(
    operation_summary='Retrieve Lesson Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific lesson by ID. '
        'The response includes details such as ID, season, title, and other lesson information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.lesson'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the lesson to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: LessonSerializer,
        404: 'Not Found: Lesson with the specified ID does not exist.'
    }
)

public_list_lesson_swagger = swagger_auto_schema(
    operation_summary='List All Lessons (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all lesson records. '
        'The response includes details for each lesson, such as ID, season, title, and other lesson information. '
        'Optional search functionality is available using the "search" query parameter to filter by title. '
        'No authentication is required for this operation.'
    ),
    tags=['public.lesson'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter lessons by title (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: LessonSerializer(many=True)
    }
)