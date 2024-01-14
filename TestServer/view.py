from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

@api_view()
@permission_classes([AllowAny])
def api_test(request):
    return JsonResponse({"result":request.query_params['id']})