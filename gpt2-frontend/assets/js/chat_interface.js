
class ChatInterface {
    constructor(inputElement, outputElement) {
        this.inputElement = inputElement;
        this.outputElement = outputElement;
        console.log(outputElement);
    }

    appendInput(message, role) {
        const messageWrapper = document.createElement("div");
        const messageRole = document.createElement("div");
        const messageElement = document.createElement("div");

        messageWrapper.classList.add("message");
        messageWrapper.classList.add(role);

        messageRole.classList.add("message-role");
        messageElement.classList.add("message-text");

        messageRole.innerHTML = role;
        messageElement.innerText = message;

        messageWrapper.appendChild(messageRole);
        messageWrapper.appendChild(messageElement);
        this.outputElement.appendChild(messageWrapper);

        // Scroll to bottom
        window.scrollTo(0, document.body.scrollHeight);
    }

    clearInput() {
        this.inputElement.value = "";
    }

    getInput() {
        return this.inputElement.value;
    }

    setInput(value) {
        this.inputElement.value = value;
    }
}
