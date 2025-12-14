import ollama

# initialize the Ollama client
client = ollama.Client()

# define the model and the input prompt
model = "mistral"
prompt = "what is python"

# send the query to the model
response = client.generate(model=model, prompt=prompt)

# print the response from the model
print("Response from Ollama: ")
print(response.response)
