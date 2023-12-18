# DFS Maze solver
### Video Demo: https://youtu.be/aavw76TPw-o
#### Hello! This is my final project, a maze solver using the DFS (Depth-First Search) algorithm. It auto-solves the maze when you press 'a.' You can also try to defeat the algorithm using the arrow keys, but you won't be able to win against hahahaha *MALEVOLENT LAUGHTER* Anyway, this was made with a lot of effort and care. To understand the algorithm, I needed to use it in a more visual way. Also, I love to solve problems and make games, and this is what I came up with. I couldn't make use of Pygame or Turtle for the display, so I ended up using Windows-curses.

## HOW DFS WORKS
## General Explanation:
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It starts at the root (or an arbitrary node) and explores as far as possible along each branch before backtracking.
### Initialization:

Maintain a stack to keep track of vertices to visit.
Mark all vertices as not visited.
### Traversal:

Start with an initial vertex and mark it as visited.
Explore adjacent unvisited vertices.
If a dead-end is reached, backtrack to the nearest unexplored vertex.
### Termination:

Continue until all vertices are visited or a specific condition is met.
Specific Explanation (Maze Solver Game):
The provided maze solver game uses the DFS algorithm to find a path from the starting point "@" to the exit point "E" in a maze. Here's how it works:

### Maze Representation:

The maze is represented as a grid of characters.
"@" represents the starting point, "E" represents the exit, and "#" represents walls.
The maze is initially displayed on the screen.
### DFS for Maze Solving:

The DFS algorithm is used to find a path from the starting point to the exit.
The DFS stack maintains the current position and the path taken so far.
The algorithm explores adjacent unvisited positions until the exit is reached.
### User Interaction:

The user can control the movement of "@" using arrow keys (up, down, left, right).
Pressing 'a' triggers an auto-solve mode using DFS, showing the solution step by step.
### Game Mechanics:

The game prevents movement through walls and updates the display after each valid move.
If the user reaches the exit, a "You Win!" message is displayed.
In auto-solve mode, the algorithm solves the maze, and an "Auto-solved!" message is displayed.
### Curses Library:
The curses library is used for terminal-based user interface handling.

## To Use it you will need to have python installed open your terminal and make it big then type in the terminal

### to enter lvl 1
```
python project.py
```
### to enter lvl 2
```
python project.py 2
```

### to enter lvl 3
```
python project.py 3
```
### to enter lvl 4
```
python project.py 4
```

### to enter lvl 5
```
python project.py 5
```

### to enter lvl 6
```
python project.py 6
```