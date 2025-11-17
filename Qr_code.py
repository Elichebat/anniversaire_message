import qrcode
img =qrcode.make('https://github.com/Elichebat/anniversaire_message')

img.save('qrcode.png')