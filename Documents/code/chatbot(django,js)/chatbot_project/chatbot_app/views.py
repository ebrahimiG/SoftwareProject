from django.shortcuts import render
from django.http import JsonResponse
import ollama

# Create your views here.


def chatbot(request):
    if request.method == "POST":
        # getting the message from js (fetch in js file)
        message = request.POST.get('message')

        # ollama here: 
        client = ollama.Client()
        model = 'mistral'
        prompt = message
        Response = client.generate(model=model,prompt=prompt)

        response = Response.response
        # convert response to json format and sending it to js
        return JsonResponse({'response': response})

    return render(request, 'chatbot_app/chatbot.html')
