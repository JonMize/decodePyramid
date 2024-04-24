import numpy as np
import re 
#numeric sort for finding sorted numeric order of words in the list
def num_sort(test_string):
    return list(map(int, re.findall(r'\d+', test_string)))[0]
 
def decode(message_file): 
    #First step is read the text file
    file = open(message_file,'r')
    content = file.readlines()
    file.close()
    #turn the content string into a list of each line in the text file
    arr = np.array(content)
    #creates filter array which is half the size of arr
    filter_arr = np.array(arr.size/2+1)
    #removes all blank lines from the array
    filter_arr = arr != '\n'
    newarr = arr[filter_arr]
    #turns newarr to a list to be sorted
    newlist = newarr.tolist()
    #sorts by numeric digits in the strings
    newlist.sort(key=num_sort) 
    i = 0
    rows = int((len(newlist)-1)/2)
    number = 0
    finlist = list()
    #nested for loop for creating the pyramid structure
    for i in range(1, rows+1):
        for j in range(1, i+1):
            #tracking newlist[number] gives us the last string in each row of the pyramid
            number += 1
        if number < len(newlist):
            finlist.append(newlist[number-1])
    #converts finlist to a string to be output
    strlist = str(finlist)
    #filter removes all of the numbers from the final string
    result = "".join(filter(lambda x: not x.isdigit(), strlist))
    #this split removes all \n characters that were concatenated to the end of each word
    res = ''.join(result.split('\\n'))
    #print final output
    print(res)
decode(r"C:\Users\lmize\OneDrive\Desktop\Test.txt")
