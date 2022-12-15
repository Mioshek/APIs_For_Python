import subprocess
import pathlib
arr = [334,123,5,6,1,71,7,23545,12,6,7,3,12,67,78,8,4,25,72,8,39,33]
cmd = ["cargo", "run", "--"] + [str(i) for i in arr]
path = pathlib.Path(__file__).parent.resolve()
print (path)

try:
    process:subprocess.run = subprocess.run(cmd, stdout=subprocess.PIPE, cwd=path)
    output_list:list = str(process.stdout)[3:-4].split("\\n")
    print (output_list)
except Exception as exc: print(exc)