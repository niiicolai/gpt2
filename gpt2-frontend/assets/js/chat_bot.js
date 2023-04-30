const API_URL = "http://localhost:5000/generate";
const API_HEADERS = {
    "Content-Type": "application/json"
};

const API_OPTIONS = {
    method: "POST",
    headers: API_HEADERS
};

class ChatBot {
    constructor(callback) {
        this.callback = callback;
    }

    async prompt(input) {
        const response = await fetch(API_URL, {
            ...API_OPTIONS,
            body: JSON.stringify({
                input_text: input
            })
        });

        const data = await response.json();
        this.callback(data.generated_text);
    }
}


