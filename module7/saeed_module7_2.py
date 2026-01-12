import ollama
import time
import sys

# In the docker-compose setup, the Ollama service will be reachable at http://ollama:11434.
client = ollama.Client(host='http://ollama:11434')

def wait_for_ollama(timeout=120):
    """Waits for the Ollama service to be available."""
    print("Connecting to Ollama...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Check if the service is up by listing models
            client.list()
            print("Ollama service is available.")
            return True
        except Exception:
            print("Waiting for Ollama service to start...")
            time.sleep(5)
    print("Timed out waiting for Ollama service.", file=sys.stderr)
    return False

def get_ollama_response():
    """Gets a response from the Ollama model."""
    try:
        user_prompt = "Why is the sky blue?"
        print(f"Sending prompt to Ollama: '{user_prompt}'")

        response = client.chat(
            model='gemma:2b',
            messages=[{'role': 'user', 'content': user_prompt}],
        )
        
        print("\n--- Ollama Response ---")
        print(response['message']['content'])
        print("-----------------------")

    except Exception as e:
        print(f"An error occurred while communicating with Ollama: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if wait_for_ollama():
        get_ollama_response()
    else:
        sys.exit(1)
