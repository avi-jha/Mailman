from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from mailman_service.services.email_service import EmailService


class CreateUserView(APIView):
    renderer_classes = [JSONRenderer]
    
    def post(self, request):
        data = request.data
        
        email = data.get("email")
        pass

class EmailView(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        data = request.data
        return Response({"message": "Email API endpoint ready"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        # import ipdb; ipdb.set_trace()
        data = request.data
        to_email = data.get('to_email')
        from_email = data.get('from_email')
        subject = data.get('subject')
        body = data.get('body')
        
        try:
            email_service = EmailService()
            email_service.send_email(
                to_email=to_email, from_email=from_email, subject=subject, body=body)
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
