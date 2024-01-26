# CS:3980: Assignment 1
Assignment 1: Python Refresher for CS:3980: Web Application Development

## echo.py
echo.py takes in a user input and mimics a real world echo in the console of the last word of the input.
The echo function is implemented recursively as such:
###
![](/Screenshots/echo_screenshot.png)
###
A recursive implementation helped reduce code complexity and made it easy to catch unusual inputs. It can
adapt to a variety of text inputs:
###
![](/Screenshots/echo_output.png)
###
## fib.py
fib.py calculates every fibonacci number and outputs the amount of time it took to calculate each one. It
does this recursively using a standard fibonacci algorithm, but saves time using a Least Recently Used
Cache. The cache saves the results of previous method calls, allowing them to be reused in future calls.
This saves a lot of time for the fibonacci algorithm because it needs to call most numbers twice. The
following graph shows the speed it takes to call any individual fibonacci number using the LRU cache:
###
![](/calc_speed_graph.png)
###
The code outputs this raw data to the console:
###
![](/Screenshots/fib_output.png)
###
This outputting is done in the timer decorator. The decorator runs the fibonacci algorithm for a given
number and times how long it takes, reporting that time before returning the value. See the code here:
###
![](/Screenshots/timer_screenshot.png)
###
