from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.

class ContactView(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = request.data
            html_message = render_to_string('email.html', {'context': context})
            send_mail(
            'CONTACT FORM',
            strip_tags(html_message),
            f'{settings.EMAIL_HOST_USER}',
            ['brianebrahimi@gmail.com'],
            fail_silently=False,
            html_message=html_message
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)