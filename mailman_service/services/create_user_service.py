from mailman_service.models import MailmanUser, ApiKey
from rest_framework.response import Response
from rest_framework import status

class CreateUserService:
    
    def __init__(self):
       pass
    
    def create_user(self, email):
        response = {
            "messsage" : "Something went wrong.",
            "status" : status.HTTP_500_INTERNAL_SERVER_ERROR
        }
        # validate email by sending a otp
        self.validate_email()
        # generate api key
        try:
            # Check if user exists
            if MailmanUser.objects.get(email=email).DoesNotExist:
                user = MailmanUser.objects.get(email=email)
                api_key = ApiKey(user=user)
                api_key.generate_key()
                
                response['message'] = "Key generated successfully."
                response['api_key'] = api_key.key
                response['status'] = status.HTTP_200_OK
            else:
                response["messsage"] = "User already exists. User another email id."
                response['status'] = status.HTTP_400_BAD_REQUEST
            
        except Exception as e:
            raise e

        return Response(response)
    
    
    def validate_email():
        # send an email with a 6 digit otp
        pass