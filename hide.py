#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : Suyash Poredi sporedi@iu.edu
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#
#
import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]


# Count total # of friends on board
def count_friends(board):
    return sum([row.count('F') for row in board])


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F', ] + board[row][col + 1:]] + board[row + 1:]


# Check above the current position
def check_nodes_above(board, row, col):
    for j in range(row - 1, -1, -1):
        if board[j][col] == '&':
            return True
        elif board[j][col] == 'F':
            return False
    return True


# Check below the current position
def check_nodes_below(board, row, clm):
    for j in range(row + 1, len(board)):
        if board[j][clm] == '&':
            return True
        elif board[j][clm] == 'F':
            return False
    return True


# Check left to the current position
def check_nodes_left(board, row, col):
    for j in range(col - 1, -1, -1):
        if board[row][j] == '&':
            return True
        elif board[row][j] == 'F':
            return False
    return True


# Check right to the current position
def check_nodes_right(board, row, col):
    for j in range(col + 1, len(board[0])):
        if board[row][j] == '&':
            return True
        elif board[row][j] == 'F':
            return False
    return True


# Validate function for successors
def check_valid_successor(board, row, col):
    if check_nodes_below(board, row, col):
        if check_nodes_above(board, row, col):
            if check_nodes_left(board, row, col):
                if check_nodes_right(board, row, col):
                    return True
    else:
        return False


# Get list of successors of given board state
def successors(board):
    return [add_friend(board, r, c) for r in range(0, len(board)) for c in range(0, len(board[0]))
            if board[r][c] == '.' and check_valid_successor(board, r, c)]


# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited_board = []
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if s not in visited_board:
                if is_goal(s):
                    return s
                fringe.append(s)
                visited_board.append(s)
    return False


# Main Function
if __name__ == "__main__":
    IUB_map = parse_map(sys.argv[1])
    print(IUB_map)
    # This is K, the number of friends
    K = int(sys.argv[2])
    print("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print("Here's what we found:")
    print(printable_board(solution) if solution else "None")

'''
Citation/Reference 
1) https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
Reference for the traversing the List backwards.

2) N Queen Problem 
for understanding the basic logic of the code.
'''