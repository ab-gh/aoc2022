from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

def main(): # o=opposition, y=you. use ord() for char->int, and o-y%3 for calculating w/l/d
    return sum([ (6 if ((ord(o)-64 - ord(y)-87) % 3)==2 else 0 if ((ord(o)-64 - ord(y)-87) % 3)==1 else 3) + ord(y)-87 for o, y in [line.split(" ") for line in puzzle.input_data.splitlines()]])
    
if __name__ == "__main__":
    print(main())