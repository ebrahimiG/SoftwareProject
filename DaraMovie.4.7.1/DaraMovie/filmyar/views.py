from django.shortcuts import render, redirect
from django.http import JsonResponse
import ollama
# for creating user we need User:
from django.contrib.auth.models import User
# for login and logout
from django.contrib import auth 
# to show the chat history from db
from .models import Chat



# ask ollama
def ask_ollama(message):
    client = ollama.Client()
    model = 'filmiar' 
    prompt = message

    Response = client.generate(model=model, prompt=prompt)
    response = Response.response

    return response


# get message from js file
# give it to ollama and get the response
# send the response to js file to show
# show chat history using Chat model
def filmyar_view(request):
    # get the show chat history of the current user from db and put it in context: 
    if request.user.is_authenticated:
        chats = Chat.objects.filter(user = request.user)
    else:
        chats = Chat.objects.none()
    context = {'chats':chats}

    # getting the message from script_filmyar.js
    if request.method =="POST":
        message = request.POST.get('message')
    
        # sending message to ollama and take the response:
        response = ask_ollama(message)

        # storing chat history:
        # first value is from Chat model and second is from html file.
        chat = Chat(user = request.user, message = message, response = response)
        chat.save()

        # giving the response to the script_filmyar.js
        return JsonResponse({'response':response})
    
    # sending the chat history to html file
    return render (request,'filmyar/filmyar_chat.html',context)
    

    
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
                return redirect('home')
            # error handling and sending the error to html file: 
            except: 
                error_message = 'Error creating account!'
                return render(request,'filmyar/register.html',{'error_message':error_message})
        # if passwords didn't match: 
        else: 
            error_message = 'Passwords do not match! try again please'
            return render(request,'filmyar/register.html',{'error_message':error_message})

    return render(request,'filmyar/register.html')



#login
def login_view(request):
    if request.method == "POST":
        # gathering info: 
        username = request.POST['username']
        password = request.POST['password']

        # check if the user exists: if the info is valid, it will creat user object other wise it's None.
        user = auth.authenticate(request, username= username, password= password)
        # log in the user
        if user is not None: 
            auth.login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid User!'
            return render (request,'filmyar/login.html',{'error_message':error_message})

    return render(request,'filmyar/login.html')


# logout
def logout_view(request):
    auth.logout(request)
    return redirect('home')