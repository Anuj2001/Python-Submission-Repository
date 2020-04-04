# Assigning elements to different lists:
list1=[1,2,3,4,5]
list2=["I","love","you",3000,"times"]
list3=[200,["I","we","You"],"are","pronouns",3]
list4=["list",10,{"sets",5,10},{"key1":"value1","key2":"value2"}]
list4[0]="list4"
list2[3]=5000
print("List1:",list1,"\n")
print("list2:",list2,"\n")
print("List3:",list3,"\n")
print("List4:",list4,"\n\n\n")


# Accessing the elements of a tuple:
tuple1=("tuple1",5,10)
tuple2=(5,0,20)
print("Tuple1:",tuple1,"\n")
print("Tuple2:",tuple2,"\n")
print(tuple1[1:])
print(tuple2[1:-1])
print(tuple2[2:],"\n\n\n")



# Deleting different dictionary elements:
dict={'key1':"I",'key2':"Love",'key3':"You",'key4':3000,'key5':"Times"}
print("Dictionary: ",dict,"\n")
del dict['key5']
print("New dictionary:",dict,"\n")
del dict['key3']
print("New dictionary:",dict)
