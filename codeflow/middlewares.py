
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from codeflow.auth import APIBackend

PREFIX = 'Bearer '


def get_token(header):
    if not header.startswith(PREFIX):
        return ''

    return header[len(PREFIX):]


class ProcessRequestMiddleware(MiddlewareMixin):
    def process_request(self, request, **kwargs):
        header = request.headers.get('Authorization')
        if header:
            token = get_token(header)
            user = APIBackend.authenticate(request.user, request, token)
            request.user = user

