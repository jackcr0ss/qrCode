import qrcode
from PIL import Image
#needed imports to generate QR Code and open image

#Sourse of url (in future version it will be file download) and a filename input statement
source = 'https://github.com/jmc8252'
filename = input('Enter filename for QR Code: ')


#Generates the QR code based off of size parameters, adds the url to the qr code
qr = qrcode.QRCode(version=1,box_size=15,border=4)
qr.add_data(source)
qr.make(fit=True)

#Cretes the QR Code imgae and saves it based off of predetermined file name
qrImage = qr.make_image(fill='black', back_color='white')
qrImage.save(filename)

#Opens the image file
open = Image.open(filename)
open.show()