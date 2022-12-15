import subprocess
import pathlib
def main(arr):
    cmd = ["cargo", "run", "--"] + [str(i) for i in arr]
    path = pathlib.Path(__file__).parent.resolve()
    print (path)

    try:
        process:subprocess.run = subprocess.run(cmd, stdout=subprocess.PIPE, cwd=path)
        output_list:list = str(process.stdout)[3:-4].split("\\n")
        print (output_list)
    except Exception as exc: print(exc)