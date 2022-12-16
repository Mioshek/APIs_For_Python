import subprocess
import pathlib
path = pathlib.Path(__file__).parent.resolve()
file_path = str(path) + "/tosort.txt"

def create_file(arr) -> None:
    with open(file_path, 'w+') as f:
        [f.write(str(i)+";") for i in arr]

def return_sorted() -> list:
    with open(file_path, 'r') as f:
        sorted = f.readline()
    return sorted

def main(arr) -> list:
    create_file(arr)
    cmd = ["cargo", "run", "--release", file_path]

    try:
        process:subprocess.run = subprocess.run(cmd, cwd=path)
    except Exception as exc: print(exc)
    
    return return_sorted()


main([1,2,3,3535,61234,2453,4])
