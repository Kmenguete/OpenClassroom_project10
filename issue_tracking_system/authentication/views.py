from .models import User
from rest_framework.views import APIView

from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny


class SignUpView(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer
