#!/usr/bin/python
from PIL import Image
n=int(raw_input("Enter the distance between 2 consecutive files: "))
m=2*n
X=0
Y=0
try:
	im=Image.new('RGB',(512,512))
except:
	print"Unable to load image"
pixels=im.load()
while(X<=(512-n)):
	for i in range(0,m):
		X=X+1
		Y=Y+1
	A=X
	B=0
	while(A!=0):
		pixels[A,B]=(255,255,255)
		A=A-1
		B=B+1
	m=n

X=512
Y=512
m=2*n
while(X>=n):
	
	X -= m
	Y -= m

	A=X
	B=511
	while(A!=512):
		pixels[A,B]=(255,255,255)
		A=A+1
		B=B-1

	m=n
im.show()
