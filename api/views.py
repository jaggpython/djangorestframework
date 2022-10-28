from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
