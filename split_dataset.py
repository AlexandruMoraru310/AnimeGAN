import os
import shutil
import random


copy_path = "/home/alexandru/Downloads/out2"
root = "/home/alexandru/data/AnimeGAN"

all_files = os.listdir(copy_path)
png_files = list(filter(lambda fl: fl[-4:] == ".png", all_files))
random.shuffle(png_files)

number_of_files = len(png_files)
number_of_files_test = number_of_files//5
number_of_files_valid = number_of_files//5

files_valid = sorted(png_files[0:number_of_files_valid])
files_test = sorted(png_files[number_of_files_valid:number_of_files_valid + number_of_files_test])
files_train = sorted(png_files[number_of_files_valid + number_of_files_test:number_of_files])

train_path = os.path.join(root, "train")
test_path = os.path.join(root, "test")
valid_path = os.path.join(root, "valid")

if os.path.isdir(train_path):
    shutil.rmtree(train_path)

os.mkdir(train_path)
for fl in files_train:
    shutil.copy2(os.path.join(copy_path, fl) , train_path)

if os.path.isdir(test_path):
    shutil.rmtree(test_path)

os.mkdir(test_path)
for fl in files_test:
    shutil.copy2(os.path.join(copy_path, fl) , test_path)

if os.path.isdir(valid_path):
    shutil.rmtree(valid_path)

os.mkdir(valid_path)
for fl in files_valid:
    shutil.copy2(os.path.join(copy_path, fl) , valid_path)
