#Task 1: Create an array/list of 5 integers and print each element on a new line.
arr = [1,2,3,4,5]
for i in arr :
    print(i)


#Q2: Find the length of an array without using len().
arr = [1,23,4,34,45,63]
count = 0
for i in arr:
    count +=1
print(count)


# Q3: Reverse an array manually (don’t use slicing like [::-1]).
arr = ['abi','akshu','nithya']
revarr = []
for i in range(len(arr)-1, -1, -1):
    revarr.append(arr[i])
print(revarr)


#Q4: Find if a given number exists in the array.
arr = [1,2,3,34,4,3]
target = 3
for i in range(len(arr)):
    if(arr[i] == target):
        print(True)
        break


#Q5: Return the index of the first occurrence of an element in the array.
arr = [2,24,34,2123,43,54,6,43]
target = 43
for i in range(len(arr)):
    if(arr[i]==target):
        print('the index is',i)
        break


#Q6: Count how many times a given element occurs in the array.
arr = [1,23,4,35,3,5,2,352,5]
target = 5
count = 0
for i in range(len(arr)):
    if(arr[i]== target):
        count +=1
print(count)

#Q7: Find the maximum element in an array.
arr = [12,33,5,23,43,25,53]
max_val = arr[0]
for i in range(1,len(arr)):
    if(arr[i] > max):
        max_val = arr[i]
print(max)


#Q8: Find the minimum element in an array.
arr = [11,15,24,56,12,63,18,14]
min_val = arr[0]
for i in range(len(arr)):
    if(arr[i] < min_val):
        min_val = arr[i]
print(min_val)


#Q9: Find the second largest element in an array.
arr = [1,23,4,45,63,6,8,4,9]
large = arr[0]
small = arr[0]
for i in arr :
    if i > large:
        small = large
        large = i
    elif i > small and i != large:
        small = i
print(small)



#Q10: Calculate the sum of all elements in the array.
arr = [1,24,5,2,6,2]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
print(sum)
