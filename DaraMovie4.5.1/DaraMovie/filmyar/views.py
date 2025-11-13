from django.shortcuts import render
import ollama


def filmyar_view(request):
    # get chat history from session
    messages = request.session.get("messages", [])

    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        if user_message:
            # add user message
            messages.append({"role": "user", "text": user_message})

            # call Ollama
            client = ollama.Client()
            response = client.generate(model="mistral", prompt=user_message)
            ai_reply = response.response

            # add AI reply
            messages.append({"role": "bot", "text": ai_reply})

            # persist history
            request.session["messages"] = messages

    return render(request, "filmyar/filmyar_chat.html", {"messages": messages})

