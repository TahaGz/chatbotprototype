from django.shortcuts import render
from django.http import JsonResponse

# Predefined questions, answers, and audio files
QUESTIONS_ANSWERS = {
    "متى و اين ولدت": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},
    "متى ولدت": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},
    "اين ولدت": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},
    "متى و اين ولد حنبعل": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},
    "متى ولد حنبعل": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},
    "اين ولد حنبعل": {"response": "Birth", "audio": "/static/chatbot/audio/birth.mp3"},



    "لماذا قررت محاربه روما": {"response": "Rome war", "audio": "/static/chatbot/audio/rome_war.mp3"},
    "اخبرني عن حرب روما": {"response": "Rome war", "audio": "/static/chatbot/audio/rome_war.mp3"},


    "ما هي اشهر معركه لك": {"response": "Best war", "audio": "/static/chatbot/audio/best_war.mp3"},
    "ما هي اشهر معركه لحنبعل": {"response": "Best war", "audio": "/static/chatbot/audio/best_war.mp3"},


    "كيف انتهت حياتك": {"response": "Death", "audio": "/static/chatbot/audio/death.mp3"},

    "مرحبا": {"response": "Hello", "audio": "/static/chatbot/audio/hello.mp3"},
    "اهلا": {"response": "Hello", "audio": "/static/chatbot/audio/hello.mp3"},

    "وداعا": {"response": "Bye", "audio": "/static/chatbot/audio/bye.mp3"},
    "الى القاء": {"response": "Bye", "audio": "/static/chatbot/audio/bye.mp3"},
}

def chatbot_view(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            user_input = data.get("user_input", "").strip().lower().replace(" ", "")  # Normalize input

            # Normalize keys in QUESTIONS_ANSWERS for comparison
            normalized_questions = {key.strip().lower().replace(" ", ""): value for key, value in QUESTIONS_ANSWERS.items()}

            # Fetch the response
            response_data = normalized_questions.get(
                user_input, 
                {"response": "error", "audio": "/static/chatbot/audio/error.mp3"}
            )
            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return render(request, "chatbot/index.html")