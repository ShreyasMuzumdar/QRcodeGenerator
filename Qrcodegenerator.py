import os
import segno
folder_path = "/Users/shreyas/Documents/VScode Projects/QRcodeGenerator/QRcodes"
data = input("Enter the data you would like to turn into a qr code:")
qrcode = segno.make_qr(data)
file_path = os.path.join(folder_path, "website.png")
qrcode.save(
    file_path,
    scale=10,
    border=0,
    light="white"
)