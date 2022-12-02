from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)
def main(): # this is blackmagic fuckery. i dont know how to explain it
    return sum([3-( 1 - ((ord(g))%3) - (ord(o)-65) )%3 + (ord(g)-88)*3 for o, g in [line.split(" ") for line in puzzle.input_data.splitlines()]])
if __name__ == "__main__": print(main())