from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

import jwt
from django.contrib.auth.models import AnonymousUser
from jwt import InvalidTokenError

User = get_user_model()


def decode_jwt(token):
    try:
        decoded_data = jwt.decode(
            jwt=token, key='secret', algorithms=["HS256"]
        )

        return decoded_data
    except InvalidTokenError:
        print('Error decoding JWT token')
        return None


class APIBackend(BaseBackend):

    def authenticate(self, request, token):
        print('\n*\n*\n*\nIM AUTHENTICATING\n*\n*\n*\n*\n*\n*')
        decoded_data = decode_jwt(token)
        if decoded_data:
            print('decoded data: ', decoded_data)
            email = decoded_data.get('email')
            organization = decoded_data.get('organization_id')
            name = decoded_data.get('name')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User(username=name)
                user.email = email
                user.organization_id = organization
                user.save()
            return user
        return AnonymousUser()

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None