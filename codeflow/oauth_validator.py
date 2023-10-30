from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):

    def get_additional_claims(self, request):
        print('*' * 40)
        print('get_additional_claims')
        print('request: ', request)
        return {
            "org_id": 1234,
            'email': 'dario.chacon@thoropass.com',
        }
