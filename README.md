# pythonQRCodeReader
This script goes through the whole directory and prints the code of all the qrcode pictures.
This script is easy to edit 
Written in python2.7
You need to install python-qrtools to use this script.
You can also use a tool called zbarimg from the command line

=================BUGS==================

It might give you an error saying something like:

raw = toString( 

or something along those lines. 

TO FIX IT:
You need to go to the file where the error is located
and find the LINE that says raw = toString(
and change toString to tobytes()

ANOTHER COMMON BUG
If the script cannot find the name of the file it will 
throw a weird looking error
TO FIX IT: 

Make sure that the file name exists

=================BUGS==================
