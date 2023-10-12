import os
import csv

input_directory = "/home/palashdas/champsim/ChampSim-master/4MB_next_line/stt_pref"
output_csv_file = "output.csv"
lines_to_extract = [-183, -152, -121, -90]

# Function to extract the last word from a given line
def extract_last_word(line):
    words = line.strip().split()
    if words:
        return words[-1]
    else:
        return ""

# List to store all the extracted last words from all files
last_words = []

# Get a sorted list of files in the directory
file_list = sorted(os.listdir(input_directory))

# Iterate through all sorted files in the directory
for item in file_list:
    file_path = os.path.join(input_directory, item)
    if os.path.isfile(file_path):  # Check if it is a file (not a directory)
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Extract the last words for the specified lines
        for line_num_offset in lines_to_extract:
            line_number = len(content) + line_num_offset-1
            if 0 <= line_number < len(content):
                last_word = extract_last_word(content[line_number])
                print(content[line_number])
                last_words.append(last_word)
            else:
                print(f"Line not found in file '{file_path}' at offset {line_num_offset}.")

# Write all the extracted last words to a single CSV file
with open(output_csv_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Last Word'])
    for word in last_words:
        writer.writerow([word])
