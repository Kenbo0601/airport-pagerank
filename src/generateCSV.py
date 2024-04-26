import csv

# Path to the input text file
input_file_path = 'source-dest.txt'

# Path to the output CSV file
output_file_path = 'source-dest.csv'

# Read the text file and split the lines into a list, skipping empty lines
with open(input_file_path, 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

# Write the list to a CSV file
with open(output_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in lines:
        # Split each line by white space (spaces or tabs) and write it to the CSV file
        csvwriter.writerow(line.split())

print("CSV file has been created successfully.")
