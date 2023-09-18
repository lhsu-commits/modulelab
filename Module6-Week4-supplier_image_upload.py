#!/usr/bin/env python3
import os
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

api_url = "http://localhost/upload/"
student_username = "student-02-d6f138365c39"
img_directory = "/home/" + student_username + "/supplier-data/images/"

for file in os.listdir(img_directory):
    if (file.endswith(".jpeg")):
        with open(img_directory + file, "rb") as img_file:
            response = requests.post(api_url, files={"file": img_file})
            if (str(response.status_code) == "201"):
                print("image successfully uploaded!")
            else:
                response.raise_for_status()
