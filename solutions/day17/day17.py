import numpy as np
import sys
lines = open('solutions/day17/input.txt').read().splitlines()
arr = np.array([list(line) for line in lines])
sys.setrecursionlimit(1000000)

print(arr)

paths = {(row, col): [] for row in range(arr.shape[0]) for col in range(arr.shape[1])}


def djikstra(row, col, path, paths):
    choices = []
    if row-1 >= 0 and arr[row-1][col] not in paths: