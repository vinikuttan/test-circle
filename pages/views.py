from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.
from django.views.generic import View



class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Home successfull!'})


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'About successfull!'})
