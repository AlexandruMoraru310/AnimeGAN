import os
import random


path = "/home/alexandru/data/AnimeGAN"
all_files = os.listdir(path)
png_files = list(filter(lambda fl: fl[-4:] == ".png", all_files))
random.shuffle(png_files)

number_of_files = len(png_files)
number_of_files_test = number_of_files//5
number_of_files_valid = number_of_files//5

ind_valid = []
ind_test = []
ind_train = []

for i in range(0, number_of_files_valid):
    print(png_files[i])

for i in range(number_of_files_valid, number_of_files_valid + number_of_files_test):
    print(png_files[i])

for i in range(number_of_files_valid + number_of_files_test, number_of_files):
    print(png_files[i])
