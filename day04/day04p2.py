from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=4)
def main():
    return sum([False if (set(r1) & set(r2)) == set() else True for (r1, r2) in [[range(int(t[0]), int(t[1])+1) for t in tp] for tp in [[p.split('-') for p in pp] for pp in [l.split(',') for l in puzzle.input_data.splitlines()]]]])
if __name__ == "__main__": print(main())