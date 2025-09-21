# Animations
we make our own variables to use : 
```
/* we apply these to some elements */
@keyframes slideInFromLeft{
    0%{
        transform: translateX(-100%);
    }
    100%{
        transform: translateX(0);
    }
}

@keyframes slideInFromRight{
    0%{
        transform: translateX(100%);
    }
    100%{
        transform: translateX(0);
    }
}

@keyframes slideInFromTop{
    0%{
        transform: translateY(-100%);
    }
    100%{
        transform: translateY(0);
    }
}
```
and this is an example of use : 
```
.showcase-text{
    animation: slideInFromLeft 1s ease-in;
}
```
