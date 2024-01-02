filename = 'python.txt'

with open(filename)as file:
    content = file.read()
    word = content.split()
    words = len(word)
print(words)
#open file and read it by read()
#split the content in the file by split() function,this add each word into a list
#then print the length of that splited words




count = 0
with open(filename,'r')as file:
    for line in file:
        count += len(line.split('.'))
print(count)
#make count as 0
#open file and read
#iterate content from file to line
#where ever the . found it consider as a line and add each line count to count
#print the count


import re
from collections import Counter

with open(filename,'r')as file:
    content = file.read()
    words = re.findall(r'\w+',content.lower())
    repeated_word_count = Counter(words)
print(repeated_word_count)

#use regex function(import re) and re.findall to returns a list containing all matches
#Counter is a built in function use to count the repeated words
#r : any backslashes () in the string are not treated as escape characters.
#w+ : for write and reading       

        
        