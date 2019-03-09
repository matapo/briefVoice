from django.http import JsonResponse, HttpResponse


def serve(request):
    response = {
  "payload": {
    "google": {
      "expectUserResponse": True,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "I can send you alerts. Would you like that?"
            }
          }
        ],
        "suggestions": [
          {
            "title": "Alert me of new tips"
          }
        ]
      }
    }
  }
}

    return JsonResponse(response,safe=False)