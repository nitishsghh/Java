def reverse(str):
    strl=""
    for i in str:
        strl=i+strl
    return strl

str=input("\n Enter any string:")
print("\n The original string:" ,str)
print("\n The reverse string is",reverse(str))
