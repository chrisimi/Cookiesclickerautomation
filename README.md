# Cookiesclickerautomation
A little python script which can automate the cookie clicker on https://cookiesclicker.net

# Instructions

## Install selenium webdriver
`pip install selenium` to install selenium
more information https://selenium-python.readthedocs.io/

Selenium WebDriver is licensed with Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) more under https://creativecommons.org/licenses/by-sa/4.0/

## Install matplotlib for graph 
`pip install matplotlib ` to install matplotlib for displaying a graph

license: https://matplotlib.org/users/license.html

## Install numpy 
`pip install numpy`to install numpy

github repo: https://github.com/numpy/numpy
license: https://github.com/numpy/numpy/blob/master/LICENSE.txt

## Install driver for your browser (Google Chrome for example)

go to https://sites.google.com/a/chromium.org/chromedriver/downloads and install the webdriver for your browser version

when you are using another webdriver you have to change

`driver = webdriver.` to your browser:
Firefox: `driver = webdriver.Firefox(PATH)`
and so on...

extract the .exe and put it in a common folder like Program Files (X86) or wherever you like

change in the code following line:
`PATH = "C:\Program Files (x86)\chromedriver.exe`
to the path to your chrome driver executable!!!

# How it works

The program interacts with the HTML code of the website and manipulates it. 

When the program crashed or you closed the browser, a graph will be generated which shows the amount of cookies at time x

Feel free to make a Pull request if you have implemented new features :).
