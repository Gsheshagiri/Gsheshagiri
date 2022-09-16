# A Python3 program to find a peak element

# Find the peak element in the array
def Peak(arr, n) :

 # first or last element is peak element
 if (n == 1) :
     return 0
 if (arr[0] >= arr[1]) :
      return 0
 if (arr[n - 1] >= arr[n - 2]) :
      return n - 1

 # check for every other element
 for i in range(1, n - 1) :

  # check if the neighbors are smaller
  if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
   return i
   
# Driver code.
arr = []
n =int(input("size"))
print("Enter the array")
for i in range(n):
    b=int(input())
    arr.append(b)
print("Index of peak element",Peak(arr, n))

# This code is contributed by divyeshrabadiya07
