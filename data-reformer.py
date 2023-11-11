"""
Very simple script to create train, test data

Need to manually replace source and destination folder

I made this instead of using tensorflow util is because the data was not in standard format

Author:

Van Tran

"""



import pandas as pd
import os
import shutil
import random

# split all files 20-80 for train-test
def split_data(source, train, test, split_ratio=0.8):
    files = os.listdir(source)
    num_files = len(files)
    num_train = int(num_files * split_ratio)
    random.shuffle(files)

    train_files = files[:num_train]
    test_files = files[num_train:]

    # Create subfolders for labels inside train and test
    train_label_folder = os.path.join(train, os.path.basename(source))
    test_label_folder = os.path.join(test, os.path.basename(source))

    os.makedirs(train_label_folder, exist_ok=True)
    os.makedirs(test_label_folder, exist_ok=True)

    for file in train_files:
        source_path = os.path.join(source, file)
        destination_path = os.path.join(train_label_folder, file)
        shutil.move(source_path, destination_path)

    for file in test_files:
        source_path = os.path.join(source, file)
        destination_path = os.path.join(test_label_folder, file)
        shutil.move(source_path, destination_path)
for i in [3, 5, 6, 7, 8]:

    # Define the source folder where your files are located.
    source_folder = r"C:\Users\wadva\Downloads\EggTaiwan-20231108T193419Z-001\EggTaiwan\Day" + str(i)

    # Define the destination folder where you want to copy the matching files.
    destination_folder = r"F:\Projects\reformed_data\Day" + str(i)

    # Create train and test datasets as well
    train_folder = destination_folder + r"\train"
    test_folder = destination_folder + r"\test"

    label1_folder = destination_folder + r"\Male"
    label2_folder = destination_folder + r"\Female"

    # Load the Excel file with names and labels.
    excel_file = r"C:\Users\wadva\Downloads\EggTaiwan-20231108T193419Z-001\EggTaiwan\Label.xlsx"
    df = pd.read_excel(excel_file, engine='openpyxl')

    # Loop through each row in the Excel file.
    for index, row in df.iterrows():
        egg_index = row['STT']
        label = row['Lable']

        # Check if the name is not empty and create a destination folder for it.
        if label:
            folder_name = os.path.join(destination_folder, label)
            os.makedirs(folder_name, exist_ok=True)

            # List all files in the source folder.
            files = os.listdir(source_folder)

            # Loop through the files and copy the matching ones to the destination folder.
            for file in files:
                if "egg_" + str(egg_index) + "_" in file:
                    source_file = os.path.join(source_folder, file)
                    destination_file = os.path.join(folder_name, file)
                    shutil.copy2(source_file, destination_file)


    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Splitting data for Male
    split_data(label1_folder, train_folder, test_folder)

    # Splitting data for Female
    split_data(label2_folder, train_folder, test_folder)

    os.rmdir(label1_folder)
    os.rmdir(label2_folder)


print("Files have been copied based on the Excel file.")
