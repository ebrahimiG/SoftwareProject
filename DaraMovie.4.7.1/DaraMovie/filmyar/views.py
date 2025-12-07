from django.shortcuts import render
from django.http import JsonResponse
import ollama

# get message from js file
# give it to ollama and get the response
# send the response to js file to show

# ask ollama
def ask_ollama(message):
    client = ollama.Client()
    model = 'mistral' 
    prompt = message

    Response = client.generate(model=model, prompt=prompt)
    response = Response.response

    return response



# filmyar and show chat and chat history
def filmyar_view(request):
    # getting the message from script_filmyar.js
    if request.method =="POST":
        message = request.POST.get('message')
    
        # sending message to ollama and take the response:
        response = ask_ollama(message)

        # giving the response to the script_filmyar.js
        return JsonResponse({'response':response})

    return render (request,'filmyar/filmyar_chat.html')
    