import os
import shutil

# Parent Directory path 
parent_dir = "/content/gdrive/My Drive/moneyprinter/shorts"
parent_dir_imgs = "/content/gdrive/My Drive/moneyprinter/imgs"

def save_short(youtube_path, title, description):
  global parent_dir
  name_file = youtube_path.split('/')[-1]
  # Path 
  path = os.path.join(parent_dir, name_file) 
  try: 
    os.makedirs(path, exist_ok = True) 
    print("Directory '%s' created successfully" % name_file) 
  except OSError as error: 
    print("Directory '%s' can not be created" % name_file)
  f = open(path + "/title-desc.txt", "w")
  f.write(title + '\n' + description)
  f.close()
  shutil.copyfile(youtube_path, path + '/' + name_file)

def save_image(img_path, folder_name):
  global parent_dir_imgs
  name_file = img_path.split('/')[-1]
  # Path 
  path = os.path.join(parent_dir_imgs, folder_name) 
  try: 
    os.makedirs(path, exist_ok = True) 
    print("Directory '%s' created successfully" % path) 
  except OSError as error: 
    print("Directory '%s' can not be created" % path)
  shutil.copyfile(img_path, path + '/' + name_file)
