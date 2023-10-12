import subprocess
import os
import shutil

# Set the directory path
directory_path = "/Users/luyumpegoo/Downloads/ChampSim-master/dpc3_traces"
# Get all the filenames in the director
filenames = os.listdir(directory_path)

# Define the common configuration for all simulations
common_config = {
    "build_command": "./build_champsim.sh bimodal no no no next_line lru 4",
    "destination_directory": "/Users/luyumpegoo/Downloads/ChampSim-master/8MB_next_line_dp3",  # Common destination directory
    "run_command": "./run_4core.sh bimodal-no-no-no-next_line-lru-4core 5 50 0",
    "source_file_path": '/Users/luyumpegoo/Downloads/ChampSim-master/results_4core_50M/mix0-bimodal-no-no-no-next_line-lru-4core.txt',
}

# Define the unique configurations for different simulations
simulations = [
    {
        "name": "sram",
        "cache_file": "/Users/luyumpegoo/Downloads/ChampSim-master/cache_files/sram.cc",
        "start_index": 0,  # Set the starting index for the range
        "count": 0,        # Initial count value for this simulation
    },
    {
        "name": "sram_pref",
        "cache_file": "/Users/luyumpegoo/Downloads/ChampSim-master/cache_files/sram_pref.cc",
        "start_index": 0,  # Set the starting index for the range
        "count": 0,        # Initial count value for this simulation
    },
    {
        "name": "hybrid",
        "cache_file": "/Users/luyumpegoo/Downloads/ChampSim-master/cache_files/hybrid_cache.cc",
        "start_index": 0,  # Set the starting index for the range
        "count": 0,        # Initial count value for this simulation
    },
    {
        "name": "hybrid_stt_sram",
        "cache_file": "/Users/luyumpegoo/Downloads/ChampSim-master/cache_files/hybrid_cache_stt_sram.cc",
        "start_index": 0,  # Set the starting index for the range
        "count": 0,        # Initial count value for this simulation
    },
    {
        "name": "hybrid_sram_stt",
        "cache_file": "/Users/luyumpegoo/Downloads/ChampSim-master/cache_files/hybrid_cache_sram_stt.cc",
        "start_index": 0,  # Set the starting index for the range
        "count": 0,        # Initial count value for this simulation
    },
    # {
    #     "name": "stt",
    #     "cache_file": "/home/palashdas/champsim/ChampSim-master/cache_files/stt.cc",
    #     "start_index": 0,  # Set the starting index for the range
    #     "count": 0,        # Initial count value for this simulation
    # },
    # {
    #     "name": "stt_pref",
    #     "cache_file": "/home/palashdas/champsim/ChampSim-master/cache_files/stt_pref.cc",
    #     "start_index": 0,  # Set the starting index for the range
    #     "count": 0,        # Initial count value for this simulation
    # },
    # Add more simulation configurations here as needed
]

print("-------------------------------------------SIMULATION STARTED-------------------------------------------")

def run_simulation(config):
    # Copy the cache file to cache.cc
    source_file = config["cache_file"]
    destination_file = '/Users/luyumpegoo/Downloads/ChampSim-master/src/cache.cc'
    shutil.copyfile(source_file, destination_file)

    count = config["count"]  # Use the initial count value for this simulation
    subprocess.run(common_config["build_command"], shell=True)
    print(f"---------------------------------------------------{config['name']} started----------------------------------------------")
    with open("traces.txt", "w") as file:
        # Write the filenames to the file, one per line
        for i in range(config["start_index"], len(filenames), 4):
            batch_filenames = filenames[i:i+4]  # Get four filenames at a time
            for filename in batch_filenames:
                file.write(filename + "\n")
            command = f"{common_config['run_command']} {' '.join(batch_filenames)}"
            print(count, command)
            subprocess.run(command, shell=True)
            count += 1

            # Set the destination directory mix0-bimodal-no-no-no-no-lru-4core.txt
            destination_directory = os.path.join(common_config["destination_directory"], config["name"])

            destination_file_path = os.path.join(destination_directory, str(count))
            # Copy the file from source to destination
            shutil.copyfile(common_config["source_file_path"], destination_file_path)

    print("completed execution of", count * 4, "traces")
    print(f"---------------------------------------------------{config['name']} COMPLETED-------------------------------------------------")

# Run all simulations
for config in simulations:
    run_simulation(config)

print("---------------------------------------------ALL COMPLETED------------------------------------------------------")
