from PIL import Image
X=0
Y=0
n=int(raw_input("Enter the distance between 2 consecutive lines"))
w=int(512/(2*n))
try:
	im=Image.new('RGB',(513,513))
except:
	print"Unable to load image"
pixels=im.load()
for i in range(0,w):
	for j in range(0,n):
		X=X+1
		Y=Y+1
	A=X
	B=Y
	while(B!=0):
		pixels[A,B]=(255,255,255)
		A=A+1
		B=B-1
	A=X
	B=Y
	while(A!=0):
		A=A-1
		B=B+1
		pixels[A,B]=(255,255,255)
for k in range(0,w):
	for l in range(0,n):
		X=X+1
		Y=Y+1
	A=X
	B=Y
	while(A!=512):
		pixels[A,B]=(255,255,255)
		A=A+1
		B=B-1
	A=X
	B=Y
	while(B!=512):
		A=A-1
		B=B+1
		pixels[A,B]=(255,255,255)
im.show()