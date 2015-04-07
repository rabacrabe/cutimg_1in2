from distutils.core import setup
import py2exe, os

Mydata_files = []
imgs_dir = 'perso/prog/src/gui/images'
for files in os.listdir(imgs_dir):
    if os.path.isfile(os.path.join(imgs_dir, files)): # skip directories
        f = 'images', [os.path.join(imgs_dir, files)]
        Mydata_files.append(f)

setup(
      windows=["perso/prog/src/gui/launch_gui.py"],
      name="Convert2Leto",
      options={
               "py2exe":
               {
                "includes":["sip",'gzip']
                }
               },
      data_files=Mydata_files
      )