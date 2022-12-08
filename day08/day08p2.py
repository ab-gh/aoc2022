from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=8)

arr = [list(map(int, x)) for x in puzzle.input_data.splitlines()]
transp = [*zip(*arr)]
scores = []
for x in range(0, len(arr)):
    for y in range(0, len(arr[x])):
        left = [l for l in arr[x][0:y]][::-1]
        right = [r for r in arr[x][y+1:]]
        up = [u for u in transp[y][0:x]][::-1]
        down = [d for d in transp[y][x+1:]]
        tree_score = 1
        for direction in [up, left, down, right]:
            trees_you_can_see = 0
            for tree in direction:
                if tree >= arr[x][y]:
                    trees_you_can_see +=1
                    break
                else:
                    trees_you_can_see += 1
            tree_score = trees_you_can_see * tree_score
        scores.append(tree_score)

print(sorted(scores, reverse=True)[0])