# AI Problem N Queens Variation:
## Problem Statement :
It’s your first day at IU and you are looking for Luddy Hall.  The CS Department has provided a map, but, in typical CS style,  it is encoded with esoteric symbols in an ASCII text file.  The map file consists of N lines, each with M columns, representing a campus of size N×M units.  Each cell of campus is marked with one of three symbols:  # represents your current location, @ is Luddy Hall, sidewalks are marked by., and other buildings, which you are not allowed to enter, are marked by &.  

Here is an example:

....&&&

.&&&...

....&..

.&.&...

.&.&.&.

#&...&@

Your goal is to find the shortest path between where you are and Luddy Hall using this map.  You are allowed to move one sidewalk square at a time in one of four principal compass directions.  Your program should find the shortest distance between the two points and then output a string of letters (compass directions)indicating that solution.

### Part 1: Finding your way
The problem statement says to find the Luddy Hall (@) in the given map.
Solution  :
Search Abstraction Used in Code Sceleton : DFS ( Depth First Search )
As the element from fringe was being popped from the end i.e Stack was being used the DFS abstraction was being used.
Start State : The given Map is the start state of the problem.
Goal State : We should find @ in the minimum steps covered.
Valid States : The nodes that are having values '.' (dot) are the valid positions where a person can go.
Successors : The possible moves for given fringe. i.e we can travel in 4 direction. One row up -> South, One row Down-> North, One column back -> West, One column next-> East
Cost -> Each step cost is 1.

I used the BFS approach in which i used a queue that will pop the 1st element out. But the code went in infinite loop. Then i figured out that the visited states of the fringes were not checked so the nodes that were already visited were again taken in the fringes. So for that i created a visited array in which i will append the positions which has been already visited. So for each iteration while checking the valid moves for successors before adding to the fringe the positions will be checked in the visited array and then only passed to the fringe. This solved the problem of the infinite loop and i got the minimum steps to reach the destination i.e @.
Second requirement was to show the minimum path that is traversed while finding the destination. For this i added the directions in the moves function where the valid move is checked for a given fringe position.
Here i just added a element in the moves tupple which looks like eg  (row + 1, col, 'S'). Here S stands for South. If the next move is in the south direction S is appended in the fringe itself. I changed the fringe structure which will accomodate the current position on the map, minimum path traversed to reach that location , total cost(till that position)
eg [((5, 6), 'NNNEESSSEENNEESS', 16)]
This helped me finding the path that was traveresed till the destination.

#### Code Run :
 ```
 ./find_luddy.py map.txt
 ```
### Part 2 : Hide-and-seek

The Problem statement was to Arrange K friends in a Map such that no two friends can see each other.

Solution :
Search Abstraction Used : Depth First Search is used and queue is used to pop the board from the fringe one by one.

Start/ Initial States : The Board given is the initial state of the solution.

....&&&

.&&&...

....&..

.&.&...

.&.&.&.

#&...&@

Goal State : All the friends placed on the board where they cannot see each other directly.
Eg : (K = 7)

.F..&&&

.&&&...

...F&..

.&.&&F.

F&F&.&F

#&..F&@

```
def count_friends(board)
This function counts the number of 'F' present in the board passed to the function.
```

Valid States : The Friends should be placed such that they cannot see each other. But they can be placed on either side of obstacle i.e '&' in the code. The friends can be placed only where '.' is present.
eg:  F&F&.&F
```
def check_valid_successor(board, row, col)
Validate function for successors
This function check for 4 conditions where the valid position is found.
4 function call for 4 conditions in the If statements.
Check above the current position
1)def check_nodes_above(board, row, col)
Check below the current position
2)def check_nodes_below(board, row, clm)
Check left to the current position
3)def check_nodes_left(board, row, col)
Check right to the current position
4)def check_nodes_right(board, row, col)

If any of the if statement fails the code returns null to the calling function. This helps in iterating the other positions helps in reducing time complexity.
```
Successor Function : All the states in which a friend can be added given the current board states.

```
def successors(board)
This functions helps to add the friends checking all the valid states  
```

For minimizing the time complexity of the code i have used visited_board list in which all the board that have been visited are not visited again and again.

Flow of the Code :
The Main program calls the solve function giving the initial board as an input. The solve functions adds that to the fringe. Till the Fringe is not empty one fringe is popped out using queue and all the successor are calcualted calling successor function. In that function friends are added while checking for all the valid states and conditions required for placing a friend in a particular (row,column).
After that the board that successor sends is checked if it is already visited. If not then for all the successor the Goal state is checked where no of friends are calculated . If it equals to the required number then it returns the board and the solution is found. If the goal state is not reached the successors are added to the fringe and also to the visited array and the procedure repeats till the final state is reached.

#### Code Run :
 ```
 /hide.py map.txt 9
 ```
