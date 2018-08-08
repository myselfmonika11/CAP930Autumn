#Lists

'''
easy_as=[1,2,3]
print(easy_as)                          #Output: [1,2,3]


empty=[]                                
print(empty)                            #Output: []                
letters=['a','b','c','d']
print(letters)                          #Output: [a,b,c,d]
numbers=[2,3,5]
print(numbers)                          #Output: [2,3,5]
mixed=[4,5,"seconds"]                   
print(mixed)                            #Output: [4,5,'seconds']



numbers=[2,3,5]
numbers.append(7)
print(numbers)                          #Output: [2,3,5,7]

print(numbers[1])                       #Output: 3


numbers=[2,3,5]
print(numbers[0])                       #Output: 2
print(numbers[-1])                      #Output: 7
print(numbers[1:-1])                    #Output: [3,5]
letters=['a','b','c','d']
print(letters[:3])                      #Output: ['a','b','c']

'''

#Nested list

Number=[1,2,3,4,5,6]                    
Alphabet=['A','B','C','D','E']
Nested_List=[Number,Alphabet]
print(Nested_List)                      #Output: [[1,2,3,4,5,6],['A','B','C','D','E']]
print(Nested_List[0])                   #Output: [1,2,3,4,5,6]
print(Nested_List[0][1])                #Output: 2

