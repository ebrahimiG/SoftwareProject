# registration system : 
creating a register system with user history; <br><br>
-- to create an account system for the website: <br>
1 create login and register pages <br>
2 register and login page sending the user info with `<form>` and `{% csrf_token %}` to the backend.<br>
3 in the views.py : receive the info and process them<br>
4 make sure html is sync with backend<br>
5 to save user chat history, create a model to save data in the database and register the model to admin panel <br>
6 go to views.py, import the created model, and use it to save the chat and test it to see if the chat info is in the admin panel<br>
7 to show the chat history to user, use the chat info in the html file.<br>