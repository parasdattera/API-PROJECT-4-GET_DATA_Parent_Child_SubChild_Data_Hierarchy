import json
from django.shortcuts import render
from django.http import JsonResponse
from .dboperations import dbop_get_data
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def API_get_data(request):
    try:
        if request.method == 'POST':
            progress_type_id = request.data.get('progress_type_id')
            if progress_type_id is not None:
                result = dbop_get_data(progress_type_id)
                # Parse the JSON string into a JSON object
                result = json.loads(result[0][0])
                return JsonResponse(result , safe=False)
            else:
                return Response({'error':'Missing input value.'}, status=400)
    except Exception as e:
        return Response({'error': 'An error occurred'}, status=500)