#!/usr/bin/python
from PIL import Image,ImageFilter
try:
	X=0
	Y=0
	count=0
	n=int(raw_input("Width : "))
	choice=int(raw_input("Enter 1 for horizontal and 2 for vertical"))
	im=Image.new('RGB',(512,512),"Black")
	pixels=im.load()
	if choice==1:
		Y=250
		while (count<n):
			for x in range(1,513):
				pixels[X,Y]=(255,255,255)
				X=X+1   
			X=0
			Y=Y+1
			count=count+1
		im.show()
	elif choice==2:
		X=250
		while (count<n):
			for x in range(1,513):
				pixels[X,Y]=(255,255,255)
				Y=Y+1	
			Y=0
			X=X+1
			count=count+1
		im.show()
	else:
		print"Enter valid choice"
except:
	print"Cannot load file"