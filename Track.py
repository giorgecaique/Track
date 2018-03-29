# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:59:08 2018

@author: giorge.luiz
"""

import math

#moviment coordinates
dx = [-1, 0, 0, -1]
dy = [0, -1, 1,  0]


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

# Variables

n = 0
m = 0
k = 0
types_visited = []
map_path = []
game_map = []

# Methods

def euclidian_distance(x, y):
    result = math.sqrt(math.pow((x - (m-1)),2) +  math.pow((y - (n-1)),2))
    return result

def greedy_choice_property(x, y):
    selected_x, selected_y = 0, 0
    selected_distance = 99999999
    
    for i in range(0,4):
        if x+dx[i] >= 0 and x+dx[i] < m and y+dy[i] >= 0 and y+dy[i] < n: # verifica se está dentro do mapa
            if euclidian_distance((x+dx[i]),(y+dy[i])) < selected_distance and len(types_visited) < k:
                selected_distance = euclidian_distance((x+dx[i]),(y+dy[i]))
                selected_x, selected_y = (x+dx[i]),(y+dy[i])
            elif euclidian_distance((x+dx[i]),(y+dy[i])) < selected_distance and game_map[(y+dy[i])][(x+dx[i])] == game_map[y][x]:
                selected_distance = euclidian_distance((x+dx[i]),(y+dy[i]))
                selected_x, selected_y = (x+dx[i]),(y+dy[i])
                
    if game_map[selected_y][selected_x] not in types_visited:
        types_visited.append(game_map[selected_y][selected_x])
    map_path.append(game_map[selected_y][selected_x])
    return selected_x, selected_y
                    

def greedy_choice(x,y):
    if x == (m-1) and y == (n-1):
        return
    next_x, next_y = greedy_choice_property(x,y) 
    greedy_choice(next_x, next_y)
    

def load_data():
    global n, m, k, game_map
    split_input = []
    for item in inpt:
        split_input.append(item.split(' '))
    n,m, game_map = int(split_input[0][0]), int(split_input[0][1]), split_input[1:n-1]
    

def main():
    load_data()
    greedy_choice(0,0)

main()
