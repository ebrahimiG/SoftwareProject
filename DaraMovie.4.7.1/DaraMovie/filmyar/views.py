from django.shortcuts import render, redirect
from django.http import JsonResponse
import ollama
# for creating user we need User:
from django.contrib.auth.models import User
from django.contrib import auth



# ask ollama
def ask_ollama(message):
    client = ollama.Client()
    model = 'mistral' 
    prompt = message

    Response = client.generate(model=model, prompt=prompt)
    response = Response.response

    return response


# get message from js file
# give it to ollama and get the response
# send the response to js file to show
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
    

    
# register
def register_view(request):
    if request.method == "POST":
        # gathering the info
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # check the passowrds: 
        if password1 == password2:
            try: 
                # creating and saving new user: 
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                # log in the created user: 
                auth.login(request,user)
                return redirect('filmyar')

    return render(request,'filmyar/register.html')



#login
def login_view(request):
    return render(request,'filmyar/login.html')