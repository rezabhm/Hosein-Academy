from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.core.serializers import StudentInformationSerializer, TeacherSerializer

# StudentInformationAdminAPIView Decorators
admin_create_student_info_swagger = swagger_auto_schema(
    operation_summary='Create a New Student Information (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new student information record. '
        'The request must include required fields such as user_id and other student details. '
        'The response returns the created student information details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    request_body=StudentInformationSerializer,
    responses={
        201: StudentInformationSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_student_info_swagger = swagger_auto_schema(
    operation_summary='Retrieve Student Information Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific student by ID. '
        'The response includes details such as ID, user, and other student information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the student information to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: StudentInformationSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Student information with the specified ID does not exist.'
    }
)

admin_update_student_info_swagger = swagger_auto_schema(
    operation_summary='Fully Update Student Information (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing student information record identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated student information details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    request_body=StudentInformationSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the student information to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: StudentInformationSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Student information with the specified ID does not exist.'
    }
)

admin_partial_update_student_info_swagger = swagger_auto_schema(
    operation_summary='Partially Update Student Information (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing student information record identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated student information details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    request_body=StudentInformationSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the student information to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: StudentInformationSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Student information with the specified ID does not exist.'
    }
)

admin_destroy_student_info_swagger = swagger_auto_schema(
    operation_summary='Delete Student Information (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a student information record by its ID. '
        'The operation permanently removes the record from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the student information to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Student information successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Student information with the specified ID does not exist.'
    }
)

admin_list_student_info_swagger = swagger_auto_schema(
    operation_summary='List All Student Information (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all student information records. '
        'The response includes details for each record, such as ID, user, and other student information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.student_information'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter student information by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: StudentInformationSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# StudentInformationUserAPIView Decorators
user_retrieve_student_info_swagger = swagger_auto_schema(
    operation_summary='Retrieve Own Student Information',
    operation_description=(
        'This endpoint allows authenticated users to retrieve their own student information by ID. '
        'The response includes details such as ID, user, and other student information. '
        'This operation requires JWT authentication.'
    ),
    tags=['student_information'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the student information to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: StudentInformationSerializer,
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own student information.',
        404: 'Not Found: Student information with the specified ID does not exist.'
    }
)

user_list_student_info_swagger = swagger_auto_schema(
    operation_summary='List Own Student Information',
    operation_description=(
        'This endpoint allows authenticated users to retrieve a list of their own student information records. '
        'The response includes details for each record, such as ID, user, and other student information. '
        'This operation requires JWT authentication.'
    ),
    tags=['student_information'],
    responses={
        200: StudentInformationSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required.',
        403: 'Forbidden: User can only access their own student information.'
    }
)

# TeacherAdminAPIView Decorators
admin_create_teacher_swagger = swagger_auto_schema(
    operation_summary='Create a New Teacher (Admin)',
    operation_description=(
        'This endpoint allows administrators to create a new teacher record. '
        'The request must include required fields such as user_id and other teacher details. '
        'The response returns the created teacher’s details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    request_body=TeacherSerializer,
    responses={
        201: TeacherSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

admin_retrieve_teacher_swagger = swagger_auto_schema(
    operation_summary='Retrieve Teacher Details (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve detailed information about a specific teacher by ID. '
        'The response includes details such as ID, user, and other teacher information. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the teacher to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TeacherSerializer,
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Teacher with the specified ID does not exist.'
    }
)

admin_update_teacher_swagger = swagger_auto_schema(
    operation_summary='Fully Update a Teacher (Admin)',
    operation_description=(
        'This endpoint allows administrators to fully update the details of an existing teacher identified by its ID. '
        'The request body must include all required fields even if some fields remain unchanged. '
        'The response returns the updated teacher’s details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    request_body=TeacherSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the teacher to update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TeacherSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Teacher with the specified ID does not exist.'
    }
)

admin_partial_update_teacher_swagger = swagger_auto_schema(
    operation_summary='Partially Update a Teacher (Admin)',
    operation_description=(
        'This endpoint allows administrators to partially update the details of an existing teacher identified by its ID. '
        'Only the provided fields in the request body will be updated. '
        'The response returns the updated teacher’s details. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    request_body=TeacherSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the teacher to partially update.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TeacherSerializer,
        400: 'Invalid input data.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Teacher with the specified ID does not exist.'
    }
)

admin_destroy_teacher_swagger = swagger_auto_schema(
    operation_summary='Delete a Teacher (Admin)',
    operation_description=(
        'This endpoint allows administrators to delete a teacher record by its ID. '
        'The operation permanently removes the teacher from the system. '
        'A successful deletion returns a 204 No Content response. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The unique ID of the teacher to delete.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'Teacher successfully deleted.',
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.',
        404: 'Not Found: Teacher with the specified ID does not exist.'
    }
)

admin_list_teacher_swagger = swagger_auto_schema(
    operation_summary='List All Teachers (Admin)',
    operation_description=(
        'This endpoint allows administrators to retrieve a list of all teacher records in the system. '
        'The response includes details for each teacher, such as ID, user, and other teacher information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'This operation is restricted to admin users only and requires JWT authentication.'
    ),
    tags=['admin.teacher'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter teachers by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: TeacherSerializer(many=True),
        401: 'Unauthorized: Valid JWT token required for admin users.',
        403: 'Forbidden: User is not an admin.'
    }
)

# TeacherPublicAPIView Decorators
public_retrieve_teacher_swagger = swagger_auto_schema(
    operation_summary='Retrieve Teacher Details (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve detailed information about a specific teacher by ID. '
        'The response includes details such as ID, user, and other teacher information. '
        'No authentication is required for this operation.'
    ),
    tags=['public.teacher'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="The ID of the teacher to retrieve.", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: TeacherSerializer,
        404: 'Not Found: Teacher with the specified ID does not exist.'
    }
)

public_list_teacher_swagger = swagger_auto_schema(
    operation_summary='List All Teachers (Public)',
    operation_description=(
        'This endpoint allows public access to retrieve a list of all teacher records in the system. '
        'The response includes details for each teacher, such as ID, user, and other teacher information. '
        'Optional search functionality is available using the "search" query parameter to filter by user username. '
        'No authentication is required for this operation.'
    ),
    tags=['public.teacher'],
    manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Filter teachers by user username (partial match).", type=openapi.TYPE_STRING)
    ],
    responses={
        200: TeacherSerializer(many=True)
    }
)