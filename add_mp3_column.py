import csv

# Input CSV file and output CSV file
input_file = 'PlusPunkt Deutsch A1 (English).csv'
output_file = 'decks.csv'

# Open the input and output files
with open(input_file, 'r', newline='') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv, delimiter=';')
    writer = csv.writer(output_csv, delimiter=';')

    for row in reader:
        # Check if there are at least 1 column in the row
        if len(row) >= 1:
            # Modify the first column by adding ".mp3" to it
            first_column = "[sound:" + row[0] + ".mp3" + "]"
            # Add the modified first column as the 5th column
            row.append(first_column)
            # Append the modified row to the output CSV file
            writer.writerow(row)

print("CSV processing complete. Data written to", output_file)
