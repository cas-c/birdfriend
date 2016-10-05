from urllib import urlretrieve
import os

bird_pics = "list_of_bird_pics.txt"  
# this list was scraped from the raw html of their gallery page.
# the scraped info was used to build urls for each photo since
# the thumbnail filenames had little variation from the full 
# filename hosted elsewhere. there are 5 or 6 failed downloads.

# realistically this script could be used to download whatever
# space separated list of urls you wanted but i just wanted to
# get matt his bird pics

with open(bird_pics) as temp_file:
    bird_pic_urls = [line.rstrip('\n') for line in temp_file][0].split(' ')
    for bird_pic_url in bird_pic_urls:
        file_name = bird_pic_url.split("/")[-1]
        print("Downloading " + file_name)
        urlretrieve(bird_pic_url, os.path.join("output/", file_name))