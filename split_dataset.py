import os
import random


path = "/home/alexandru/data/AnimeGAN"
all_files = os.listdir(path)
png_files = list(filter(lambda fl: fl[-4:] == ".png", all_files))
random.shuffle(png_files)

number_of_files = len(png_files)
number_of_files_test = number_of_files//5
number_of_files_valid = number_of_files//5

files_valid = sorted(png_files[0:number_of_files_valid])
files_test = sorted(png_files[number_of_files_valid:number_of_files_valid + number_of_files_test])
files_train = sorted(png_files[number_of_files_valid + number_of_files_test:number_of_files])
