import pyqrcode
from pyqrcode import QRCode



s = input("enter your QR code info : ")

url = pyqrcode.create(s)

url.svg("MyQR.svg",scale = 20)

