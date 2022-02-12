import os
import pandas as pd


source_folder = "/home/alexandru/data/AnimeGAN_clean"
subfolders = ["train", "test", "valid"]


all_files = sorted(os.listdir(os.path.join(source_folder, "train")))
files_train = pd.Series(all_files, name="train")
all_files = sorted(os.listdir(os.path.join(source_folder, "test")))
files_test = pd.Series(all_files, name="test")
all_files = sorted(os.listdir(os.path.join(source_folder, "valid")))
files_valid = pd.Series(all_files, name="valid")

with pd.ExcelWriter("selected_files.xlsx") as writer:
    files_train.to_excel(writer, index=False, sheet_name="train")
    files_test.to_excel(writer, index=False, sheet_name="test")
    files_valid.to_excel(writer, index=False, sheet_name="valid")
