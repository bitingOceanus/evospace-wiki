import sys
from xml.etree import ElementTree
import shutil
import os
import os.path
import json

from PIL import Image

our_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def lerp(x, y, a):
	return x+(y-x)*a

output_path = "icons"

os.makedirs(output_path)

for dirpath, dirnames, filenames in os.walk(our_path + "/../Content/Generated/Resources"):
	for filename in [f for f in filenames if f.endswith(".json")]:
		fullname = os.path.join(dirpath, filename)
		print (fullname + " is parsing")

		with open(fullname) as f:
			data = json.load(f)

			for object in data["Objects"]:

				if object["Class"] == "IcoGenerator":

					for image in object["Images"]:

						try:
							img = Image.new("RGBA", (32,32), (255,255,255,0))
							output = img.load()

							ibase = Image.open(our_path + "/../gen/Icons/" + image["Base"] + ".png")
							pixels = ibase.load()

							for i in range(img.size[0]):
								for j in range(img.size[1]):
									output[i, j] = pixels[i, j]

							if "MulMask" in image:
								try:
									mbase = Image.open(our_path + "/../gen/Icons/" + image["MulMask"] + ".png")
									mpixels = mbase.load()
									for i in range(img.size[0]):
										for j in range(img.size[1]):
											color = tuple(int((l / 255.0) * (r / 255.0) * 255) for l, r in zip(pixels[i, j], mpixels[i, j]))
											output[i, j] = (color[0], color[1], color[2], pixels[i, j][3])
								except IOError:
									print (our_path + "/../gen/Icons/" + image["MulMask"] + ".png is missed; Base image created.")

							if "AddMask" in image:
								try:
									if isinstance(image["AddMask"], list):
										for addmask in image["AddMask"]:
											mbase = Image.open(our_path + "/../gen/Icons/" + addmask + ".png")
											mpixels = mbase.load()
											for i in range(img.size[0]):
												for j in range(img.size[1]):
													r = int(lerp(output[i, j][0], mpixels[i, j][0], mpixels[i, j][3] / 255.0))
													g = int(lerp(output[i, j][1], mpixels[i, j][1], mpixels[i, j][3] / 255.0))
													b = int(lerp(output[i, j][2], mpixels[i, j][2], mpixels[i, j][3] / 255.0))
													a = max(output[i, j][3], mpixels[i, j][3])

													output[i, j] = (r, g, b, a)
									else:
										mbase = Image.open(our_path + "/../gen/Icons/" + image["AddMask"] + ".png")
										mpixels = mbase.load()
										for i in range(img.size[0]):
											for j in range(img.size[1]):
												r = int(lerp(output[i, j][0], mpixels[i, j][0], mpixels[i, j][3] / 255.0))
												g = int(lerp(output[i, j][1], mpixels[i, j][1], mpixels[i, j][3] / 255.0))
												b = int(lerp(output[i, j][2], mpixels[i, j][2], mpixels[i, j][3] / 255.0))
												a = max(output[i, j][3], mpixels[i, j][3])

												output[i, j] = (r, g, b, a)
								except IOError:
									None

							img.save(output_path + "/" + image["NewName"] + ".png")
						except IOError:
							print (image["NewName"] + " err" + str(IOError))

for dirpath, dirnames, filenames in os.walk(our_path + "/../gen/Icons"):
	for filename in [f for f in filenames if f.endswith(".png")]:
		fullname = os.path.join(dirpath, filename)
		img = Image.open(fullname)
		name_only = os.path.splitext(filename)[0]
		name = output_path + "/" + name_only + ".png"
		img.save(name)

