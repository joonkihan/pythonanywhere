from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("파이썬으로 제작한 첫번째 페이지 입니다")

