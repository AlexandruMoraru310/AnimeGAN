import os
import shutil
import numpy as np
import pandas as pd
import cv2 as cv


source_folder = "/home/alexandru/data/AnimeGAN"
dest_folder = "/home/alexandru/data/AnimeGAN_small"
clean_folder = "/home/alexandru/data/AnimeGAN_clean"
subfolders = ["train", "test", "valid"]

save_for_cleaning = False


border = 45
border_white = 15
img_size = 200

for sb in subfolders:
    source_path = os.path.join(source_folder, sb)
    dest_path = os.path.join(dest_folder, sb)
    path_for_clean = os.path.join(clean_folder, sb)
    all_files = pd.read_excel(
        "./selected_files.xlsx", sheet_name=sb, header=0, verbose=False
    ).squeeze("columns").to_list()
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    if save_for_cleaning is True:
        if os.path.isdir(path_for_clean):
            shutil.rmtree(path_for_clean)
        os.mkdir(path_for_clean)
    for fl in all_files:
        im_s = cv.imread(os.path.join(source_path, fl))
        if border == 0:
            im_d = im_s[...]
        else:
            im_d = im_s[border:-border, border:-border, :]
        im_d = cv.resize(im_d, (img_size, img_size))
        cv.imwrite(os.path.join(dest_path, fl), im_d)
        if save_for_cleaning is True:
            im_w = 255 * np.ones_like(im_d, shape=(img_size + 2*border_white, img_size + 2*border_white, 3))
            im_w[border_white:-border_white, border_white:-border_white, :] = im_d
            cv.imwrite(os.path.join(path_for_clean, fl), im_w)
