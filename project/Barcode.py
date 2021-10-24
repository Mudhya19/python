import pyqrcode

s = "https://forms.gle/YsamjZXXURD5LznG6"

url = pyqrcode.create(s)

url.svg("FormBPM.svg", scale=8)
