# Loruki index.html
## 📝Description
this project is about learning __how to make a responsive website__ using html,css.
this project is a practice for my main college project "Daramovie".
[this is the link of the video for Loruki project](https//something). in this file i explained the _index.html_, _features.html_, _docs.html_ and _style.css_. but this project includes other parts like utility classes, responsiveness and animation.

here is the link to other parts : 

[Utility classes](Utilities.md) <br>
[Responsiveness](Responsive.md) <br>
[Animation](Animation.md)



## starting 
like any other html project, first we need a project folder : 

* project loruki (folder)
    * index.html
    * features.html
    * docs.html
    * css (folder)
        * style.css
        * basics.css
        * utilities.css
    * images

than we need "font-awesome" for this project. it will help us with icons.
> font-awesome is not only a font, it will help us with icons too. Font Awesome is designed to be used with inline elements. The < i > and < span > elements are widely used for icons. Also note that if you change the font-size or color of the icon's container, the icon changes. Same things goes for shadow, and anything else that gets inherited using CSS. Font Awesome gives you scalable vector icons that can instantly be customized — size, color, drop shadow, and anything that can be done with the power of CSS.

for having font-awesome, we go to this website : [cdnjs.com](https://cdnjs.com/)
>cdnjs is a free and open-source CDN service. A CDN (Content Delivery Network) is essentially a network of servers distributed across the globe that helps deliver web content faster and more reliably.

then we search for fontawesome in the websit, searching for a link that contains everything--> (https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css) and than copy link tag (</>).

we paste the link tag in the `<head>` :

```
<!-- font-awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
```
also don't forget this one: order matters ( utilities.css above the style.css)
```
<link rel="stylesheet" href="css/utilities.css">
<link rel="stylesheet" href="css/basics.css">
<link rel="stylesheet" href="css/style.css">
```
## html (Navbar)
we are going to start with navbar.
navbar contains _logo_ and _navigation_.
We don't want the logo to lean too far to the right, so we make another `<div>` __inside__ the navbar (container) so we can control the second div for placing the logo and navigation.
```
.navbar         .container
-------------------------------------------------------------------------
|           |                                               |           |
|           |                                               |           |
|           |  logo                             navigation  |           |
|           |                                               |           |
|           |                                               |           |
-------------------------------------------------------------------------
```

so here is the code so far :
```
<body>

    <!-- NAVBAR -->
    <div class="navbar">
        <div class="container flex">
            <h1 class="logo">Loruki</h1>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="featurse.html">Featurse</a></li>
                    <li><a href="docs.html">Docs</a></li>
                </ul>
            </nav>
        </div>
    </div>
    
</body>
```
## css (basics)
* this is in the __basics.css__ file :

first of all, we need a __font__. we go to google fonts and search for __Lato__. select it and copy the __import__ (to use in css file).
```
/* using font Lato */
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');
```
to define a __variables__ in css we do this : here we define colors to use all around the website.
```
:root{
    --primary-color:# 047aed;
    --secondary-color: #1c3fa8;
    --dark-color: #002240;
    --light-color: #f4f4f4;
    --success-color:#5cb85c;
    --error-color:#d9534f;
}
```
and this is how we use it : `background-color: var(--primary-color);`.


than we go for __reset__. it allows us to add padding and... without add to width it's better be in every project :
```
/* reset */
*{
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}
```
here is the __body__ :
line-height spread things out a little bit.
```
body{
    font-family: 'Lato',sans-serif;
    line-height: 1.6;
    color: #333;
}
```
__ul__ : list-style-type to make sure we don't have any bullet points.
```
ul{
    list-style-type: none;
}
```
__a__ : get rid of the underline.
```
a{
    text-decoration: none;
    color: #333;
}
```
__h1,h2__ : margin top&bottom 10px and left&right 0px.
```
h1,h2{
    /* make the font little less bold */
    font-weight: 300;
    margin: 10px 0;
    line-height: 1.2;
}
```
__p__ :
```
p{
    margin: 10px 0;
}
```
__img__ : keeps the image in its container.
```
img{
    width: 100%;
}

```


## css (navbar)
here is settings for the navbar.
first of all the __navbar__ : we use the variable that we defined for the background color :
```
/* NAVBAR */
.navbar{
    background-color: var(--primary-color); 
    color: #fff;
    height: 70px;
}
```
__navbar flex__ : we want to use the flex class in other places ([flex is a utility class](Utilities.md)) but in navbar we want the _justify-content_ to be _space between_ in navbar so this is the code : 
```
.navbar .flex{
    justify-content: space-between;
}
```
__navbar ul__ : makes the list item to be in a row.
```
.navbar ul{
    display: flex;
}
```
__navbar a__ : give them color and space between them.
```
.navbar a{
    color: #fff;
    margin: 0 5px;
    padding: 10px;
}
```
__navbar a:hover__ : give it a under line when hover.
```
.navbar a:hover{
    border-bottom: 2px #fff solid;
}
```
## html (Showcase)
This section includes two parts : _text_ and _form_.

for making Showcase, we use `<section>` tag. `<section>` is semantic, meaning it tells browsers and assistive tech that the content inside is thematically related. It’s ideal for content that could appear in a table of contents or outline.
this tag should typically include a headin (h1-h6) to define its topic. Without one, it loses its semantic punch.

inside the `<section>`, we use ([container grid](Utilities.md)) class. this will allow us to use the _container_ class that we defined before. inside this class is __text__ (showcase-text class includes h1 and p and a) and __from__ (showcase-form card class includes h2 and form). inside the < form> we have three div (that each div includes input) and an input with submit type. 

this is the code : 
```
<!-- SHOWCASE -->
    <section class="showcase">
        <div class="container grid"> <!-- to put the content in center just like navbar -->

            <!-- Text here -->
            <div class="showcase-text"> 
                <h1>Easeier Deployment</h1>
                <p>
                Deploy web apps of all kinds, from large scale enterprise APIs to static websites for individuals. Fill out the from to try demo of our platform.
                </p>
                <a href="features.html" class="btn btn-outline">Read More</a>
            </div>

            <!-- From here -->
            <div class="showcase-form card"> 
                <h2>Request Demo</h2>
                <form>
                    <div class="form-control">
                        <input type="text" name="name" placeholder="Name" required>
                    <div class="form-control">
                        <input type="text" name="company" placeholder="Company Name" required>
                    <div class="form-control">
                        <input type="text" name="email" placeholder="Email" required>
                    </div>
                    <input type="submit" value="send" class="btn btn-primary">
                </form>
            </div>
        </div>
    </section>
```
## css (showcase)
__showcase__ : position(relative) so that if we need to position anything absolute within it we can.
```
/* Showcase */
.showcase{
    background-color: var(--primary-color);
    height: 400px;
    color: #fff;
    position: relative; 
}
```
__showcase h1__ : makes the h1 bigger.
```
.showcase h1{
    font-size: 40px;
}
```
__showcase p__ : we need a little bit more space in pragraph in the show case.
```
.showcase p{
    margin: 20px 0;
}
```
__showcase grid__ : to use grid in showcase and change it a little bit. grid-template-columns: 55% 45%; means 55% for the text part (showcase-text class) and 45% for the form part (showcase-form class).<br> overflow (visible) is because the form in the showcase is overflowing (height 350 in showcase-form class). 
```
.showcase .grid{
    grid-template-columns: 55% 45%;
    gap: 30px;
    overflow: visible;
}
```
__showcase-text__:
we add some [animation](Animation.md):
```
.showcase-text{
    animation: slideInFromLeft 1s ease-in;
}
```
__showcase-form__ :styling the form inside the card. position(relative) and top(60) is for to push it down a little bit. and height(350px) makes the for overflowing so to fix it we go to showcase grid and make the overflow(visible). z-index is for to make sure the form is always in front and justify-self(flex-end) to push the from to the right. and we add some animation.
```
.showcase-form{
    position: relative;
    top: 60px;
    height: 350px;
    z-index: 100;
    justify-self: flex-end;
    animation:slideInFromRight 1s ease-in ;
}
```
__showcase-form form-control__ : to separete those inputs a little bit more.
```
.showcase-form .form-control{
    margin: 30px 0;
}
```
__showcase-form input[type='text'] and [type='email']__ : because the submit button is also an input but we don's want to style it with other inputs we do this:
```
.showcase-form input[type='text'],
.showcase-form input[type='email']{
    border: 0;
    border-bottom: 1px #b4becd solid;
    
    /* makes them go all the way across the from box */
    width: 100%;
    padding: 3px;
    font-size: 16px;
}
```
__showcase-form input:focus__ : we dont want that border around the input when we click on it so here is how we get rid of it: 
```
.showcase-form input:focus{
    outline: none;
}
```
for making a slant without adding a new html element, we're goning to use _pseudo selectors_. when we use _before_ and (or) _after_ we're have to have a content property and we can leave it blank but if you want text in it like 'hello' , it will show the text before and after the div.
*make sure the showcase has the position(relative).
when we make tha position(absolute) we have:

bottom(-70) to only have bottom and how far. more negetive more down.

left and right(0) to have no space from left and right (if we not defined them it wont show)

for making a slant we use transform(skewY(-3deg)) that makes the rectangel to rotate three degrees to the left. and then by making the background-color as the same as the body background-color, we finished making a slant.

making sure this will work in all browsers.(i don't know if this is necessary)

-webkit-transform: skewY(-3deg);

-moz-transform: skewY(-3deg);

-ms-transform: skewY(-3deg);
```
/* for making a slant */
.showcase::before,.showcase::after{
    content:'';
    position: absolute;
    background-color: #fff;
    height: 100px;
    /* to only have on the bottom and how far more negetive more down. */
    bottom: -70px;
    /* to have no space between left and right (if you don't define them it wont show) */
    left: 0px;
    right: 0px;
    /* slant */
    transform: skewY(-3deg);
    /* to make sure it's working in all browsers */
    -webkit-transform: skewY(-3deg);
    -moz-transform: skewY(-3deg);
    -ms-transform: skewY(-3deg);
}
```
## html (stats)
this is stats section. we have text and icons here. we have a section that includs container (everything be in center just like navbar and showcas) inside we have a h3 and a div. h3 has stats heading, text-center(utilty class) and my-1(utility class means margin top and bottom 1). than we have a div with grid, grid-3(a grid with 3 elements),text-center and my-4. 

inside this div we have three divs that contains icons(using font-awesome). font-awesome class(fas) - the icon(fa-server) - the size of it(fa-3x).

```
<!-- STATS -->
    <section class="stats">
        <div class="container">
            <h3 class="stats-heading text-center my-1"> 
            Welcome to the best platform for building applications of all types with modern architecture and scaling.
            </h3> 
            <div class="grid grid-3 text-center my-4"> 
                <div>
                    <i class="fas fa-server fa-3x"></i> 
                    <h3>10,349,405</h3>
                    <p class="text-secondary">Deployments</p>
                </div>
                <div>
                    <i class="fas fa-upload fa-3x"></i> 
                    <h3>987 TB</h3>
                    <p class="text-secondary">Published</p>
                </div>
                <div>
                    <i class="fas fa-project-diagram fa-3x"></i> 
                    <h3>2,343,365</h3>
                    <p class="text-secondary">Projects</p>
                </div>
            </div>
        </div>
    </section>
```
## css (stats)
in __stats__ we give it a padding-top(100px) so that the texts won't go under the showcase slant. give it a background-color to see it. and add some animation.
```
/* Stats */
.stats{
    padding-top: 100px;
    animation:slideInFromBottom 1s ease-in ;
}
```
__stats-heading__ : using max-width to make the sentence to be in two lines and margin(auto) to put text in the center.
```
.stats-heading{
    max-width: 500px;
    margin: auto;
}
```
__stats grid h3__ : targeting only numbers below the icons not the h3 text above them.
```
.stats .grid h3{
    font-size: 35px;
}
```
__stats grid p__ : targeting the paragraph below the h3 for icons.
```
.stats .grid p{
    font-size: 20px;
    font-weight: bold;
}
```

## html (cli)
in this section we have an image and two cards.this section have three columns and two rows. starting from left, we want the image take two of three colunms and two of two rows, and one card take a column on the right side of the image and the other card take place below the first card.

to do this we need grid. this is how we define it in html, the rest of it is for css.

we also use container class as usual. 
```
<!-- Cli -->
    <section class="cli">
        <div class="container grid">
            <img src="images/cli.png" alt="">
            <div class="card">
                <h3>Easy to use, cross platform CLI</h3>
            </div>
            <div class="card">
                <h3>Deploy in seconds</h3>
            </div>
        </div>
    </section>
```
## css (cli)
our grid class has two 1fr but we need more for this section. this is the structure we want to use : 
```
/* Cli */
.cli .grid{
    grid-template-columns: repeat(3,1fr);
    grid-template-rows: repeat(2,1fr);
}
```
but this is how we put our elements(image and two cards) in it:

anything that is the first child (in this case img).
this code says take the first child (the first element of the grid) and expand it from colunm 1 to 2 and from row 1 to 2.
```
.cli .grid > *:first-child{
    grid-column: 1 / span 2;
    grid-row: 1 /span 2;
}
```
we can also go like this: `.cli .grid img{...}`

* here is an example for how to create a table with grid and how to contorl elements in it (I used the utilities of this project)  : 

html:
```
    <div class="test" style="margin-top: 200px; background-color: bisque;">
        <div class="testing container grid">

            <div class="card">
                <h3>the first-child</h3>
            </div>

            <div class="card two">
                <h3>the second-child</h3>
            </div>

            <div class="card three">
                <h3>the third child</h3>
            </div>

            <div class="card four">
                <h3>the fourth child</h3>
            </div>

        </div>
    </div>
```
css:
```
/* making a 4 column and 3 row rect */
.test .grid{
    grid-template-columns: repeat(4,1fr);
    grid-template-rows: repeat(3,1fr);
}
/* controling elements */
/* from row number 1 expand to row number 2 */
.test .grid >*:first-child{
    grid-row: 1 /span 2;
}
.test .grid .two{
    grid-row: 2 /span 3;
}
.test .grid .three{
    grid-column: 3 / span 4;
}
.test .grid .four{
    grid-column: 3 /span 4;
    grid-row: 2/span 3;
}
```

## html (cloud)
this is the next section: we have a grid that includes two elements(text-center div that includes h2,p,a -- and an image)
```
    <!-- cloud -->
    <section class="cloud bg-primary my-2 py-2">
        <div class="container grid">
            <div class="text-center">
                <h2 class="lg">Extreme Cloud Hosting</h2>
                <p class="lead my-1">
                    Cloud hosting like you've never seen. Fast, efficient and scalabe
                </p>
                <a href="features.html" class="btn btn-dark">Read More</a>
            </div>
            <img src="images/cloud.png" alt="">
        </div>
    </section>
```
## css (cloud)
```
/* cloud */
/* first element take the 4fr and second take the 3fr */
.cloud .grid{
    grid-template-columns: 4fr 3fr;
}
```
## html (languages)
in this section we have an h2, and a contaier flex div that includs 8 card divs. each card div has an h4 and an img.
```
<!-- languages -->
    <section class="languages">
        <h2 class="md text-center my-2">
            Supported Languages
        </h2>
        <div class="container flex">
            <div class="card">
                <h4>Node.js</h4>
                <img src="images/logos/node.png" alt="">
            </div>
            <div class="card">
                <h4>Python</h4>
                <img src="images/logos/python.png" alt="">
            </div>
            <div class="card">
                <h4>Clojure</h4>
                <img src="images/logos/clojure.png" alt="">
            </div>
            <div class="card">
                <h4>Csharp</h4>
                <img src="images/logos/csharp.png" alt="">
            </div>
            <div class="card">
                <h4>Go</h4>
                <img src="images/logos/go.png" alt="">
            </div>
            <div class="card">
                <h4>php</h4>
                <img src="images/logos/php.png" alt="">
            </div>
            <div class="card">
                <h4>Ruby</h4>
                <img src="images/logos/ruby.png" alt="">
            </div>
            <div class="card">
                <h4>Scala</h4>
                <img src="images/logos/scala.png" alt="">
            </div>
        </div>
    </section>
```
## css (languages)
margin 1value: all around top&bottom&left&right

margin 2value: top&bottom then left&right

marigin 3value: top and left&right and bottom

margin 4value: top and right and bottom and left (clockwise)
```
/* languages */
.languages .card{
    text-align: center;
    margin: 18px 10px 40px;
    transition: transform 0.2s ease-in;
}
```
making the section a little bit respinsive, so when the screen gets smaller, the cards will go to the next line instead of getting smaller.
```
.languages .flex{
    flex-wrap: wrap;
}

```
each language's h4.
```
.languages .card h4{
    font-size: 20px;
    margin-bottom: 10px;
}
```
when hover makes the card rise up a little bit.
```
.languages .card:hover{
    transform: translateY(-15px);
}
```
## html (footer)
our footer includs three part : div(h1 and p),nav(ul),div(social). using bg-dark for background color , py-5 to make the footer a little bit biger form top and bottom. we also use container and grid and grid-3 (because we have 3 elements fot this grid). 
```
<!-- fotter -->
    <footer class="footer bg-dark py-5">
        <div class="container grid grid-3">
            <div>
                <h1>Loruki</h1>
                <p>Copyright &copy; 2020</p>
            </div>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="features.html">Featurse</a></li>
                    <li><a href="docs.html">Docs</a></li>
                </ul>
            </nav>
            <div class="social">
                <a href="#"><i class="fab fa-github fa-2x"></i></a>
                <a href="#"><i class="fab fa-facebook fa-2x"></i></a>
                <a href="#"><i class="fab fa-instagram fa-2x"></i></a>
                <a href="#"><i class="fab fa-twitter fa-2x"></i></a>
            </div>

        </div>

    </fotter>
```
## css (footer)
make the icons a have a little bit gab with each other:
```
.footer .social a{
    margin: 0 10px;   
}
```

# Loruki features.html
we only keep the navbar and footer of the index.html.
start with the head section which is after navbar. it has a text(h1 and p) and an image that is on the right side of text.
we use grid (container grid) :
## html (head)
```
<!-- head -->
    <section class="features-head bg-primary py-3">
        <div class="container grid">
            <div>
                <h1 class="xl">Featurse</h1>
                <p class="lead">
                    Check out the features of Loruki that separate us from the cometition
                </p>
            </div>
            <img src="images/server.png" alt="">
        </div>
    </section>
```
## css (head)
justify-self helps us to justify the item itself within it's block of grid. instead of all the items (justify-content).
```
/* features.html */
/* head */
.features-head img{
    width: 200px;
    /* this will push the img to the right */
    justify-self: flex-end;
}
```
## html (sub head)
this is also looks like head section:
```
<!-- sub head -->
    <section class="features-sub-head bg-light py-3">
        <div class="container grid">
            <div>
                <h1 class="md">The Loruki Platform</h1>
                <p>
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ducimus nulla aliquid possimus sequi dicta, delectus doloremque voluptatem maxime esse nostrum inventore provident, mollitia debitis officia eaque dolorem, hic saepe quaerat?
                </p>
            </div>
            <img src="images/server2.png" alt="">
        </div>
    </section>
```
## css (sub head)
make the image a little bit smaller.
```
/* sub head */
.features-sub-head img{
    width: 300px;
    justify-self: flex-end;
}
```
## html (main)
we have cards in this section that want to align them using grid and align inside of each card using flex.
```
<!-- main -->
    <section class="features-main my-2">
        <div class="container grid">
            <div class="card flex">
                <i class="fas fa-server fa-3x"></i>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odio, dolore aliquam assumenda sint esse accusamus consequatur rerum earum fugit eligendi dicta aspernatur doloremque tenetur veritatis, distinctio delectus commodi, recusandae quo.
                </p>
            </div>
            <div class="card flex">
                <i class="fas fa-network-wired fa-3x"></i>
                <p>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus
                    recusandae perferendis culpa, reiciendis a itaque debitis qui vel
                    dignissimos ipsum!
                </p>
            </div>
            <div class="card flex">
                <i class="fas fa-laptop-code fa-3x"></i>
                <p>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Debitis,
                    magnam.
                </p>
            </div>
            <div class="card flex">
                <i class="fas fa-database fa-3x"></i>
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, a!
                </p>
            </div>
            <div class="card flex">
                <i class="fas fa-power-off fa-3x"></i>
                <p>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Debitis,
                    magnam.
                </p>
            </div>
            <div class="card flex">
                <i class="fas fa-upload fa-3x"></i>
                <p>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Debitis,
                    magnam.
                </p>
            </div>

        </div>
    </section>
```
## css (main)
```
/* make some space on the left and right of the icons */
.features-main .card > i{
    margin: 0 10px;
}
/* to show the shadow of the top and bottom cards */
.features-main .grid{
    overflow: visible;
}

.features-main .grid >*:first-child{
    grid-column: 1 / span 3;
}
/* this is how we pick other elements in grid */
.features-main .grid >*:nth-child(2){
    grid-column: 1 / span 2;
}
```
# Loruki docs.html
## html (head)
we also keep the navbar and header.just like the head for the features.
```
<!-- head -->
    <section class="docs-head bg-primary py-3">
        <div class="container grid">
            <div>
                <h1 class="xl">Docs</h1>
                <p class="lead">
                Learn how to setup and install the Loruki platform
                </p>
            </div>
            <img src="images/docs.png" alt="">
        </div>
    </section>
```
## css (head)
fixing the img:
```
/* docs.html */
/* head */
.docs-head img{
    width: 200px;
    justify-self: flex-end;
}
```
## html (main)
we have two main card here that each has it's own elements:
```
<!-- main -->
    <section class="docs-main my-4">
        <div class="container grid">
            <!-- card 1 -->
            <div class="card bg-light p-3">
                <h3 class="my-2">Essentials</h3>
                <nav>
                    <ul>
                        <li><a href="#">Introduction</a></li>
                        <li><a href="#">About Loruki</a></li>
                        <li><a href="#">Installation</a></li>
                    </ul>
                </nav>
                <h3 class="my-2">Deployments</h3>
                <nav>
                    <ul>
                        <li><a href="#">Setting up a container</a></li>
                        <li><a href="#">Using the CLI</a></li>
                        <li><a href="#">Upgrade & downgrade</a></li>
                    </ul>
                </nav>
            </div>

            <!-- card 2 -->
            <div class="card">
                <h2>Introduction</h2>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Accusamus, dolorem? Magnam, eum maiores molestiae in a, dignissimos voluptatibus dolorem blanditiis architecto voluptates, harum ea recusandae esse inventore quasi obcaecati laboriosam?</p>
                <div class="alert alert-success">
                    <i class="fas fa-info"></i> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quibusdam, alias?  
                </div>
                <h3>Lorme, ipsum dolor.</h3>
                <p>
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dignissimos, aperiam officiis. In vitae saepe expedita id ut nostrum quidem dolores.
                </p>
                <a href="#" class="btn btn-primary">Install CLI</a>
                <h3>Requairments</h3>
                <ul>
                    <li>Windows 10, Mac OSX, Linux</li>
                    <li>Node.js v12 or higher</li>
                </ul>
                <p>Mac (Homebrew)</p>
                <pre><code>$ brew install loruki-cli</code></pre>
                <p>NPM</p>
                <pre><code>$ npm install loruki-cli</code></pre>
                <p>Yarn</p>
                <pre><code>$ yarn install loruki-cli</code></pre>
            </div>
        </div>
    </section>
```
## css (main)
```
/* main */
.docs-main h3{
    margin: 20px 0;
}

/* to make the second card wider and align them on top */
.docs-main .grid{
    grid-template-columns: 1fr 2fr;
    align-items: flex-start;
}

/* we use nav li not only li because there is another li on the other card that we don't want to target it */
.docs-main nav li{
    font-size: 17px;
    padding-bottom: 5px;
    margin-bottom: 5px;
    border-bottom: 1px solid #ccc;
}

.docs-main a:hover{
    font-weight: bold;
}
```
