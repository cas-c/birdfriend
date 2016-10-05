from urllib import urlretrieve
import os

bird_pics = "list_of_bird_pics.txt"
with open(bird_pics) as temp_file:
    bird_pic_urls = [line.rstrip('\n') for line in temp_file][0].split(' ')
    for bird_pic_url in bird_pic_urls:
        file_name = bird_pic_url.split("/")[-1]
        print("Downloading " + file_name)
        urlretrieve(bird_pic_url, os.path.join("output/", file_name))