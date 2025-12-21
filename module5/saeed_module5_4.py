import requests

def ask_ollama_with_persona():
    # system prompt (persona)
    system_prompt = (
        "You are a friendly Python teacher. "
        "Explain answers in simple words. "
        "Use short examples."
    )

    # get user input
    user_input = input("Ask a question: ")

    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"

    # request data
    data = {
        "model": "llama3",
        "prompt": f"SYSTEM: {system_prompt}\nUSER: {user_input}",
        "stream": False
    }

    # send request
    response = requests.post(url, json=data)

    # get result
    result = response.json()

    # print answer
    print("\nLLM Answer:")
    print(result["response"])


# run the function
ask_ollama_with_persona()
