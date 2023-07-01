def myReverse(s):
 return s[::-1]
def ispalindrome(s):
    rev=myReverse(s)
    if(s==rev):
        return True
    return False
s=input("Enter name")
ans=ispalindrome(s)
if ans==1:
    print("yes")
else:
    print("no")
        
            
