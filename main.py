from escpos import *
p = printer.Serial("COM3")
# Print text
p.text("Hello World\n")
# Print image
p.image("sem_titulo.png")
# Print QR Code
p.qr("You can readme from your smartphone")
# Print barcode
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
# Cut paper
p.cut()
