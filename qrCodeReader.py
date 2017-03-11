#!/usr/bin/python
import qrtools
qr = qrtools.QR()
i = 1
keyWord = ""
while(True):
  qr.decode("file%d" % i)
	keyWord += qr.data
	if i > 29:
		break
	i+=1
print keyWord
