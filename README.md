# Download the NBA-images

## Description
This script is intend to download all the images on the NBA website.

For now only the image names and urls are provided as the printing result, no images were downloaded actually. You may browse the images through the urls dicrectly.
The real downloading action will be added later. 

Well,it also depends. 

## How to use
Just run below command in your terminal:

        cd /your/path/nbapro
        scrapy crawl img_download

or, if you wanna save the result:

        scrapy crawl img_download >> result.log
        
## update
now "it depends" is completed. when you run the script, the images will be download into your local drive ('path/project_dir/images'). You may also change it to wherever you like by modifing the setting.

What you need to do is just `scrapy crawl img_download`  after cd to the project_dir.
