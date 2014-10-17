'''

'''
def round(float):
    base = int(float)
    if float - base >= 0.5:
        return base+1
    else:
        return base
    
def numlines(text):
    if not text:
        return 0
    line = 1
    for char in text:
        if char == "\n":
           line  += 1    
    return line

def pythagoras(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    
def reverse(list):
    length = len(list)
    for i in range(len(list)/2):
        temp = list[i]
        list[i] = list[length-i-1]
        list[length-i-1] = temp   
    return list
    
def wordcount():
    text = open("test.txt")
    wordlist = text.split()
    worddict = dict()
    for word in wordlist:
        num = worddict.get(word, 0)
        num += 1
        worddict[word] = num
    for key, value in worddict.iteritems():
        print "%s:\t%d"%(key, value)


