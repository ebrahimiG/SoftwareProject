# Daramovie 
## 📝 Descroption
This is a website for movie reviews and suggestions.
It will also use an AI(filmyar) to recommend movies and series to the users.
Users can have profile in the website.

## starting 
I use font __Cinzel__ for logo and __Raleway__ for the rest of the site(from google fonts) <br>
and I use __font awesome__ for icons.
And than I make the project folder like this:
* 📁 Daramovie
    * index.html
    * about_us.html
    * advanced_search.html
    * blog_list.html
    * blog.html
    * filmyar.html
    * movie.html
    * others_profile.html
    * personal_profile.html
    * sign_up.html

    * 📁 css
        * basics.css
        * style.css
        * utilities.css
    * 📁 notes
        * Daramovie.md
    * 📁 img
    
## index.html
I started the file with links to __css__ and __font awesome__ in the `<head>` : 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- css -->
    <link rel="stylesheet" href="css/basics.css">
    <link rel="stylesheet" href="css/utilities.css">
    <link rel="stylesheet" href="css/style.css">

    <!-- font awesome for icons -->
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

     <title>Daramovie</title>
</head>
    
<body>

      
</body>
</html>
```
### -- NAVBAR --
First of all let's make the navbar. this navbar contains __logo__, __category__, __search__ and __sign up__. <br>
I don't want the __logo__ go to far to the left. I want it more in center so this is how I do it. <br>
I have `<div class="navbar">` and inside it I have a `<div class="container flex">`. <br>
_container flex_ are two [utility classes](utilities.md) that defined in _utilities.css_. _contaier_ help that the element of it be in the center of the page and _flex_ helps with the order of those elements.
```
<!-- navbar -->
    <div class="navbar">
        <div class="container flex">
            <a href="index.html"><h1 class="logo"><span>D</span>aramovie</h1></a>
            <nav>
                <ul>
                    <li><a href="#">category</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="#">filmyar</a></li>
                </ul>
            </nav>
        </div>
    </div>  
```
## basics.css
Before I go any further, I want to work on __basics.html__. <br>
This file contains basics settings for the project. We put a default value for the elements like `<a>`, `<ul>`, `<h1>`, `<img>` and...
```
/* font Cinzel for logo and Raleway for the rest of the site */
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap');

/* colors */
:root{
    --yellow-color:#DDDD10;
    --white-color:#eae4e4;
}

/* Reset */
*{
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}

body{
    background-color: #1b1a1a;
    color:var(--white-color);
    font-family: "Raleway", sans-serif;
}

img{
    width: 100%;
    height: 100%;
}
h1, h2{
    font-weight: 200;
}

a{
    text-decoration: none;
    color:var(--white-color);
}
ul{
    list-style-type: none;
}
```
## style.css
Here is the main css file.

### -- NAVBAR --
I style the navbar like this :
```
/* navbar */
.logo{
    font-family: "Cinzel Decorative", serif;
}
.logo span{
    color:var(--yellow-color);
}

.navbar{
    height: 70px;
}
.navbar ul{
    display: flex;
}
.navbar a{
    padding: 10px;
    margin: 0 5px;
}
.navbar .flex{
    justify-content: space-between;
}
.nav a:hover{
    border-bottom: solid 1px #eae4e4;
}
```
I want Category to be a drop down menu : <br>
__(Positions)__ <br>
There is five position in css : static | relative | absolute | fixed | sticky. <br>
static is the default value.
With relative, absolute, fixed, sticky we can use the properties like : <br>
top<br>
bottom<br>
left<br>
right<br>
z-index<br>
When we use `position: relative;` it means the position of the element will change based on if it was static. <br>
Here is the example: top means how much element push further away from top and so on... .
In this example this red will go down 100px and go to the right 20px __from where it was before.__
```
.element1{
    background-color: red;
    height: 300px;
    width: 300px;
    font-size: 45px;
    padding: 10px;
    position: relative;
    top: 100px;
    left: 20px;
}
```
`position: fixed;` means the element will be fixed on the screen and when user scrolls, it will follow the user.<br>
It can be used when we need a navbar that will follow the user when they scroll down.<br> The properties (top, left,...) will work and change the position of the element __based on the screen it self__. <br> 
So when we put the `top: 10px;`, it wont go down just 10px (just like relative) but it will be 10px from the top of the screen. <br>
And when we put the `right: 0;`, the element will go to right of the screen with no space.

`position: sticky;` just like fixed, the element will follow the user but when it's about to go out of screen when user scrolls. We can define that when the element follow the user by (top).

`position: absolute;` we have two `<div>`s one is `<div class="parent";>` and inside of it we have `<div class="child">`. <br>
If we want to change the position of the `<div class="child">` based on the `<div class="parent";>`, here how we do it. <br>
First the `<div class="parent";>` must have `position: relative;` and `<div class="child">` must have `position: absolute;`.<br>
Than we can use top, bottom, and ... for the `<div class="child">` and it will change it's position based on the `<div class="parent";>`. If the `<div class="parent";>` does't have `position: relative;` the `<div class="child">` will change position based on the screen. <br>

`z-index` helps us to defined which element be on top of the other elements.











