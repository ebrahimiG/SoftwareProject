from django.shortcuts import render
import ollama

# Create your views here.


def chatbot_view(request):

    # initialize the Ollama client
    client = ollama.Client()

    # define the model and the input prompt
    model = "mistral"
    prompt = "what is python"

    # send the query to the model
    response = client.generate(model=model, prompt=prompt)

    # print the response from the model
    print("Response from Ollama: ")
    r = response.response
    context = {'response': r}

    return render(request, 'chatbot_app/index.html', context)
