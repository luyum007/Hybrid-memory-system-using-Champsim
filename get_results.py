import os
dir_path = "/home/palashdas/champsim/ChampSim-master/spec_traces"




# dir_path = "/home/vasu/Documents/ChampSim-master/results_50M"
output_file = "spec_names.txt"

with open(output_file, "w") as f_out:
    for filename in os.listdir(dir_path):
        #add file name to output_file
        f_out.write(f"{filename}\n")






# with open(output_file, "w") as f_out:
#     for filename in os.listdir(dir_path):
#         file_path = os.path.join(dir_path, filename)
#         if os.path.isfile(file_path):
#             with open(file_path, "r") as f_in:
#                 lines = f_in.readlines()
#                 if len(lines) >= 27:
#                     f_out.write(f"{filename}:\n{lines[26]}")