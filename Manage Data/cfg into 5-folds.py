import os
import shutil

# Define the source and destination directories
source_dir = r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\all\fgs'
base_dest_dir = r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data'

# Create destination directories if they don't exist
folders = [
    'F1\\val\\fgs', 'F1\\train\\fgs',
    'F2\\val\\fgs', 'F2\\train\\fgs',
    'F3\\val\\fgs', 'F3\\train\\fgs',
    'F4\\val\\fgs', 'F4\\train\\fgs',
    'F5\\val\\fgs', 'F5\\train\\fgs'
]

for folder in folders:
    os.makedirs(os.path.join(base_dest_dir, folder), exist_ok=True)

# Function to copy files
def copy_files(patient_range, val_dest, train_dest):
    for i in range(1, 501):
        filename = f'patient{i:04d}_Info_2CH.cfg'
        source_file = os.path.join(source_dir, filename)
        if i in patient_range:
            dest_file = os.path.join(base_dest_dir, val_dest, filename)
        else:
            dest_file = os.path.join(base_dest_dir, train_dest, filename)
        shutil.copy(source_file, dest_file)

# Copy files to the respective folders
copy_files(range(1, 101), 'F1\\val\\fgs', 'F1\\train\\fgs')
copy_files(range(101, 201), 'F2\\val\\fgs', 'F2\\train\\fgs')
copy_files(range(201, 301), 'F3\\val\\fgs', 'F3\\train\\fgs')
copy_files(range(301, 401), 'F4\\val\\fgs', 'F4\\train\\fgs')
copy_files(range(401, 501), 'F5\\val\\fgs', 'F5\\train\\fgs')

print("Files have been copied successfully.")
