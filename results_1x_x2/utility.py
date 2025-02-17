import random

import numpy as np


def transform_result(str, is_home):
    if is_home:
        if str == '1':
            return 3
        elif str == 'X':
            return 1
        else:
            return 0
    else:
        if str == '1':
            return 0
        elif str == 'X':
            return 1
        else:
            return 3

def get_random_medium_points(points,games):
    sum = points
    for i in range(5-games):
        rand = random.randint(0, 3)
        sum += rand
    return sum/5

def get_result(gol_home, gol_away):
    if gol_home > gol_away:
        return '1'
    elif gol_home < gol_away:
        return '2'
    else:
        return 'X'
    
def convert_result(result):
    if result == 0:
        return '1'
    elif result == 1:
        return 'X'
    else:
        return '2'
    
def convert_result_x(result):
    if result == 0:
        return '1'
    else:
        return '2'
    
def generate_random_trend():
    trend = []
    for i in range(5):
        res = 2
        while res==2:
            res = random.randint(0, 3)
        trend.append(res)
    return trend

def convert_result_one_hot(res):
    max = 0
    index = 0
    for i in range(len(res)):
        if res[i] > max:
            index = i
    if index == 0:
        return '1'
    elif index == 1:
        return 'X'
    else:
        return '2'