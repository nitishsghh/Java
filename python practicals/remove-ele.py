list [0,1,2,3,4,9]
print("printing oragnal list:")
for i in list:
    print(i,end ="")
    list.remove(9)
    print("\nprinting the list after the removal of first element....")
    for i in list:
    print(i,end ="")