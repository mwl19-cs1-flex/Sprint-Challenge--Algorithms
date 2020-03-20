#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n)
A is a constant that will only increase as the while loop continues, and that loop will continue while a is less than n * n * n. Here, all that matters is how large n is, and not the exponents of n. That is because we are only checking the size of n times itself, not how many times we multiple n by itself (for example, in a for loop).


b) Runtime is O(n log n)
The sum is a constant that is not checked against any other value, the only values we check are j and whether or not it is less than n. The for loop has a value of O(n), as we are running the logic inside of it against the range of n. Inside that loop, we run a while loop that has j *= 2. This is exponential growth, so this is O(log n). We multiply each value of Big O for each line, and get O(n log n)


c) Runtime is O(n)
This function is only testing against the value of bunnies (n in our case) and if it is 0. If it is not 0, return 2 plus the function being run recursively with bunnies minus 1. The only value that matters in this case is bunnies, and as it is being used once, run that function recursively. 

## Exercise II

I can do this naively and drop an egg off of each floor until the egg does not break when dropped, or I can tackle this problem as if I were using Binary Search. I would take the amount of floors in the building and divide them by half, and start on that floor. When dropping the egg, if the egg broke at that floor, I could immediately cancel out the entire upper half of the building, and I would repeat my process with the new middle. 

If, when using the new middle, the egg did not break, I would cancel out the entire lower half of that middle, and repeat the process again with a new middle between my original starting point and my second middle value. I would repeat this process again until I found the true middle.

Here is what the code would look like

def binary_eggs(n, f)
    n is the number of floors total
    f is the current middle 
    I will find f by taking the n and dividing it in half.
    f will be set to that value

    egg_breaks = False
    while egg_breaks is True:
        if I can find f of n,
            divide f in half minus one and recurse the function
        if I cannot
            divide f in half plus one and recurse the function

This algorithm is log of n. 