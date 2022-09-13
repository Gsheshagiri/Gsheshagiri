#sorted list program
test_list1=[1,2,4]
test_list2=[1,3,4]
print("the list 1 is:",test_list1)
print("the list 2 is:",test_list2)
test_list1.extend(test_list2)
test_list1.sort()
print("the combined sortedlist is:",test_list1)
