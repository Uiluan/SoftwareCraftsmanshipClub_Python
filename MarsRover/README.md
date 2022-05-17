# [Mars Rover](https://katalyst.codurance.com/simple-mars-rover)
Redeveloped after Chapter 9, using test driven design. No app has been created, only the rover functionality
implemented as classes and unit tested.

The divisions in these classes is largely arbitrary. I took a look at changing things to use dependency injection,
but ran into a quirk where mocking the lower layers function meant I really didn't have much to real logic to test,
because all of my logic was in that function. Nevertheless, it was a fun playground for learning about testing
and at least thinking about splitting out classes.

## Result
Running "python3 -m pytest" in my environment produces the following:
![PytestResults](resources/PytestResults.png)