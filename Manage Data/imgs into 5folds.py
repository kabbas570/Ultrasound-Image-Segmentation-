import os
import shutil

def copy_files(patient_range, src_folder, dest_folder):
    for i in patient_range:
        for phase in ['ES', 'ED']:
            filename = f'patient{i:04d}_2CH_{phase}_gt.nii.gz'
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            if os.path.exists(src_path):
                shutil.copy(src_path, dest_path)

def main():
    src_folder = r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\all\gts'

    destinations = [
        (range(1, 101), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F1\val\gts', 
         list(range(101, 501)), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F1\train\gts'),
        (range(101, 201), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F2\val\gts', 
         list(range(1, 101)) + list(range(201, 501)), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F2\train\gts'),
        (range(201, 301), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F3\val\gts', 
         list(range(1, 201)) + list(range(301, 501)), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F3\train\gts'),
        (range(301, 401), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F4\val\gts', 
         list(range(1, 301)) + list(range(401, 501)), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F4\train\gts'),
        (range(401, 501), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F5\val\gts', 
         list(range(1, 401)), r'C:\Users\Abbas Khan\Downloads\Resources (1)\all_data\all_data\F5\train\gts')
    ]

    for val_range, val_dest, train_range, train_dest in destinations:
        copy_files(val_range, src_folder, val_dest)
        copy_files(train_range, src_folder, train_dest)

if __name__ == "__main__":
    main()
