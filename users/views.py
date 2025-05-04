from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]  # Anyone can access this endpoint

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # This creates a session and sets a sessionid cookie
            return Response({"message": "Login successful!"})
        else:
            return Response({"message": "Invalid credentials"}, status=400)
