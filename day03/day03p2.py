from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=3)
def main():#(a..Z -> 1..52                      ) for char in backpack    for group of three in                   1st, 2nd, 3rd in       0 to length of backpacks  every 3 backpacks                
    pri = [[[p-38 if (p:=((ord(c)%96)))>37 else p for c in b] for b in g] for g in [puzzle.input_data.splitlines()[x:x+3] for x in range(0, len(puzzle.input_data.splitlines()), 3)]]
    return sum([list(set(g[0]) & set(g[1]) & set(g[2]))[0] for g in pri]) # sum of priorities for each priority which occurs in every backpack in groups of threes
if __name__ == "__main__": print(main())