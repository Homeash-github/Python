
def count_substring(string, sub_string):
    c=0
    l=len(string)
    l1=len(sub_string)
    a=string.index(sub_string)
    #print(a,l1)
    for i in range(l):

        if(sub_string in string):
            c+=1
            string=string[a+l1-1:]
        #print(string)
    
    return c
print(count_substring("ABCDCDC","CDC"))
