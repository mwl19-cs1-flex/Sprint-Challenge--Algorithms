#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n)
A is a constant that will only increase as the while loop continues, and that loop will continue while a is less than n * n * n. Here, all that matters is how large n is, and not the exponents of n. That is because we are only checking the size of n times itself, not how many times we multiple n by itself (for example, in a for loop).


b) Runtime is O(n log n)
The sum is a constant that is not checked against any other value, the only values we check are j and whether or not it is less than n. The for loop has a value of O(n), as we are running the logic inside of it against the range of n. Inside that loop, we run a while loop that has j *= 2. This is exponential growth, so this is O(log n). We multiply each value of Big O for each line, and get O(n log n)


c) Runtime is O(n)
This function is only testing against the value of bunnies (n in our case) and if it is 0. If it is not 0, return 2 plus the function being run recursively with bunnies minus 1. The only value that matters in this case is bunnies, and as it is being used once, run that function recursively. 

## Exercise II



