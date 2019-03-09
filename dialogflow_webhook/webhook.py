from django.http import JsonResponse, HttpResponse


def serve(request):


    return JsonResponse({'fulfillmentText': 'my answer!'},safe=False)