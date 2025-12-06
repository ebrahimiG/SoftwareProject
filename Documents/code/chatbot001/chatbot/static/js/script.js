const messagesList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');

// when submit button is clicked, we want to do some stuff
messageForm.addEventListener('submit', (event) => {
  // don't refresh the page
  event.preventDefault();

  // store message that inputed 
  const message = messageInput.value.trim();
  // don't return anything if the message is empty
  if (message.length === 0) {
    return;
  }

  // creating a list item to show the users message on the screen
  const messageItem = document.createElement('li');
  // add this classes to the <li> tag --> message and sent
  messageItem.classList.add('message', 'sent');
  // what is in the <li> tag
  messageItem.innerHTML = `
      <div class="message-text">
          <div class="message-sender">
              <b>You</b>
          </div>
          <div class="message-content">
              ${message}
          </div>
      </div>`;
  // add the created <li> to the screen list
  messagesList.appendChild(messageItem);
  // clear the message input box after sending message
  messageInput.value = '';

  // using fetch to send the message to the backend.
  // fetch('') means urls.py --> urlpattern[path('',views.chatbot_view,name='chatbot'),]
  // and using urls.py, we can access to the views.py to get a response from AI and send it to js file
  fetch('', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
      'Message': message
    })
  })
    // getting the response from backend: 
    .then(response => response.json())
    .then(data => {
      const response = data.response;
      // creating a list item to show the response just like users message
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
      </div>
        `;
      messagesList.appendChild(messageItem);
    });
});
