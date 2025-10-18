#printing out lists
courses = ['history', 'maths', 'compsci']
print(courses)

#how many items are there in the list
print(len(courses))

#how to access values individually
print(courses[0]) 
#0 is where indexing starts- 0 for 1st item
#negative indexes start from the end of the list
#-1 for compsci
#index error for something that doesnt exist

#accessing range of values
#slicing lite
print(courses[0:2]) #the second index is not inclusive at all
print(courses[:2]) #same as above
print(courses[1:]) #all the way to the end

#modifying items in the list

#adding items to our list- gen to the last
courses.append('art')
print(courses)

#adding items to our list- at a specific position
courses.insert(0, 'art')
print(courses)

#method2
courses = ['history', 'maths', 'compsci']
courses_2 = ['art' , 'education'] #combine the two

courses.insert(0, courses_2)
print(courses)
#but lets use the extend method
courses.extend(courses_2)
print(courses)
#????some diff wrt append and extend

#removing values
courses = ['history', 'maths', 'compsci']
courses.remove('maths')
print(courses)
#method2- the pop method- to remove the last value o
courses.pop()
print(courses)

#sorting
#reversing
fruits = ['apple', 'banana', 'pineapple', 'anar']
fruits.reverse()
print(fruits)
#sorting is alphabetically here
fruits.sort()
print(fruits)

nums = [1, 5, 7, 9]
nums.sort()
print(nums)
nums.sort(reverse=True)
fruits.sort(reverse=True)
print(nums)
print(fruits)

#wanting a sorted version of the list without tampering with the og list
sorted_courses = sorted(nums)
print(sorted_courses)

#printing min value
print(min(nums))

#printing max value
print(max(nums))

#printing min value
print(sum(nums))

#finding out index of the elements in a list
subj = ['History', 'Math', 'CompSci', 'Art']
print(subj.index('CompSci'))
#for a value that doesnt exist u'll get value error
print('Math' in subj) #will give true
print('Hindi' in subj) #will give false

#for loop
for item in subj:
    print(item)