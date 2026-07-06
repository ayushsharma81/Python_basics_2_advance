def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")


mylist = [7, 3, 9, 12, 11]

n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break

print(mylist)
