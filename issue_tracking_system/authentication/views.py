from rest_framework.generics import CreateAPIView


from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer
