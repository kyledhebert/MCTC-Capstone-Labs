from PIL import Image
import sys

#Open file

def main():

    if (len(sys.argv) < 2):
        sys.exit("Please specify a filename")

    filename = sys.argv[1];

    if (len(sys.argv) == 3):
        lines = int(sys.argv[2])
    else:
        lines = 35    
    try :
        img = Image.open(filename)
    except FileNotFoundError:
        exit("Sorry, that file not found")
    except OSError:
        exit("That file doesn't seem to be an image")

    ascii(img,lines)


def ascii(img,lines):

    h = img.height    #Height & width of original image, in pixels
    w = img.width

    ascii = ""  #Will contain our ascii picture; a string of characters

    y_boxes = lines   #Since displaying in terminal, will make picture 35 lines tall.
    y_box_pix = int(h / lines)     #How many pixels on one line?

    x_boxes = int(w / y_box_pix) * 2  #Use twice as many characters for length as height
    x_box_pix = int(y_box_pix / 2) #And half as many pixels

    #Loop over all of the boxes....

    for ybox in range(0, y_boxes):

        for xbox in range(0, x_boxes):

            left = xbox * x_box_pix
            upper = ybox * y_box_pix
            right = left + x_box_pix
            lower = upper + y_box_pix

            #Crop this box and return as new image.
            cropbox = img.crop((left, upper, right, lower));

            colors = cropbox.getcolors()   #Extract colors as "an unsorted list of count, pixel values"

            #Identify most popular RGB color in this box; we'll call this "average" color
            avg = avg_col(colors);

            #Turn this color into a grayscale color - a single number in range 0-255
            gray = color_to_gray(avg)

            #And transform this average color into one of our ASCII character 'pixels'
            pixel = ascii_pix(gray)

            ascii += pixel

        ascii += '\n'

    print(ascii)


def avg_col(colors):

    #Example of colors; a list of ( frequency, (r,g,b) ) tuples of the most popular colors in this image;
    #the frequencies seem to be normalized to add up to 16.

    # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]

    if colors is None:
        return 0;

    #Find most popular color. Turn it to grayscale. Return grayscale value, between 0-255.
    mostpopindex = 0
    occurance = colors[0][0]
    for c in range(len(colors)):
        if colors[c][0] > occurance:
            occurance = colors[c][0]
            mostpopindex = c

    pop_color = colors[mostpopindex][1]

    return pop_color


def color_to_gray(color):

    gray = 0.3 * color[0] + 0.6 * color[1] + 0.1 * color[2]
    #http://stackoverflow.com/questions/687261/converting-rgb-to-grayscale-intensity
    #Rounded to nearest 0.1, it doesn't matter if we are not perfectly accurate

    #make sure in range 0 to 255.

    if gray < 0:
        return 0
    if gray > 255:
        return 255

    return int(gray);


    #Can edit this to create alternate palette of characters.
    #Characters arranged from 'light' to 'dark'.
ascii_pixels = [
        ' ',
        '.',
        '~',
        '/',
        '*',
        '0',
        '#',
        '@'
    ]


def ascii_pix(color):

    #color is a number between 0 and 255
    #divide by 24

    val = 255-color;

    index = int(val/32)

    #val in range 0-255. We only have 8 different pixels.
    #Divide gray by 32 to reduce range to 0-7.

    return ascii_pixels[index];



if __name__ == '__main__':
    #Running this as a script: call the main method.
    main()
else:
    #Importing this module from somewhere else; for example, a test case
    #Without this, the main method would be run when the module is imported into the
    #test case, which is probably not the behavior you want,
    #You probably don't need the else clause for this if statment
    #but I added it so I had somewhere to write this comment.
    pass