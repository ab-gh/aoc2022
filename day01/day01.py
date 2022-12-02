from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=1)
N = 3   # top N elves carrying the most calories

def top_n_calories(n):
    inp = np.array(puzzle.input_data.splitlines())      # cast input to numpy array
    spl = np.split(inp, np.where(inp=="")[0])           # split input by "" into subarrays
    filt = [np.array(list(filter(None, s))) for s in spl] # filter "" from subarrays
    summ = [np.sum(a.astype(int)) for a in filt]         # sum these subarrays
    sort = sorted(summ, reverse=True)                   # sort high-low
    return sort[:n]                                     # top n sums

def main():
    print("Calories of top elf:".ljust(30),  top_n_calories(1)[0])    
    print("Calories of top three elves:".ljust(30), sum(top_n_calories(3)))    

if __name__ == "__main__":
    main()