#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop will execute n times because n x (n * n) = n**3, after it runs once it's n^2 - drop constant n^3/n^2 giving it's runtime is O(n)

sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
b) O(n ^2) this is a loop running in a nested loop. 


c) 
You may use a binary search to find floor f on which the egg gets broken. 
You'll calculate the middle_floor = n // 2 and drop the egg to see if it breaks. 
If it does break you'll repeat the algorithm on the floors below at 1:middle_floor. 
Repeating this process if the egg continues to break, if the egg does not break you can repeat the algorithm on the upper floors at middle_floor:n

## Exercise II


