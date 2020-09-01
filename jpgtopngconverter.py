import sys
import os
from PIL import Image

#grab first and second arg
first = sys.argv[1]
second = sys.argv[2]

#check if new/ exists, if not create
if not os.path.isdir(second):
	os.makedirs(second)

#print(os.path.isdir(second))
#loop through folder
#convert
#save to new folder

for file in os.listdir(first):
	img = Image.open(f"{first}{file}")
	clean_name = os.path.splitext(file)[0]
	print(clean_name)
	img.save(f"{second}{clean_name}.png","png")
	print("all done!")


