def seq_search(list, x):
\# complètez ici
for i in range(len(list)): # i est considéré comme un index
    if list[i] == x:
        print("X present in list at index: ", i)
        return i
        break
else: #only used when loop not terminated by a break statement
#if i == len(list)-1 and list[i] != x:  # also possible
        print("X not present in list")
        return -1

liste = [3,55,6,8,3,5,56,33,6,5,3,2,99,53,532,75,21,963,100,445,56,45,12,56,24]
x = 100
seq_search(liste, x)

%%time 
print(seq_search(liste, x))