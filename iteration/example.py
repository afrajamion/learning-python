nums = []
# while loop to add elements to a list
while len(nums) < 5: 
    nums.append(int(input("Enter a number: "))) 

# basic for-loop through a list
for num in nums: 
    print(num ** 2)

countries = {'UK':'London', 'France':'Paris', 'Belgium':'Brussels'}

# for-loop through key-value pairs of a dictionary
for k, v in countries.items(): 
    print(f"The capital of {k} is {v}")

# for-loop through numeric range
for i in range(2,11,2): 
    print(i)

fruits = ["apple", "pear", "banana", "plum", "cherry"]
# checking whether any elements in the list begin with 'p'
print(len([x for x in fruits if x[0] == 'p']) != 0) 

# long-hand approach for capitalising every occurence of 'pear'
newlist = []
for fruit in fruits:
    if fruit == 'pear':
        newlist.append(fruit.capitalize())
    else:
        newlist.append(fruit)

# concise approach using list comp.
newlist = [x.capitalize() if x == 'pear' else x for x in fruits]