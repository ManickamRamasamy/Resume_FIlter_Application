import PyPDF2
from os import listdir
import  os
from os.path import isfile, join


Filepath = input("Enter path -  use / backslash when typing in directory path: ")

x = [a for a in os.listdir(Filepath) if a.endswith(".pdf")]

# define count of keywords
String = []
Keyword = []


# define keyterms
String = [item for item in input("After completed the Keywords Hit a ENTER button \n Enter the content to search with Space: ").split()]
print(String)
print("Total number keywords entered: ", len(String))
keyword_count = int(input("Enter the count of Minimum number of keywords should matched : "))



for pdf in x:
#    print("\n" + pdf)
    count = 0
    object = PyPDF2.PdfFileReader(pdf)
    NumPages = object.getNumPages()
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        #    print("Page: " + str(i))
        text = PageObj.extractText().lower()
        for word in String:
            if word.lower() in text:
                count = int(count+1)
#               print("Keywords Matched in Resume are: " + word)


    if count>=keyword_count:
        print("\n" + pdf)
        print("Number of keywords matched:" +count)
    else:
        print("Minimum expected keyword(s) count match is not as expected")
