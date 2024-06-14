from django.shortcuts import render
from django.http import HttpResponse

def attendance_view(request):
    return HttpResponse("<h1>Attendance leevel view</h1>")

def exam_view(request):
    return HttpResponse("<h1>Exam leevel view</h1>")

