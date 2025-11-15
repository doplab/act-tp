def overlap(list1,list2):
    res=[]
    for elm in list1:
        if elm in list2:
            if not(elm in res):
                res.append(elm)
    return res

print(overlap([1, 2, 3, 4], [9, 4, 3, 7, 1]))