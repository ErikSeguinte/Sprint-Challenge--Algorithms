#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N³)
  * The loop will continue to run a number of times equal to N cubed.


b) O(N²)
  * Includes a nested loop that runs through each element for every interation of the outer loop


c) O(1)
  * The size of the input has no influence on the runtime of this function.
    No matter the size of the input, it will run at the same speed.

## Exercise II
If we were given only a single egg, than the only choice we would have would be a linear search starting from the bottom floor.
This would be a O(N) solution, with a worst case of N meaning that the floor f is the very top floor.

If we assume that "many eggs" means infinite eggs, or at least "enough eggs", then we can use Binary search, which would give us an answer in O(Log₂ N).
Such a solution would find could determine f with a tower of 100 floors with less than 8 eggs broken.
```
bottom = 0
top = n
f == -1

while bottom < top:
    middle = (top + bottom) // 2
    test middle
    if egg breaks, test floors below:
        top = middle
    if egg does not break, test floors above:
        f = middle
        bottom = middle + 1 
end loop

return f
```


a