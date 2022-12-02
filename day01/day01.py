from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)

def main():
    return sum(sorted([sum(list(map(int, a.split("\n")))) for a in puzzle.input_data.split("\n\n")], reverse=True)[:int(input("Number of elves to count for calories: "))])
      
if __name__ == "__main__": 
    print(main())