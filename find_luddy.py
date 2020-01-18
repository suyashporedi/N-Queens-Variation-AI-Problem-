#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : Suyash Poredi sporedi@iu.edu
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves = ((row + 1, col, 'S'), (row - 1, col, 'N'), (row, col - 1, 'W'), (row, col + 1, 'E'))

    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]


# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc = [(row_i, col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if
               IUB_map[row_i][col_i] == "#"][0]

    visited_nodes = []
    path = ''
    fringe = [[you_loc, '', 0]]

    while fringe:
        (curr_moves, path, curr_dist) = fringe.pop(0)

        for move in moves(IUB_map, curr_moves[0], curr_moves[1]):
            if IUB_map[curr_moves[0]][curr_moves[1]] == "@":
                return str(curr_dist) + ' ' + path
            else:
                if (move[0], move[1]) not in visited_nodes:
                    visited_nodes.append((move[0], move[1]))
                    fringe.append(((move[0], move[1]), path + move[2], curr_dist + 1))
    return 'Inf'

# Main Function
if __name__ == "__main__":
    IUB_map = parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    print("Here's the solution I found:")
    print(solution)
