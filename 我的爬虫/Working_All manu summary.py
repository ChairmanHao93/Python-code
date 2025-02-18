import os
import pandas as pd

# Set the directory where your Excel files are located
directory = r'C:\Users\h.zhang.2\Desktop\All Wolt Manu'

# Get a list of all Excel files in the directory
excel_files = [file for file in os.listdir(directory) if file.endswith('.xlsx')]

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through each Excel file and combine its sheets into the list
for file in excel_files:
    file_path = os.path.join(directory, file)
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names:
        sheet_data = pd.read_excel(xls, sheet_name)
        data_frames.append(sheet_data)

# Concatenate the DataFrames in the list
combined_data = pd.concat(data_frames, ignore_index=True)

# Write the combined data to a new Excel file
output_path = r'C:\Users\h.zhang.2\Desktop\combined.xlsx'
combined_data.to_excel(output_path, index=False)
