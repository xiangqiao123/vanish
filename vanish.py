#test
from PIL import Image
import numpy

i1 = Image.open("Images/pyLogo1.jpg")
i2 = Image.open("Images/pyLogo2.jpg")
i3 = Image.open("Images/pyLogo3.jpg")

print(i1.mode)

res = Image.new(i1.mode, i1.size)
pixels = res.load()

width, height = i1.size

for x in range(0, width):
	for y in range(0, height):
		r1, g1, b1 = i1.getpixel((x,y))	
		r2, g2, b2 = i2.getpixel((x,y))	
		r3, g3, b3 = i3.getpixel((x,y))	

		r = int(numpy.median([r1, r2, r3]))
		g = int(numpy.median([g1, g2, g3]))
		b = int(numpy.median([b1, b2, b3]))
		
		# Need to deal with images with an alpha channel

		pixels[x, y] = (r,g,b)


res.show();
