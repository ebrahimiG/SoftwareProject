const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");


function addMessage(message, classNme) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", classNme);
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.onclick = async () => {
    const message = userInput.value.trim();
    if (message === "") return;
    addMessage(message, "user-message");
}