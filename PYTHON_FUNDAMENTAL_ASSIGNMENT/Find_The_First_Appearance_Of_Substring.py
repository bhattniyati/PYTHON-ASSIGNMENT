


string= "The Weather is Good Poor Today..."


index_Not= string.find('Not')
index_Poor= string.find('Poor')

if index_Poor > index_Not:
    result= string[:index_Not]+ 'Good' + string[index_Poor+4:]
else:
    result=string


print("Result: ",result)
