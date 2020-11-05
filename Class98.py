f=open("D:/WHJ/test.txt")
fileLines=f.readlines()
#print(f.read())


#for line in fileLines:
#    print(line)

    
#myString="Exhistu! Coma Revoo Divoo Blappi"
#words=myString.split()
#print(words)


def ourFunction(name):
    print("My Name Is "+name+", which is your name")
#ourFunction("Smaran")


def countWordsFromFile():
    fileName=input("Filename: ")
    numOfWords=0
    file=open(fileName, 'r')
    for line in file:
        words=line.split()
        numOfWords=numOfWords+len(words)
    print(numOfWords)
#countWordsFromFile()


def jokes():
    num=int(input("Enter a number: "))
    if(num==1):
        print("Which bear has no eyes? Gummy Bears!!")
    elif(num==2):
        print("What do you get when a cow jumps on a trampoline? A milkshake!!")
    elif(num==3):
        print("How do you know that the elephant has been to the fridge? Because she left the footprints in the butter!!")
    else:
        print("Enter a number between 0 and 4")
#jokes()
