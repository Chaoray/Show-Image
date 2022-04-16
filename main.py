from sys import exit
from sys import argv
from sys import stdout
from os.path import isdir
from os.path import exists
import cv2

if __name__ == '__main__':
    if len(argv) < 3:
        print('Usage: showimg [image path] [compression rate]')
        exit()
    args = argv[1:]

    if isdir(args[0]) or not exists(args[0]):
        print('File does not exist: %s' % args[0])
        exit()
    
    AsciiChars = [' ', '.', ',', '\'', '\"', '-', '+', ':', ';', '(', '[', '{', '=', '#', '%', '@']
    AsciiCharsLength = len(AsciiChars) - 1

    compressionRate = 10
    try:
        compressionRate = int(args[1])
    except ValueError:
        print('Invalid compression rate: %s' % args[1])
        exit()

    img = cv2.imread(args[0])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    print('Original image size: %dx%d' % (width, height))

    width, height = int(width / compressionRate) * 2, int(height / compressionRate)

    print('Compressed image size: %dx%d' % (width, height))
    gray = cv2.resize(gray, (width, height), interpolation=cv2.INTER_AREA)

    print('Processing image... ', end='')
    stdout.flush() # output instantly

    buffer = ''
    for y in range(0, height):
        for x in range(0, width):
            index = int((gray[y][x] * AsciiCharsLength) / 255)
            buffer += AsciiChars[index]
        buffer += '\n'
        
    print('Done!')
    print(buffer)