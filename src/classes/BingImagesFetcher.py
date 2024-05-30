import os
from moviepy.editor import ImageClip
from icrawler.builtin import BingImageCrawler
import random

from .MediaGenerator import MediaGenerator

class BingImagesFetcher(MediaGenerator):
    
    def __init__(self, temp_image_dir = './image_dir_temp/'):
        self.temp_image_dir = temp_image_dir if temp_image_dir.endswith('/') else temp_image_dir + '/'

    def generate(self, query):
        google_crawler = BingImageCrawler(parser_threads=4,
                                            downloader_threads=4,
                                            storage={'root_dir': self.temp_image_dir})
        
        google_crawler.crawl(keyword=query, offset=0, max_num=1,
                            min_size=(400, 400), max_size=None)
        
        chosen_image = random.choice([self.temp_image_dir + image_file for image_file in os.listdir(self.temp_image_dir)])
        # image_clip = ImageClip(chosen_image)
        # os.remove(chosen_image)

        return chosen_image