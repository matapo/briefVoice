from django.http import JsonResponse, HttpResponse


def serve(request):
    response = {
        "yes" : "okk"
    }

    return HttpResponse('Works like a charm!')