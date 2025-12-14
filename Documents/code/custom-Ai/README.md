# How to customize a model : 
In the __Modelfile__ we have : 
```
FROM mistral

PARAMETER temperature 1

SYSTEM """
You are Mario from super mario bros, answer as mario, the assistant, only.
"""
```
`FROM {the model you've already installed}` <br>
`PARAMETER  temperature 1 ` higher the temprature higher the creativity <br>
`SYSTEM """ your message to the system """ ` this is what you want to customze about the model. <br> 

> make sure the the file name is Modefile with no .txt or .py
open the terminal in the Modelfile location using `cd` and then `ollama create mario -f ./modelfile`. instead of mario you can name it whatever you want. after you get __success__ , you can now run the model by `ollama run mario` in the terminal