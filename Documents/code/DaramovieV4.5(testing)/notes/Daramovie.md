# Daramovie 
## 📝 Descroption
This is a website for movie reviews and suggestions.
It will also use an AI(filmyar) to recommend movies and series to the users.
Users can have profile in the website.

## starting 
I use font __Cinzel__ for logo and __Raleway__ for the rest of the site(from google fonts) <br>
and I use __font awesome__ for icons.
And Then I make the project folder like this:
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


/* underline for the links */
a{
  position: relative;
}
a::after{
  content: "";
  position: absolute;
  right: 0;
  bottom: 0;
  height: 1px;
  width: 100%;
  background-color: var(--yellow-color);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s ease;
}
a:hover::after{
 /* the width of the underline blew the navbar links (it can be 1.5 and 2) */
  transform: scaleX(1); 
}
```
So instead of defining the underline for every link, all links will have the under line as default. and if a link should't have an underline (like the logo), we can define it for that link by `.ExmapleLinkClass:hover::after{transform: scaleX(0);}` 
## style.css
Here is the main css file.

### -- NAVBAR --
I style the navbar like this :
all the links have underline as default. It is defined in [basics](#basicscss). but we dont want our logo have underline when it's hoverd so we do this : `.logo:hover::after{transform: scaleX(0);}`
```
/* navbar */
.logo{
    font-family: "Cinzel Decorative", serif;
}
.logo:hover::after{
    transform: scaleX(0);
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
If we want to change the position of the `<div class="child">` based on the `<div class="parent";>`, here how we do it : <br>
First the `<div class="parent";>` must have `position: relative;` and `<div class="child">` must have `position: absolute;`.<br>
Then we can use top, bottom, and ... for the `<div class="child">` and it will change it's position based on the `<div class="parent";>`. If the `<div class="parent";>` does't have `position: relative;` the `<div class="child">` will change position based on the screen. <br>

`z-index` helps us to defined which element be on top of the other elements.

---
We need a navbar with sub menu. Like when we hover on category, we want it shows the sub menu of category. <br>
Here is a simple way of making a sub menu : <br>
html : 
```
<!-- navbar with sub menu -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>navbar with sub menu</title>
    <!-- CSS here -->
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- navbar -->
    <div class="navbar">
        <div class="container flex">
            <h1>TheLogo</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>

                    <li class="cat"><a href="#">Categories</a>
                        <div class="dropdown-cat">
                            <ul>
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Romance</a></li>
                                <li><a href="#">History</a></li>
                                <li><a href="#">Sci-Fi</a></li>
                                <li><a href="#">More</a></li>
                            </ul>
                        </div>
                    </li>

                    <li><a href="#">Docs</a></li>
                </ul>
            </nav>
        </div>
    </div>  
</body>
</html>
```
So it's just like before (almost). We go on the `<li>` that we want to give it the sub menu. In this case it's __Categories__. <br>
We give the `<li>` of __Categories__, class="cat" so we can use it in the css.
Then after `</a>` and before the `</li>`, we make `<div class="dropdown-cat">`. and inside it we have another `<ul>` with its `<li>`s. <br>
now it's time for the css : 
```
/* Reset */
*{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* basics */
ul{
    list-style-type: none;
}
a{
    text-decoration: none;
    color: black;
}

/* Utilities */
.container{
    max-width: 1100px;
    margin: 0 auto;
    height: 100%;
    padding: 0 5px;
}
.flex{
    display: flex;
    justify-content: center;
    align-items: center;
}

/* navbar */
.navbar{
    height: 70px;
    background-color: rgb(227, 239, 250);
}
.navbar .flex{
    justify-content: space-between;
}
.navbar ul{
    display: flex;
}
.navbar a{
    padding: 5px 5px;
    margin: 0 5px;
}
.navbar a:hover{
    border-bottom: 1px solid black;
}

/*******************************************/
/* Sub Menu For The Category */
.cat{
    position: relative;
}
.dropdown-cat{
    display: none;
}
.cat:hover .dropdown-cat{
    display: block;
    position: absolute;
    top: 100%;
    left: 0;
    margin-top: 5px;
    background-color: rgb(227, 239, 250);
}
.dropdown-cat ul{
    display: block;
}
.dropdown-cat li{
    padding: 10px 0;
}
/*******************************************/
```
So first of all, we make the `.cat{position: relative;}` because we want to use __position absolute__ for the __dropdown-cat__. <br>
Then we make the `dropdown-cat{display: none;}`, so it will hide the __dropdown-cat__ when the __Categories__ not hovered.<br>
Then we start to define the __dropdown-cat__ when the __Categories__ or `.cat` is hovered. First `display: block`, so it make the __dropdown-cat__ visible. Then we use `position: absolute;` so we change the position of the __dropdown-cat__ based on the __cat__ (cat was `position: relative;`). <br>
`top: 100%;` will position the __dropdown-cat__ under the `.cat` and `left: 0;` so it starts from the leftside. And we give it the background-color same as the navbar backgorund. <br>
`.dropdown-cat ul{display: block;}` is because we want the list items to be in a column not in a row. And give some space to the list items using `.dropdown-cat li{padding: 10px 0}`. <br>
But in the __Daramovie__ we want the under line to have a animation so instead of `border-bottom` we use `::after`. : 
> ⚠️ sinces we define the underline for all of the links in basics, we don't need this code, but i don't remove it for it's explanation.
```
nav a {
  position: relative;
}
nav a::after {
  content: "";
  position: absolute;
  right: 0;
  bottom: 0;
  height: 1px;
  width: 100%;
  background-color: var(--yellow-color);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s ease;
}
nav a:hover::after {
  /* the width of the underline blew the navbar links (it can be 1.5 and 2) */
  transform: scaleX(1); 
}
```
First we give the all the links in the `<nav>` __position relative__ because we want to use __position absolute__ in the `::after`. <br>
When we use `::after` or `::before`, we need __content__. In this case __content__ should be empty because we want just a simple line not any text. <br>
Then we use __position absolute__. using `bottom: 0;` so the line place under the link. <br>
We can think of it like we making a div below the link but we want it to look like a line so we give it `height: 1px;` like we defining the thickness of the line. Then `background-color` like we defining the color of the line. <br>
`transform; scaleX(0)` : this is the width of the line. 0 means no width. This is exactly what we want when the link is not hovered. `scaleX` means width through the horizontal direction and `scaleY` is about vertical direction.  <br>
`transform-origin: center;` : means where we want the line start showing up. it can be from __left__ or __right__ too. <br>
`transition: transform 0.3s ease;` : means how long it will take for the `transform` to show its animation. <br>
And then when we hover : <br>
We want to line grow from 0 width to 1 width (100% of the links width). we use `transform scaleX(1)`.

### -- SHOWCASE --
Now we want to build the showcase.













