from collections import defaultdict

from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=7)

fs = defaultdict(int)
pwd = []

def main():
    for line in puzzle.input_data.splitlines():
        match line.split(" "):
            case "$", "cd", "..": pwd.pop()
            case "$", "cd", directory: pwd.append(directory)
            case '$', "ls": continue
            case size, _:
                try:
                    fs["/".join(pwd)] += int(size)
                except:
                    continue
    for f in sorted(fs.keys(), key=lambda x: x.count("/"), reverse=True):
        fs['/'.join(f.split("/")[:-1])] += fs[f]
    return fs

if __name__=="__main__": 
    fs = main()
    free = 70_000_000 - fs["/"]
    needed = 30_000_000 - free
    print(min(v for v in fs.values() if v > needed))