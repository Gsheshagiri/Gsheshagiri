def length(str):
 
    count = 0;
    flag = False;
    length = len(str)-1;
    while(length != 0):
        if(str[length] == ' '):
            return count;
        else:
            count += 1;
        length -= 1;
    return count;
 
str = "loofy is still joy boy";
print("The length of last word is",
                      length(str))