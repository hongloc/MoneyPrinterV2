from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from config import get_user_data
import os

def upload_youtube_using_selenium(title, description, video_path):
  options = webdriver.ChromeOptions()
  options.add_argument(f"--user-data-dir={get_user_data()}") #e.g. C:\\Users\\noone\\AppData\\Local\\Google\\Chrome\\User Data
  # options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3
  driver = webdriver.Chrome(options=options)
  # driver = webdriver.Chrome(chrome_options=options)
  # driver.get("https://youtube.com")
  # Go to youtube.com/upload
  driver.get("https://www.youtube.com/upload")

  # Set video file
  FILE_PICKER_TAG = "ytcp-uploads-file-picker"
  file_picker = driver.find_element(By.TAG_NAME, FILE_PICKER_TAG)
  INPUT_TAG = "input"
  file_input = file_picker.find_element(By.TAG_NAME, INPUT_TAG)
  file_input.send_keys(video_path)

  # Wait for upload to finish
  time.sleep(5)

  # YouTube Section
  YOUTUBE_TEXTBOX_ID = "textbox"
  YOUTUBE_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_MFK"
  YOUTUBE_NOT_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_NOT_MFK"
  YOUTUBE_NEXT_BUTTON_ID = "next-button"
  YOUTUBE_RADIO_BUTTON_XPATH = "//*[@id=\"radioLabel\"]"
  YOUTUBE_DONE_BUTTON_ID = "done-button"

  verbose = True

  # Set title
  textboxes = driver.find_elements(By.ID, YOUTUBE_TEXTBOX_ID)

  title_el = textboxes[0]
  description_el = textboxes[-1]

  if verbose:
      print("\t=> Setting title...")

  title_el.click()
  time.sleep(1)
  title_el.clear()
  title_el.send_keys(title)

  if verbose:
      print("\t=> Setting description...")

  # Set description
  time.sleep(10)
  description_el.click()
  time.sleep(0.5)
  description_el.clear()
  description_el.send_keys(description)

  time.sleep(0.5)

  # Set `made for kids` option
  if verbose:
      print("\t=> Setting `made for kids` option...")

  is_for_kids_checkbox = driver.find_element(By.NAME, YOUTUBE_MADE_FOR_KIDS_NAME)
  is_not_for_kids_checkbox = driver.find_element(By.NAME, YOUTUBE_NOT_MADE_FOR_KIDS_NAME)

  is_not_for_kids_checkbox.click()

  time.sleep(0.5)

  # Click next
  if verbose:
      print("\t=> Clicking next...")

  next_button = driver.find_element(By.ID, YOUTUBE_NEXT_BUTTON_ID)
  next_button.click()

  # Click next again
  if verbose:
      print("\t=> Clicking next again...")
  next_button = driver.find_element(By.ID, YOUTUBE_NEXT_BUTTON_ID)
  next_button.click()

  # Wait for 2 seconds
  time.sleep(2)

  # Click next again
  if verbose:
      print("\t=> Clicking next again...")
  next_button = driver.find_element(By.ID, YOUTUBE_NEXT_BUTTON_ID)
  next_button.click()

  # Set as unlisted
  if verbose:
      print("\t=> Setting as unlisted...")

  radio_button = driver.find_elements(By.XPATH, YOUTUBE_RADIO_BUTTON_XPATH)
  radio_button[2].click()

  if verbose:
      print("\t=> Clicking done button...")

  # Click done button
  done_button = driver.find_element(By.ID, YOUTUBE_DONE_BUTTON_ID)
  done_button.click()

  # Wait for 2 seconds
  time.sleep(2)

  # Get latest video
  if verbose:
      print("\t=> Getting video URL...")
  driver.quit()

if __name__ == "__main__":
    # upload_youtube_using_selenium("test-upload-file.mp4", "test upload se col title", "test upload desc")
    src = "shorts"
    for fname in os.listdir(src):
        # build the path to the folder
        folder_path = os.path.join(src, fname)
        if os.path.isdir(folder_path):
            # we are sure this is a folder; now lets iterate it
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                print(file_path)
                # now you can apply any function assuming it is a file
                # or double check it if needed as `os.path.isfile(file_path)`