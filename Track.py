# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:59:08 2018

@author: giorge.luiz
"""

import math

#moviment coordinates
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# Input
"""The first input line contains three integers n, m and k (1 ≤ n, m ≤ 50, n·m ≥ 2, 1 ≤ k ≤ 4). 
Then n lines contain the map. Each line has the length of exactly m characters and consists of lowercase Latin letters and characters S and T. 
It is guaranteed that the map contains exactly one character S and exactly one character T.

Pretest 12 is one of the maximal tests for this problem."""

inpt = """5 3 2
Sba
ccc
aac
ccc
abT""".split('\n')

#inpt = """3 4 1
#Sxyy
#yxxx
#yyyT""".split('\n')

#inpt = """1 3 3
#TyS""".split('\n')

# Variables

n = 0
m = 0
k = 0

S = None
T = None

game_map = []

types_visited = []
squares_visited = []
map_path = []

# Methods

def euclidian_distance(x, y):
    result = math.sqrt(math.pow((T['x'] - x),2) +  math.pow((T['y'] - y),2))
    return result

def greedy_choice_property(x, y):
    
    selected_x, selected_y = 0, 0
    selected_distance = 99999999

    for i in range(0,4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n and [next_x,next_y] not in map_path and game_map[next_y][next_x] != 'S': # new coordinate is in the map and it was not visited before and it is not the start point
            if game_map[next_y][next_x] == 'T': # checks if the new coordinate is the end point
                selected_x, selected_y = next_x,next_y
                break
            elif euclidian_distance(next_x,next_y) < selected_distance and len(types_visited) < k:
                selected_distance = euclidian_distance(next_x,next_y)
                selected_x, selected_y = next_x,next_y
            if euclidian_distance(next_x,next_y) < selected_distance and game_map[next_y][next_x] in types_visited: # if the algorithm can't visit a new type, it selects only the matching type with the current square
                selected_distance = euclidian_distance(next_x,next_y)
                selected_x, selected_y = next_x,next_y
     
    if selected_x == S['x'] and selected_y == S['y']:
        return -1, -1
    
    if game_map[selected_y][selected_x] not in types_visited and game_map[selected_y][selected_x] != 'T':
        types_visited.append(game_map[selected_y][selected_x])
    if game_map[selected_y][selected_x] != 'T':
        squares_visited.append(game_map[selected_y][selected_x])
        map_path.append([x,y])
    
    return selected_x, selected_y

def greedy_choice(x,y):
    if x == T['x'] and y == T['y']:
        print(squares_visited)
        return
    if x == -1 and y == -1:
        print(-1)
        return
    next_x, next_y = greedy_choice_property(x,y)
    greedy_choice(next_x, next_y)
    

def load_data():
    global n, m, k, S, T, game_map
    split_input = []
    for item in inpt:
        split_input.append(item.split(' '))
    n,m, k, game_map = int(split_input[0][0]), int(split_input[0][1]), int(split_input[0][2]), inpt[1:]
    
    for i in range(0, len(game_map)):
        for j in range(0, len(game_map[0])):
            if game_map[i][j] == 'S':
                S = {'x' : j, 'y' : i}
            elif game_map[i][j] == 'T':
                T = {'x' : j, 'y' : i}
    

def main():
    load_data()
    greedy_choice(S['x'],S['y'])

main()


