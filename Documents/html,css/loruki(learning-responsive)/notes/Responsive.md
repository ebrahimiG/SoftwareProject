# Responsive <br> index.html, features.html, docs.html
we use @media(max-width:something;){...}
## css (both mobile and tablet)
```
/* to make the site responsive */
/* Tablets and under */
@media(max-width:768px){
    /* put everthing in a column below each other */
    .grid,
    .showcase .grid,
    .stats .grid,
    .cli .grid,
    .cloud .grid,
    .features-main .grid,
    .docs-main .grid{
        grid-template-columns: 1fr;
        grid-template-rows: 1fr;
    }
    .showcase{
        height: auto;
    }
    .showcase-text{
        text-align: center;
        margin-top: 40px;
    }
    /* put the form in the center */
    .showcase-form{
        /* for the item to justify itself at center */
        justify-self: center;
        margin: auto;
    }
    .cli .grid > *:first-child{
    grid-column: 1;
    grid-row: 1;
    }
    .features-head ,.features-sub-head,
    .docs-head{
        text-align: center;
    }
    .features-head img,.features-sub-head img,
    .docs-head img{
        justify-self: center;
    }

    /* fixing the cards to be below each other */
    .features-main .grid > *:first-child ,
    .features-main .grid > *:nth-child(2){
        grid-column: 1;
    }

}

/* Mobile */
@media(max-width:500px){
    /* give some height to navbar for links to have space under the logo */
    .navbar{
        height: 110px;
        /* background-color: red; */
    }
    /* bring the links under the logo */
    .navbar .flex{
        flex-direction: column;
    }
    /* give the links a background and a little padding so the have some space specially from bottom of navbar */
    .navbar ul{
        background-color: rgba(0, 0, 0, 0.1);
        padding: 10px;
    }
}
```