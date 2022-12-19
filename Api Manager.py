import subprocess
import os
import pathlib
path = pathlib.Path(__file__).parent.resolve()


class Sorting:
    def __init__(self, sorting_type:str, arr:list) -> None:
        self.executable_path = str(path) + "/Sorting Apis/bubblesort" if sorting_type == "bubblesort" else str(path) + "/Sorting Apis/countingsort"
        self.file_path = self.executable_path + "/tosort.txt"
        self.arr = arr
        self.sort(self.arr)
     
    def create_file(self,arr) -> None:
        with open(self.file_path, 'w+') as f:
            [f.write(str(i)+";") for i in arr]

    def return_sorted(self) -> list:
        with open(self.file_path, 'r') as f:
            sorted = f.readline()
        return sorted
    
    def sort(self, arr) -> list:
        self.create_file(self.arr)
        cmd = ["cargo", "run", "--release", self.file_path]
        try:
            process:subprocess.run = subprocess.run(cmd, cwd=self.executable_path)
        except Exception as exc: print(exc)
        to_return = self.return_sorted()
        os.remove(self.file_path)
        print(to_return)
        return to_return
    

class Generator:
    def __init__(self,lower_limit:int, upper_limit:int, amount:int) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.amount = amount
        self.executable_path = str(path) + "/Generators/RandomNumberGenerator"
        self.file_path = self.executable_path + "/generated.txt"
        self.generate()
        
    def generate(self):
        self.create_file()
        cmd = ["cargo", "run", "--release", self.file_path, str(self.lower_limit), str(self.upper_limit), str(self.amount)]
        try:
            process:subprocess.run = subprocess.run(cmd, cwd=self.executable_path)
        except Exception as exc:
            print(exc)
            
        to_return = self.read_data()
        os.remove(self.file_path)
        return to_return
        
    def create_file(self):
        with open(self.file_path, 'w+') as f:
            f.close()
            
    def read_data(self) -> list:
        with open(self.file_path, 'r') as f:
            files = f.readline()
        return files
