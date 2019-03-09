from django.http import JsonResponse, HttpResponse


def serve(request):
    response = {'fulfillmentText': "teext!!"}
    return JsonResponse(response,safe=False)