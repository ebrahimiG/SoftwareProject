# Utilities
## css (utilities)
>utility calss: the class that we use all around the website.

* thses class are in a different file (utilities.css).

__container__ : _maximum width_ to make it smaller than navbar. 
_margin(0 auto)_ this makes container have no margin top and bottom and to be in center of navbar from left and right.
_overflow(auto)_ to fix the space comming from h1(logo) form top(line-height).
```
.container{
    max-width: 1100px;
    margin: 0 auto;
    overflow: auto;
    padding: 0 40px;
}
```
__flex__ : utility class of flex to make thing in container Flex 
(just because we didn't want to put the display things in the container it self).
we can also use this class other places 

_display(flex)_ makes elements place beside each other (in a row).
_justify-content(center)_ horizontal move (main).
_align-item(center)_ vertically move (cross).
_height(100%)_ keeps the (container flex) in the navbar and not over flowing from bottom.
```
.flex{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    
}
```
__grid__ : display(grid) and grid-template makes the elemets palce beside each other in a row. gap is for space between elements in a row. justify-content and align-item are the same as flex. and height(100%) is for to make the grid fill the size of its container.

```
.grid{
    display: grid;

    /* it's the same as grid-template-columns: 1fr 1fr; */
    grid-template-columns: repeat(2,1fr);
    
    gap: 20px;
    justify-content: center;

    /* vertically */
    align-items: center;
    height: 100%;
}
```
__grid-3__ : when we have 3 element in div, we use this with grid class. we use it in stats. : 
```
.grid-3{
    grid-template-columns: repeat(3,1fr);
}
```

__card__ : box-shadow x y rgba --> x shadow on the right and -x on the left, y showdow on the bottom and -y on the top. rgb is for the color of the shadow and a is for opacity of it (the alpha value).
```
.card{
    background-color: #fff;
    color: #333;
    border-radius: 10px;
    box-shadow: -4px 3px rgba(0,0,0,0.2);
    padding: 20px;
    margin: 10px;
}
```
__btn__ : buttons.
```
.btn{
    display: inline-block;
    padding: 10px 30px;
    cursor: pointer;
    border: none;
    background-color: var(--primary-color);
    color: #fff;
    border-radius: 5px;
}
```
__btn:hover__ : scale the button down (make it smaller) when hover.
```
.btn:hover{
    transform: scale(0.98);
}
```
__btn-outline__ : for the buttons that have the same background-color as their div, we can use this class and the btn class at the same time. (like the Read More button at the showcase section)
```
.btn-outline{
    background-color: transparent;
    border: 1px #fff solid;
}
```
__bg-primary, secondary, dark, light__ : background-color. we use variables that we defined in basics.
```
/* Backgrounds and buttons colors */
.bg-primary,.btn-primary{
    background-color: var(--primary-color);
    color: #fff;
}
.bg-secondary,.btn-secondary{
    background-color: var(--secondary-color);
    color: #fff;
}
.bg-dark,.btn-dark{
    background-color: var(--dark-color);
    color: #fff;
}
.bg-light,.btn-light{
    background-color: var(--light-color);
    color: #333;
}
```
we do this actually because the icons in the footer were dark but we want our links to be white (except for btn-light and bg-light):
```
.bg-primary a,.btn-primary a,
.bg-secondary a, .btn-secondary a,
.bg-dark a, .btn-dark a{
    color: #fff;
}
```
__text-primary, secondary, dark, light__ : 
```
/* text colors */
.text-primary{
    color: var(--primary-color);
}
.text-secondary{
    color: var(--secondary-color);
}
.text-dark{
    color: var(--dark-color);
}
.text-light{
    color: var(--light-color);
}
```

__lead, sm, md, lg, xl__: these are font sizes:
```
/* text sizes --> rem:16px in default */
.lead{
    font-size: 20px;
}
/* small */
.sm{
    font-size: 1rem;
}
/* medium */
.md{
    font-size: 2rem;
}
/* large */
.lg{
    font-size: 3rem;
}
/* x large */
.xl{
    font-size: 4rem;
}
```

__text-center__ : put the text in center.
```
.text-center{
    text-align: center;
}
```
__alert__ : successs, error, icon
```
/* Alert */
.alert{
    background-color: var(--light-color);
    padding: 10px 20px;
    font-weight: bold;
    margin: 15px 0;
}
.alert i{
    margin-right: 10px;
}
.alert-success{
    background-color: var(--success-color);
    color: #fff;
}
.alert-error{
    background-color: var(--error-color);
    color: #fff;
}
```
__m__: margin all around
```
.m-1{
    margin: 1rem;
}
.m-2{
    margin: 1.5rem;
}
.m-3{
    margin: 2rem;
}
.m-4{
    margin: 3rem;
}
.m-5{
    margin: 4rem;
}
```
__my__ : this is about margin Y (top and bottom). rem is a css unit basicaly means the muliplier of the root element's font size. the html tag(default is 16px) unless define it yourself like html{font-size: ;}. for example my-1 gives you 16px marging on the top and bottom.
```
.my-1{
    margin: 1rem 0;
}
.my-2{
    margin: 1.5rem 0;
}
.my-3{
    margin: 2rem 0;
}
.my-4{
    margin: 3rem 0;
}
.my-5{
    margin: 4rem 0;
}
```
__p__: padding all around:
```
.p-1{
    padding: 1rem;
}
.p-2{
    padding: 1.5rem;
}
.p-3{
    padding: 2rem;
}
.p-4{
    padding: 3rem;
}
.p-5{
    padding: 4rem;
}
```
__py__ : it's same like my:
```
.py-1{
    padding: 1rem 0;
}
.py-2{
    padding: 1.5rem 0;
}
.py-3{
    padding: 2rem 0;
}
.py-4{
    padding: 3rem 0;
}
.py-5{
    padding: 4rem 0;
}
```