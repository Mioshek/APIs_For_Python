import subprocess
import pathlib
arr = [334,123,5,6,1,71,7]
cmd = ["cargo", "run", "--"] + [str(i) for i in arr]
path = pathlib.Path().resolve()

try:
    process:subprocess.run = subprocess.run(cmd, stdout=subprocess.PIPE)
    output_list:list = str(process.stdout)[3:-4].split("\\n")
    print (output_list)
except Exception as exc: print(exc)