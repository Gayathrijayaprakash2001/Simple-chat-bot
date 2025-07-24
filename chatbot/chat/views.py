from django.shortcuts import render
from django.shortcuts import render
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def chatbot(request):
    response_text = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = model.generate_content(user_input)
        response_text = response.text

    return render(request, "chat/chatbot.html", {"response": response_text})
