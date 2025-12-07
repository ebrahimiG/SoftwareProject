from django.shortcuts import render
from django.http import JsonResponse
import ollama

# get message from js file
# give it to ollama and get the response
# send the response to js file to show
def filmyar_view(request):
    # getting the message from script_filmyar.js
    if request.method =="POST":
        message = request.POST.get('message')
    
        # ollama:
        client = ollama.Client()
        model = 'mistral'
        prompt = message
        Response = client.generate(model=model,prompt=prompt)
        response = Response.response

        # giving the response to the script_filmyar.js
        return JsonResponse({'response':response})

    return render (request,'filmyar/filmyar_chat.html')
    