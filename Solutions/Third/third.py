from PIL import Image
X=0
Y=25
z=1
c=1
d=0
n=1
m=0
ch=1
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
	if ch==1:
		c1a=222
		c2a=29
		c3a=57
		c1b=238
		c2b=36
		c3b=90
	elif ch==2:
		c1a=241
		c2a=94
		c3a=46
		c1b=243
		c2b=116
		c3b=75
		
	elif ch==3:
		c1a=247
		c2a=160
		c3a=31
		c1b=254
		c2b=195
		c3b=78
		
	elif ch==4:
		c1a=162
		c2a=163
		c3a=55
		c1b=193
		c2b=182
		c3b=49
		
	elif ch==5:
		c1a=17
		c2a=141
		c3a=121
		c1b=0
		c2b=171
		c3b=149
		
	elif ch==6:
		c1a=0
		c2a=177
		c3a=180
		c1b=65
		c2b=192
		c3b=191
	
	elif ch==7:
		c1a=73
		c2a=105
		c3a=130
		c1b=78
		c2b=133
		c3b=160
	
	elif ch==8:
		c1a=129
		c2a=35
		c3a=106
		c1b=154
		c2b=41
		c3b=137
		
	elif ch==9:
		c1a=167
		c2a=32
		c3a=96
		c1b=193
		c2b=59
		c3b=141
	else:
		print"Nothing"	

	for r in range(0,8):
		for t in range(0,24):
			for u in range(0,25):
				pixels[X,Y]=(c1a,c2a,c3a)
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
	Y=(40*m)+16
	d=0.5
	z=1
	c=1.5
	for a in range(0,8):
		for s in range(0,24):
			for k in range(0,25):
				pixels[X,Y]=(c1b,c2b,c3b)
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
	ch+=1
o=0
for F in range(0,8):
	X=50*o
	Y=24
	i=25
	m=1
	for A in range(0,25):
		for B in range(0,i):
			pixels[X,Y]=(222,29,57)
			X=X+1
			Y=Y-1
		i=i-1
		X=50*o
		Y=24-m
		m=m+1
	o=o+1
o=1
for E in range (0,8):
	X=25*o+1
	Y=0
	i=24
	m=1
	for C in range(0,24):
		for D in range(0,i):
			pixels[X,Y]=(238,36,90)
			X=X+1
			Y=Y+1
		i=i-1
		Y=0
		X=(25*o)+1+m
		m=m+1
	o=o+2
o=0
for G in range(0,8):
	X=50*o
	Y=399
	m=1
	i=25
	for H in range(0,25):
		for I in range(0,i):
			pixels[X,Y]=(222,29,57)
			X=X+1
			Y=Y-1
		i=i-1
		Y=399
		X=50*o+m
		m=m+1
	o=o+1
o=1
for J in range(0,8):
	X=25*o
	Y=375
	m=1
	i=25
	for K in range(0,25):
		for L in range(0,i):
			pixels[X,Y]=(238,36,90)
			X=X+1
			Y=Y+1
		i=i-1
		X=25*o
		Y=375+m
		m=m+1
	o=o+2

im.show()