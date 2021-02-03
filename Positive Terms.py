# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element

print()
    
print("The positive numbers are:")
num = 0
  
# using while loop      
while(num < len(lst)): 
      
    # checking condition 
    if lst[num] >= 0: 
        print(lst[num], end = " ") 
      
    # increment num  
    num += 1
