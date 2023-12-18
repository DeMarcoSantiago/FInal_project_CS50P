import project
import curses


def test_create_maze():
    # Test each level
    for lvl in range(1, 6):
        maze, player_pos, exit_pos = project.create_maze(lvl)

        # Check if maze is a list of strings
        assert isinstance(maze, list)
        assert all(isinstance(row, str) for row in maze)

        # Check if player_pos and exit_pos are lists of length 2
        assert isinstance(player_pos, list) and len(player_pos) == 2
        assert isinstance(exit_pos, list) and len(exit_pos) == 2

        # Check if "@" is at player_pos and "E" is at exit_pos
        assert maze[player_pos[0]][player_pos[1]] == "@"
        assert maze[exit_pos[0]][exit_pos[1]] == "E"

class MockCursesWindow:
    def __init__(self):
        self.contents = []

    def addch(self, i, j, ch):
        # Simulate the behavior of curses addch
        while len(self.contents) <= i:
            self.contents.append([])
        while len(self.contents[i]) <= j:
            self.contents[i].append(' ')
        self.contents[i][j] = ch

def test_draw_maze():
    # Example maze data
    maze = [
        "#####",
        "#@ E#",
        "#####",
    ]

    # Create a mock window
    mock_window = MockCursesWindow()

    # Call the draw_maze function
    project.draw_maze(mock_window, maze)

    # Check if the contents match the expected maze
    assert mock_window.contents == [list(row) for row in maze]
