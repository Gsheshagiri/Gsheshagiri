#10 program in day 2
def countwords(s):
    if s.strip() ==" ":
        return 0
    words = s.split()
    return len(words)
if name == "main":
    s=input("enter the string")
    print("no of words :",countwords(s))
