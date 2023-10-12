#run build and run commands in the shell

import os
import sys
import subprocess
import time

    # build command
    # build_command = ['./build_champsim.sh', 'bimodal', 'no', 'no', 'no', 'next_line', 'lru', '1']
    # ./build_champsim.sh bimodal no no no next_line lru 1
build_command = "./build_champsim.sh bimodal no no no no lru 1"
run_command = "./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 test.xz"

# run these commands in the terminal

print(build_command)
#run the build command in terminal

subprocess.run(build_command, shell=True)

print(run_command)

# Get the start time
start_time = time.time()


subprocess.run(run_command, shell=True)

# Your program code here
# ...

# Get the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("time to run", elapsed_time)