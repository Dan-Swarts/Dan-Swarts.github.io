def round_list(mylist):
    mylist.insert(0,mylist[len(mylist)-1])
    mylist.pop(len(mylist)-1)
    return mylist
