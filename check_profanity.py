from urllib.request import urlopen
import re

#read text from a document
def read_text():
    #r at the beg. of the path is for r, if I dont use that, it fails
    quotes = open(r"C:\Git_HL\udacity-python\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()

#check the text for cursed words
def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="+text_to_check
    #print(test)
    urlNoSpace = re.compile('\s')
    url = urlNoSpace.sub('%20', url)
    connection=urlopen(url)
    output=connection.read()
    #print(output)
    if "true" in str(output):
        print ("Alert!!! There is profanity in this file")
    elif "false" in str(output):
        print ("You Are Good! There is NO profanity in this fileb")
    connection.close()
    
read_text()




