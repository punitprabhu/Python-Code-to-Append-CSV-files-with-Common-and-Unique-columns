import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = 'D:/Blackstraw/Webscrapping/UPC'

# Get list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty list to store DataFrames
dfs = []

# Iterate over each CSV file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(folder_path, file))

    # Append the DataFrame to the list
    dfs.append(df)

# Perform a union operation on the DataFrames
combined_df = pd.concat(dfs, ignore_index=True, sort=False)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('D:/Blackstraw/Webscrapping/combined.csv', index=False)

# Optionally, you can also display the combined DataFrame
print(combined_df)
