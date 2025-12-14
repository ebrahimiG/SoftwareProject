# use without proxy or vpn!
import ollama
import requests

# Check if Ollama server is running
try:
    requests.get("http://localhost:11434")
except requests.exceptions.ConnectionError:
    print("Ollama server is not running. Start it with 'ollama run mistral'")
    exit()

client = ollama.Client()
response = client.generate(model="mistral", prompt="What is Python?")
print("Response from Ollama:")
print(response.response)