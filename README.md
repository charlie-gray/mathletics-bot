# mathletics-bot
bad mathletics addition bot i made for a meme

# Requirements
1. python (lol)
2. chrome
3. selenium

to install selenium, run the following commands
``` 
$ pip install selenium
$ pip install webdriver_manager
``` 

# How to use

1. start the script (main.py)
2. log into mathletics and start an online addition game
3. wait until the first question shows up, then press enter

# Using devtools-bot.py

if you dont want to open a new window every time you want to start a new match, use this bot

1. run `.\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"` in the same directory as chrome.exe
2. start the script (devtools-bot.py)
3. log into mathletics and start an online addition game
4. wait until the first question shows up, then press enter
5. run the script again and it should work with the previous window you had opened
