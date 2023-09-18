#!/usr/bin/env python3

import os
import requests
import sys

def upload_data(filename, server_ip):
    """Uploads the product description for one product"""
    fruit_description = {}
    with open(filename) as txt_file:
        fruit_name = txt_file.readline().strip()
        fruit_weight = txt_file.readline().split()
        fruit_description = txt_file.readline().strip()
        tmp_index = filename.rfind("/")
        fruit_img = filename[tmp_index+1:].replace("txt","jpeg")
        fruit_summary = {"name":fruit_name, "weight":int(fruit_weight[0]), "description":fruit_description, "image_name":fruit_img}
        response = requests.post("http://" + server_ip + "/fruits/", data=fruit_summary)
        if (str(response.status_code) == "201"):
            print("description successfully uploaded!")
        else:
            response.raise_for_status()
    return


def main():
    student_username = "student-02-750768f8a1b9"
    student_ip = "34.75.165.178"
    descriptions_directory = "/home/" + student_username + "/supplier-data/descriptions/"
    for file in os.listdir(descriptions_directory):
            upload_data(descriptions_directory + file, student_ip)



if __name__ == "__main__":
  main()
