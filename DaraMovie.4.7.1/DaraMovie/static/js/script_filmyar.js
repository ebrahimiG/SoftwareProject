// this is the chat box where messages are shown on the screen
const chatBox = document.querySelector('.chat-box');
// submit button is in this form
const messageForm = document.querySelector('.message-form');
// user message can be extract from here.
const messageInput = document.querySelector('.user-input');


// what happen after click on the send button: 
messageForm.addEventListener('submit', (event) => {
    // we don't want the page to refresh
    event.preventDefault();
    // store the message that was inputed and ignore the empty input.
    const message = messageInput.value.trim();
    if (message.length === 0) {
      return;
    }
    // create a new div element because messages are showned by <div> on the screen.
    const messageItem = document.createElement('div');
    messageItem.classList.add('message', 'user-message');
    messageItem.innerHTML = `
        <div class="message-header"><strong>--You--</strong></div>
        <div class="message-content">${message}</div>`;
    // after creating the div item it's time to append it to the screen.
    chatBox.appendChild(messageItem);
    // scroll to the last message
    chatBox.scrollTop = chatBox.scrollHeight
    // clearing the input after clicking on send button
    messageInput.value = '';

    // Show "AI is typing..." placeholder
    const typingItem = document.createElement('div');
    typingItem.classList.add('message', 'bot-message');
    typingItem.setAttribute('id', 'typing-indicator');
    typingItem.innerHTML = `
        <div class="message-header"><strong>--Filmyar--</strong></div>
        <div class="message-content ai-typing">Filmyar is typing<span class="dots"></span></div>`;
    chatBox.appendChild(typingItem);
    chatBox.scrollTop = chatBox.scrollHeight;

    // sending the message to backend (views.py). fetch('') means path('') in urls.py
    // try filmyar in fetch
    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'message': message
      })
    })

    // get the response from views.py and convert to json. .then needs to after fetch ??
    .then(response => response.json())
    .then(data => {
        const response = data.response;
        // Remove the typing indicator
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
        chatBox.removeChild(typingIndicator);
        }

        // createing a new div item and put the response in it.
        const messageItem = document.createElement('div');
        messageItem.classList.add('message', 'bot-message');
        messageItem.innerHTML = `
        <div class="message-header"><strong>--Filmyar--</strong></div>
        <div class="message-content">${response}</div>`;
        // append the div item to the chat box to show on the screen
        chatBox.appendChild(messageItem);
        // scroll to the last message
        chatBox.scrollTop = chatBox.scrollHeight
    });
});