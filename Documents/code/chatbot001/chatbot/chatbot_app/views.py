from django.shortcuts import render, redirect
from django.http import JsonResponse
import ollama
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

# if you get this error : ollama._types.ResponseError (status code: 503) , make sure to turn off the proxy


def ask_ollama(message):
    # initialize the Ollama client
    client = ollama.Client()

    # define the model and the input prompt
    model = "mistral"
    prompt = message

    # send the query to the model and getting the response
    Response = client.generate(model=model, prompt=prompt)

    # storing the response
    response = Response.response

    # returning response
    return response

# 1️⃣ getting the message from js file.
# 2️⃣ give the message to ollama and take the response form it.
# 3️⃣ send the response to js file.


def chatbot_view(request):
    if request.method == "POST":
        # 1️⃣ storing the message that comes from js file:
        message = request.POST.get('Message')

        # 2️⃣ send message and getting the response:
        response = ask_ollama(message)

        # 3️⃣ send response to js file:
        return JsonResponse({'response': response})

    return render(request, 'chatbot_app/chatbot.html')


def register_view(request):
    if request.method == "POST":
        # receiving info form html --> the 'name' value in the tag
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # checking if the passwords match :
        if password1 == password2:
            try:
                # creating user:
                user = User.objects.create_user(username, email, password1)
                user.save()
                # login the created user:
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account!'
                return render(request, 'chatbot_app/register.html', {'error_message': error_message})
        else:
            error_message = 'paswords do not match!'
            # sending error_message to html file using dictionary
            return render(request, 'chatbot_app/register.html', {'error_message': error_message})

    return render(request, 'chatbot_app/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # checking if the user actually exists:
        user = auth.authenticate(request, username=username, password=password)

        # if user exists: 
        if user is not None: 
            # log in the user; 
            auth.login(request,user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid user!'
            return render(request,'chatbot_app/login.html',{'error_message':error_message})


    return render(request, 'chatbot_app/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('login')
