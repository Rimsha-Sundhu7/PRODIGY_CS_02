#path of image
path = r'C:\Users\Dell\Downloads\CCC.jpg'

#take encryption key as input
key = int(input('Enter key for encryption of an image : '))

#print path of image file and encryption key
print('The path of the file : ', path)
print('Key of encryption : ', key)

#open file for reading purpose
fin = open(path, 'rb')

#store image data
image = fin.read()
fin.close()

#covert image into bytearray to perform encrpytion in numeric data
image = bytearray(image)

#perform XOR on each value
for index, values in enumerate(image):
    image[index] = values ^ key

#open file for writting
fin = open(path, 'wb')

#write encryption data
fin.write(image)
fin.close()
print('Encryption Done...')
