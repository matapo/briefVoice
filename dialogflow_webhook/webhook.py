from django.http import JsonResponse, HttpResponse


def serve(request):
    response = {
  "conversationToken": "[]",
  "expectUserResponse": True,
  "expectedInputs": [
    {
      "inputPrompt": {
        "richInitialPrompt": {
          "items": [
            {
              "simpleResponse": {
                "textToSpeech": "Hey! this is BriefVoice2"
              }
            }
          ]
        }
      },
      "possibleIntents": [
        {
          "intent": "assistant.intent.action.TEXT"
        }
      ],
      "speechBiasingHints": [
        "$try_entity"
      ]
    }
  ],
  "responseMetadata": {
    "status": {
      "message": "Success (200)"
    },
    "queryMatchInfo": {
      "queryMatched": True,
      "intent": "360ea1a4-a467-4508-ad52-29196aef4ea8"
    }
  }
}
    return JsonResponse(response,safe=False)