# Please install tqdm modules before running this script
!pip install tqdm

import time
from tqdm import trange
print("Hacking NASA...20%")
time.sleep(2)
print("Hacking NASA...40%")
time.sleep(2)
print("Hacking NASA...60%")
time.sleep(2)   
print("Hacking NASA...80%")
time.sleep(2)
print("Hacking NASA...100%")
time.sleep(2)
print("Sucessfully hacked NASA")
for i in trange(100):
    time.sleep(0.05)
time.sleep(1)
print("Accessing NASA server...")
time.sleep(1)
print("Getting NASA databases...")
time.sleep(1)
print("Copying NASA databases to local machine...")
time.sleep(1)
print("Copying initiated......")
for i in trange(100):
    time.sleep(0.05)
print("NASA databases copied successfully")