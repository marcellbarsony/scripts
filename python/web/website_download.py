#!/usr/bin/env python3

import requests


def download(url):
    response = requests.get(url)
    # print(response.content)
    with open("response.txt", "w") as file:
        file.write(str(response))


download("https://wikipedia.com/")
