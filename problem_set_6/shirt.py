import sys
import os
from PIL import Image, ImageOps

def main():
    # Check command line arguments
    check_command_line()

    # Open input image
    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt
    shirt_file = Image.open("shirt.png")
    # Get the size of the shirt
    shirt_size = shirt_file.size
    # resize muppet image to fit the shirt
    muppet_image = ImageOps.fit(image_file, shirt_size)
    # Paste shirt in muppet
    muppet_image.paste(shirt_file, shirt_file)
    # Create Ouput image
    muppet_image.save(sys.argv[2])

            
def check_command_line():
    # check if command line arguments are 3 or else exit with message
    if len(sys.argv) < 3:
        sys.exit("Too low command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        input_file, output_file = sys.argv[1], sys.argv[2]
        # get the extensions of the files
        input_extension = os.path.splitext(input_file)[1].lower()
        output_extension = os.path.splitext(output_file)[1].lower()
        
        # if the extensions are not valid then exit the program with message
        if not check_extension(input_extension):
            sys.exit("Invalid input")
        if not check_extension(output_extension):
            sys.exit("Invalid ouput")
        if input_extension != output_extension:
            sys.exit("Input and output have different extensions")

        
def check_extension(extension):
    # Check the extensions are valid or not
    if extension not in [".jpg",".jpeg",".png"]:
        return False
    return True
    
if __name__ == "__main__":
    main()