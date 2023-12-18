import sys
import curses

def create_maze(lvl=1):
    maze_patterns = [
        [
            "###################",
            "#@#               #",
            "# # ##### ####### #",
            "# #     #       # #",
            "# ########### # # #",
            "#           # #   #",
            "########### # #####",
            "#E          #     #",
            "###################",
        ],
        [
            "###################",
            "#@#               #",
            "# # ##### ####### #",
            "#       #       # #",
            "############# # # #",
            "#           # #   #",
            "########### # #####",
            "#           #    E#",
            "###################",
        ],
        [
            "################################",
            "#@#               #         #  #",
            "# # ##### ####### #  ######    #",
            "#       #       # #  #    # #  #",
            "############# # # #  #      #  #",
            "#           # # ###  #    # #  #",
            "########### # ###### ### #### ##",
            "#           #               # E#",
            "################################",
        ],
        [
           "############################################",
           "#@#               #         #           #  #",
           "# # ##### ####### #  ######    #####       #",
           "#       #       # #  #    # #  #    # #    #",
           "############# # # #  #      #  #      #    #",
           "#           # # ###  #    # #  #    # #    #",
           "########### # ###### ### #### ## ###### ####",
           "#           #               # E#           #",
           "# # ##### ####### ########### ##############",
           "# #       #       #         #              #",
           "# ####### ##### # ### ####### ##############",
           "#           #   #   #   #                  #",
           "########### # # ##### # ############### ####",
           "#           # #   #   #               #    #",
           "############# ### # ######### ####### ######",
           "#         #     # # #         #   #        #",
           "# # ##### ##### # # ####### ##### ##########",
           "# #       #     # #       #     #          #",
           "# ####### ##### # ####### ##### ############",
           "#     #         #        E#     #          #",
           "############################################",
        ],
        [
           "##########################################################################",
           "#@#               #         #           #                                #",
           "# # ##### ####### #  ######    #####    # ################################",
           "#       #       # #  #    # #  #    # # # # #         #                  #",
           "############# # # #  #      #  #      # # # ### ####### ################ #",
           "#           # # ###  #    # #  #    # # # #   #       # #              # #",
           "########### # ###### ### #### ## ###### # ### ####### # #  # ######      #",
           "#           #               #  #            # ####### # ###  # #  # ######",
           "# # ##### ####### ########### ############### #       #   #       # ######",
           "# #       #       #         #               # #  #### ### #########      #",
           "# ####### ##### # ### ####### ############### #       # #    #    ###### #",
           "#           #   #     # #                  #  ####### # #### # ## #    # #",
           "########### # # ##### # ############### ### #            #   # #  ###### #",
           "#           # #   #   #               #     ######### ## # # # #         #",
           "############# ### # ######### ####### #######         #  # # # ###########",
           "#         #     # # #         #   #         #  ########  # # #           #",
           "# # ##### ##### # # ##### # ##### ######### #  #      #  # # # ######### #",
           "# #       #     # #       #     #           #  #      #  # # # #         #",
           "# ####### ##### # ####### ##### # ############ ######### ### # ###########",
           "#     #         #         #     #              #             #          E#",
           "##########################################################################",
        ],
        [
           "############################################################################################################",
           "#@#               #         #           #                                #             #                   #",
           "# # ##### ####### #  ######    #####    # ################################ ########### # ################  #",
           "#       #       # #  #    # #  #    # # # # #         #                  # #         # # #              #  #",
           "############# # # #  #      #  #      # # # ### ####### ################ # ######### #   # ###########  #  #",
           "#           # # ###  #    # #  #    # # # #   #       #                # #         # #####            # #  #",
           "########### # ###### ### #### ## ###### # ### ####### # #  # ######    ########### # #  ############### #  #",
           "#           #               #  #            # ####### # ###  # #  # #####    #   # # #  # #    ######## #  #",
           "# # ##### ####### ########### ############### #       #   #       # ##### #  # # # # #  # #    #        #  #",
           "# #       #       #         #               # #  #### ### ####### #     # #  # # # # #  # # #### ########  #",
           "# ####### ##### # ### ####### ############### #       # #    #    ######  #  # # # # #  # # #              #",
           "#           #   #     # #                  #  ####### # #### # ## #    #  #    #     #  # # # ## ######### #",
           "########### # # ##### # ############### ### #            #   # #  ####### ######## ###  # # #  # #       # #",
           "#           # #   #   #               #     ######### ## # # # #        # #      # #    # # #  # #       # #",
           "############# ### # ######### ####### #######         #  # # # ########## ###### # #### # # #  ###       # #",
           "#         #     # # #         #   #         #  ########  # # #            #    #          #              # #",
           "# # ##### ##### # # ##### # ##### ######### #  #      #  # # # #############   ### ######## #####  #########",
           "# #       #     # #       #     #           #  #      #  # # # #           #     # #        #   #          #",
           "# ####### ##### # ####### ##### # ############ ######### ### # ##########  #     # ##########   ######### ##",
           "#     #         #         #     #              #             #          #  #     #                      # E#",
           "############################################################################################################",
        ]
    ]

    maze = maze_patterns[lvl - 1]

    # Find initial "@" point and end point "E"
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "@":
                player_pos = [i, j]
            elif cell == "E":
                exit_pos = [i, j]

    return maze, player_pos, exit_pos

def draw_maze(win, maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            try:
                win.addch(i, j, cell)
            except curses.error:
                pass


def solve_maze(maze, start, end):
    # Depth-First Search (DFS)
    stack = [(tuple(start), [])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == tuple(end):
            return path

        if current in visited:
            continue

        visited.add(current)

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (current[0] + move[0], current[1] + move[1])

            if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] in (' ', 'E'):
                stack.append((new_pos, path + [move]))

    return None


def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(0)

    # Check for command line arguments to use levels
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    maze, player_pos, exit_pos = create_maze(level)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
            # moves up down lef and rigth with the arrows
        moves = {
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -1),
            curses.KEY_RIGHT: (0, 1)
        }

        move = moves.get(key, (0, 0))

        new_pos = [
            max(0, min(player_pos[0] + move[0], len(maze) - 1)),
            max(0, min(player_pos[1] + move[1], len(maze[0]) - 1))
        ]
        # move validation
        if maze[new_pos[0]][new_pos[1]] in (' ', 'E'):
            maze[player_pos[0]] = maze[player_pos[0]][:player_pos[1]] + ' ' + maze[player_pos[0]][player_pos[1] + 1:]
            maze[new_pos[0]] = maze[new_pos[0]][:new_pos[1]] + '@' + maze[new_pos[0]][new_pos[1] + 1:]
            stdscr.clear()
            draw_maze(stdscr, maze)
            stdscr.refresh()
            player_pos = new_pos

            if new_pos == exit_pos:
                stdscr.addstr(len(maze) // 2, len(maze[0]) // 2 - 5, 'You Win!', curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break
        elif key == ord('a'):
            # Auto-solve the maze when press a
            path = solve_maze(maze, player_pos, exit_pos)

            if path:
                for step in path:
                    new_pos = (player_pos[0] + step[0], player_pos[1] + step[1])
                    maze[player_pos[0]] = maze[player_pos[0]][:player_pos[1]] + ' ' + maze[player_pos[0]][player_pos[1] + 1:]
                    maze[new_pos[0]] = maze[new_pos[0]][:new_pos[1]] + '@' + maze[new_pos[0]][new_pos[1] + 1:]
                    stdscr.clear()
                    draw_maze(stdscr, maze)
                    stdscr.refresh()
                    player_pos = new_pos
                    curses.napms(200)  # Delay for better visibility
                stdscr.addstr(len(maze) // 2, len(maze[0]) // 2 - 5, 'Auto-solved!', curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break

if __name__ == '__main__':
    curses.wrapper(main)
