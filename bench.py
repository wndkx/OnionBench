import timeit
import random
import requests
import sys
import os, shutil
import pyfiglet
from numba import jit

def cpu_bound():
    var = round(random.randint(0, 999999999999) / random.randint(0, 999999999999)) / random.randint(2, 10)
    var2 = random.randint(0, 999999999999) % random.randint(0, 999999999999) / random.randint(2, 10)
    return var, var2
@jit
def gpu_bound():
    var = round(random.randint(0, 999999999999) / random.randint(0, 999999999999)) / random.randint(2, 10)
    var2 = random.randint(0, 999999999999) % random.randint(0, 999999999999) / random.randint(2, 10)
    return var, var2
def network_bound():
    request = requests.get("https://httpbin.org/get")
    return request.status_code, request.content
def is_command(l: list, index: int):
    return index < len(l)
def disk_bound():
    file_id = random.randint(1, 1000000000000000)
    if os.path.isfile(f"bound_cache/{file_id}"):
        file = open(f"bound_cache/{file_id}", "a")
        file.write(f"{file_id} \n")
        file.close()
    else:
        file = open(f"bound_cache/{file_id}", "x")
        file.write(f"{file_id} \n")
        file.close()
def clear_cache():
    shutil.rmtree("bound_cache")
    os.mkdir("bound_cache")
def prompt(command, num):
    try:
        if command == "cpu":
            print(f"Result: " + str(round(timeit.timeit(cpu_bound, number=num), ndigits=2)))
        elif command == "network":
            print(f"Result: " + str(round(timeit.timeit(network_bound, number=num), ndigits=2)))
        elif command == "disk":
            print(f"Result: " + str(round(timeit.timeit(disk_bound, number=num), ndigits=2)))
        elif command == "gpu":
            start = timeit.default_timer()
            for i in range(1, num+1):
                gpu_bound()
            print("Result: ", round(timeit.default_timer()-start, ndigits=2))
        else:
            print("You entered an invalid command! To see all the commands use help.")
    except KeyboardInterrupt:
        print("\nCanceled..")
        sys.exit()
if __name__ == "__main__":
    if not is_command(sys.argv, 1):
        logo = pyfiglet.figlet_format("OnionBench", "standard")
        print(f"{logo}\n")
        print(open("help.txt", "r").read())
    else:
        if sys.argv[1] == "help":
            logo = pyfiglet.figlet_format("OnionBench", "standard")
            print(f"{logo}\n")
            print(open("help.txt", "r").read())
        elif sys.argv[1] == "clean" or sys.argv[1] == "mrproper":
            clear_cache()
            print("Cleared")
        else:
            prompt(sys.argv[1], int(sys.argv[2]))
        
#print(f"Result: " + str(round(timeit.timeit(disk_bound, number=10000), ndigits=2)))
