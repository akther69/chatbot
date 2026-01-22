from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_bot_response

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        bot_reply = get_bot_response(user_message)
        return JsonResponse({"reply": bot_reply})

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


def chatbot_page(request):
    return render(request, "chat.html")