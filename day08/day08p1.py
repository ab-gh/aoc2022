from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=8)

arr = [list(map(int, x)) for x in puzzle.input_data.splitlines()]
transp = [*zip(*arr)]
sum = 0
for x in range(0, len(arr)):
    for y in range(0, len(arr[x])):
        left = [l for l in arr[x][0:y]]
        right = [r for r in arr[x][y+1:]]
        up = [u for u in transp[y][0:x]]
        down = [d for d in transp[y][x+1:]]
        sum += ([1 if any([all([arr[x][y] > tree for tree in direction]) for direction in [left, right, up, down]]) else 0])[0]
            
print(sum)