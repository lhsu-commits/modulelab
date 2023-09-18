#!/usr/bin/env python3

import os
from PIL import Image

student_username = "student-02-d6f138365c39"
student_ip = "34.23.163.32"
new_size = (600, 400)
new_format = "JPEG"
output_img_dir = "/home/" + student_username + "/supplier-data/images/"

def format_images(new_size, new_format, source_img_dir):
    for file in os.listdir(source_img_dir):
        if (file.endswith(".tiff")):
            filename = file.split(".")
            filename = filename[0]
            img = Image.open(source_img_dir + file)
            img = img.resize(new_size)
            img = img.convert("RGB")
            img.save(output_img_dir + filename + ".jpeg", new_format)
    return


def main():
    source_img_dir = output_img_dir
    format_images(new_size, new_format, source_img_dir)


if __name__ == "__main__":
    main()
