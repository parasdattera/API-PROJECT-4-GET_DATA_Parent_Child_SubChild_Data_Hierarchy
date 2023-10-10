from django.db import connection


def dbop_get_data(progress_type_id):
    with connection.cursor() as cursor:
        cursor.callproc('public.get_progress_data',[progress_type_id])
        result = cursor.fetchall()
    return result
