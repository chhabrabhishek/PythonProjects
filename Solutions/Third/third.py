from PIL import Image
X=0
Y=25
try:
	im=Image.new('RGB',(400,400))
except:
	print"Unable to load image"
pixels=im.load()
for e in range(0,10):
	for w in range(0,15):
		for q in range(0,8):
			for i in range(0,25):
				pixels[X,Y]=(255,255,255)
				Y=Y-1
				X=X+1
			for j in range(0,25):
				pixels[X,Y]=(255,255,255)
				Y=Y+1
				X=X+1
		X=0
		Y=Y+1
	X=0
	Y=Y+25
im.show()