import qrcode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def qrcode_genrator(URL): 
    
    URL = URL.strip()

    qr = qrcode.QRCode()
    qr.add_data(URL)

    img = qr.make_image()
    img.save("qrcode.png")
def display_qrcode():
    
    img = mpimg.imread("qrcode.png")

    plt.imshow(img,cmap='grey')
    plt.axis('off')  
    plt.show()  

print("=============================")
print("        QR CODE MAKER        ")
print("=============================")
print("")
print("Welcome to my qrcode genrator")

url = input("Enter the URL: ")
qrcode_genrator(url)
Yes = input("Display QR code? (Y/n): ")
if Yes.lower() == "y":
    display_qrcode() 
else:
    print("Invalid pick!")
print("Exiting...")