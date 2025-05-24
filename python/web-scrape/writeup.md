# Python Web Scraping Process  
## By Juan Rodriguez
<!--
 Blah blah  
 blah blha   
 bloewadfs
 this is me trying to figure out formatting with the md file format. 
 this is actually super cool.-->

I am trying to follow along with Marco Bonzanini's guide on mining twitter/X data with Python.  
The purpose of this is to help with my understanding of the language. I believe project based learning is the best way to learn. For the purpose of this writeup I will be referring to it as Twitter.  


1. I registered an application with Twitter, and installed tweepy on my system. It is a python library that easily interacts with Twitter's API.  

2.Alright I wrote the connection thing that connects to the API for twitter.  

3. i wrote the program and found out i needed to pay money to use certain features with Twitter's API  


## Web Scraper with BBC news

### Scraping up data with the Keyword "Ukraine"

Made a new Python file. I'm trying to figure this out on my own.

I have succesfully made a web scraper that will scrape headlines on the BBC news website with the key word Ukraine, and save it to a markdown file.  

I will not explain it too much because the comments themselves explain what my process was and what the program does. I am just very happy it does succesfully work. 

### Things I have learned:
- I have learned about several libraries and functions, such as the time library, which I used to have a pause between each creation of a file so as to avoid possibly overwhelming the website. I learned how the requests library works. Essentially gathers all of the HTML data and I used it to present the data in text format/human-readable. Something I like that. It sort of makes sense but it'll make more sense over time for me. beautifulSoup parses through the html data that I acquired from the requests library. I used it to filter through the headlines.  

- I've learned about file writing and the proper process of making a folder using the os library. I fiddled with this right as I finished my script, gave me a minor headache but I got it. Later, I will look at the script again to make sure I understand what I've done, and how the OS stuff works.  

- I remember some stuff from Java so I understood the for loops and attributing the iteration count to a variable, which I used to not only sort through the pages, but also make new files with the iterating page numbers.   

### What I could improve on:
- Making my code more prettier. I'm not sure if its all over the place or if its just that I'm tired, but I am a little bit overwhelmed with how my code looks. At a later date I will remake the code and probably save it under a new branch.  

- Optimization, it feels like a lot of stuff could've been written simpler somehow.

### Thoughts:
I'm quite proud of myself. This project has proved succesful on establishing my knowledge of Python. Maybe I will make a GUI for the script, but that might be doing too much. This started off as following a guide to scrape twitter data into a personal project of a topic of interest. I am excited to continue learning and delving into Python.