'''
    Write a Python program to check whether a list contains a sub list.
'''

# Define List and Sub list:
main_list= [10,20,30,40,50,60,70,80]


# sub_list convert in set 
sub_list= set([40,50,60,70])

# Use issubset method it returns True if all items in the set exists in the specified set,
# Otherwise it returns False
res= sub_list.issubset(main_list)

print(res)

                            #"OR"

# Check if main_list contains sub_list
c=0
result=True


'''
Use loop :
            Condition check main_list in i so increment and second time check condition
            c equal sub_list so result True
'''    
for i in sub_list:
    if i in main_list:
        c+=1

if(c==sub_list):
    result=True

# Display the result    
print(result)

