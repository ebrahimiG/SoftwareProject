// this is the list where messages are shown on the screen
const messagesList = document.querySelector('.messages-list');
// submit button is in this form
const messageForm = document.querySelector('.message-form');
// user message can be extract from here.
const messageInput = document.querySelector('.message-input');

// what happen after click on the send button: 
messageForm.addEventListener('submit', (event) => {
    // we don't want the page to refresh
    event.preventDefault();
    // store the message that was inputed and ignore the empty input.
    const message = messageInput.value.trim();
    if (message.length === 0) {
      return;
    }
    // create a new list element because messages are showned by list <i> on the screen.
    const messageItem = document.createElement('li');
    messageItem.classList.add('message', 'sent');
    messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
                <b>You</b>
            </div>
            <div class="message-content">
                ${message}
            </div>
        </div>`;
    // after creating the list item it's time to append it 
    messagesList.appendChild(messageItem);
    // clearing the input after clicking on send button
    messageInput.value = '';

    // sending the message to backend (views.py). fetch('') means path('') in urls.py
    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'message': message
      })
    })
    // get the response from views.py and convert to json.
    .then(response => response.json())
    .then(data => {
        const response = data.response;
        // createing a new list item and put the response in it.
        const messageItem = document.createElement('li');
        messageItem.classList.add('message', 'received');
        messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
              <b>AI Chatbot</b>
            </div>
            <div class="message-content">
                ${response}
            </div>
        </div>`;
        // append the list item to the list to show on the screen
        messagesList.appendChild(messageItem);
    });
});