def cntWordOccur(str1,str2):
    x = 0
    list1 = str1.split()
    for i in list1:
        if i == str2:
            x += 1
    return x

def cntWordsOccur(list1):
    mylist = []
    x = 0
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            if list1[i] == list1[j]:
                x += 1
        mylist.append([list1[j],x])
        x = 0
    for i in mylist:
        for j in mylist:
            if i[0] == j[0]:
                x += 1
            if x > 1:
                mylist.remove(j)
            x=0
    return mylist

def IteratingLists(list1):
    mylist = []
    for i in list1:
        if type(i) == list:
            for j in i:
                mylist.append(j)
    return mylist

def location(list1,value):
    for i in range(0,len(list1)):
        if list1[i] == value:
            return i
        
def last_location(list1,val):
    for i in range((len(list1)-1),0):
        if list1[i] == val:
            return i




    
