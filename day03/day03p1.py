from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=3)
def main():
    f = [[n-38 if (n:=((ord(l)%96)))>37 else n for l in s] for s in puzzle.input_data.splitlines()] # a..Z -> 1..52
    return sum([list(set(b[:len(b)//2]) & set(b[len(b)//2:]))[0] for b in f]) # sum union of halves of sets
if __name__ == "__main__": print(main())