def cntWordOccur(str1,str2):
    x = 0
    list1 = str1.split()
    for i in list1:
        if i == str2:
            x += 1
    return x


def cntWordsOccur(list1):
    x = 0
    mylist = []
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            if list1[i] == list1[j]:
                x += 1
        mylist.append([i,x])
        x = 0

    for i in mylist:
        for j in mylist:
            if mylist[i] == mylist[j]:
                x += 1
        for j in range(0,(x-1)):
            mylist.remove(i)
    return mylist

def two_lists_less_than(list1,list2):
    mylist = []
    for i in range(0,len(list1)):
        if list1[i] >= list2[i]:
            mylist.append(True)
        else: mylist.append(False)
    return mylist


def test(l):
    for i in range((len(l)-1),0,-1):
        print(i)
    
