import pandas as pd

# Define the input and output file paths
input_file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Navigation/f-12-89-hw_nav.400_081'
output_csv_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Navigation/navigation_data.csv'

# Read the file content and parse it based on assumed structure
# Assuming it's a text file with space-separated values
data = []
with open(input_file_path, 'r') as file:
    for line in file:
        # Split the line into columns based on whitespace
        columns = line.split()
        data.append(columns)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print("Navigation data has been saved to CSV file.")
