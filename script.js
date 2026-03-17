const chatbox = document.getElementById("chatbox");
const input = document.getElementById("message");

// First bot message
window.onload = function() {
    addMessage("Bot", "Hi, how can I help you!");
};

// Send message on Enter key
input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage(){

    let message = input.value.trim();
    if(message === "") return;

    addMessage("You", message);

    input.value = "";

    let response = await fetch(`/chat?message=${encodeURIComponent(message)}`);
    let data = await response.json();

    // Delay for typing effect
    setTimeout(() => {
        addMessage("Bot", data.response);
    }, 500);
}


// Function to add message with animation
function addMessage(sender, text){

    let messageDiv = document.createElement("div");

    if(sender === "You"){
        messageDiv.className = "message user";
    } else {
        messageDiv.className = "message bot";
    }

    messageDiv.innerHTML = text;

    chatbox.appendChild(messageDiv);

    chatbox.scrollTop = chatbox.scrollHeight;
}