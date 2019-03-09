from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def serve(request):
    response = {'fulfillmentText': "teext!!",}
    return JsonResponse(response,safe=False)