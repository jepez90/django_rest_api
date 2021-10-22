from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate


class LoginApiView(GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
