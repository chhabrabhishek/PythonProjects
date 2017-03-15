from PIL import Image
X=0
Y=25
z=1
c=1
d=0
n=1
m=0
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
for v in range(0,9):
	X=0
	Y=40*n+1
	z=1
	c=1
	d=0
	for r in range(0,8):
		for t in range(0,24):
			for u in range(0,25):
				pixels[X,Y]=(222,29,57)
				X=X+1
				Y=Y-1
			X=50*d
			Y=(40*n)+1+z
			z=z+1
		d=d+1
		Y=(40*n)+1
		X=50*c
		c=c+1
		z=1
	X=25
	Y=40*m+16
	d=0.5
	z=1
	c=1.5
	for a in range(0,8):
		for s in range(0,24):
			for k in range(0,25):
				pixels[X,Y]=(238,36,90)
				X=X+1
				Y=Y+1
			X=50*d
			Y=40*m+16+z
			z=z+1
		d=d+1
		Y=40*m+16
		X=50*c
		c=c+1
		z=1
	m=m+1
	n=n+1


im.show()