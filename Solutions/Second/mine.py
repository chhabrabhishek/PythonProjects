#!/usr/bin/python
import Image

dbLineSpace, lImg = int(raw_input("Enter The Distance Between Lines: "))*(2**0.5), Image.new("RGB", (512, 512))
for lPoint in xrange(int(512/dbLineSpace)):

	