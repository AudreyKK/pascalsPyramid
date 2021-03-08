# 1. [DONE] define a function that creates pascal's pyramid up to the level of
# input. Have it print in a neat, pyramid format
# 2. [DONE] define a function that applies the algorithm you made in the first
# function, but instead of starting at 1, starts at a different number (2, 3,
# etc.). Build it so it takes two numbers as input. The starting number and
# the pyramid level.
# 3. [TODO] find a way to traverse the pyramid in order to find the nth level. This
# will depend on how you initially decided to structure it, and you may have
# to redo some work here. Return the entirity of that level.
# 4. [TODO] Find a way to return the jth item of the nth level of the pyramid.
# 5. [TODO] Since finding the jth item of the nth level is the number of
# ways you can arrange n items. Return a list of sets of all j combinations.
# 6. [TODO] Define an algorithm that will peruse the list of sets that was
# returned in 5. Reurn now the list of sets that are all 100% distinct from
# each other. As in, each index conains a different value.
# 7. [TODO] Refine the algorithm in 6. so that it returns the list of sets
# of all j combinations up to a customizeable level of uniqueness. For example,
# instead of each index in each set being unique, you could settle for x out of
# k where x is any positive integer and k is the length of the set.

def pascalsPyramid(n):
    """Prints a formatted string of pascal's pyramid up to n levels."""
    pyramid = {}
    for i in range(n):
        if i == 0:
            # the start is initialized to 1
            pyramid[i] = [1]
        else:
            pyramid[i] = [1]

            for j in range(len(pyramid[i-1]) - 1):
                val = (pyramid[i-1][j] + pyramid[i-1][j+1])
                pyramid[i].append(val)

            pyramid[i].append(1)

    print(pyramid)
    return pyramid

def formatPyramid(n, pyr):
    """Function to format a dict of arrays in a centered pyramid formation."""
    for i in range(len(pyr)):

        spaces = (n*18)
        strng = ''
        print(strng.join([(str(pyr[i][j]) + " " * 7) for j in range(len(pyr[i]))]).center(spaces))

n = 5
# ret = pascalsPyramid(n)
# formatPyramid(n, ret)

def myPyramid(p, n):
    """Prints a formatted string of similar to Pascal's pyramid up to n levels,
        except instead of starting at 1, it starts at p."""
    pyramid = {}
    for i in range(n):
        if i == 0:
            # the start is initialized to 1
            pyramid[i] = [p]
        else:
            pyramid[i] = [p]

            for j in range(len(pyramid[i-1]) - 1):
                val = (pyramid[i-1][j] + pyramid[i-1][j+1])
                pyramid[i].append(val)

            pyramid[i].append(p)

    print(pyramid)
    return pyramid

ret = myPyramid(2, 10)
formatPyramid(n, ret)
