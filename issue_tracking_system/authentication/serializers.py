from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        elif self.validate_digits_letters(attrs["username"]) is False:
            raise serializers.ValidationError(
                {"username": "Username should not have special characters."}
            )
        elif self.validate_digits_letters(attrs["password"]) is False:
            raise serializers.ValidationError(
                {"password": "Password should not have special characters."}
            )
        elif self.validate_digits_letters(attrs["first_name"]) is False:
            raise serializers.ValidationError(
                {"first_name": "First name should not have special characters."}
            )
        elif self.validate_digits_letters(attrs["last_name"]) is False:
            raise serializers.ValidationError(
                {"last_name": "Last name should not have special characters."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

    def validate_digits_letters(self, word):
        for char in word:
            if not char.isdigit() and not char.isalpha():
                return False
        return True
