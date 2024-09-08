import sys
import argparse
from PIL import Image, ImageDraw

def create_image(width, height):
    return Image.new('RGB', (width, height), 'white')

def show_image(image):
    pixels = image.load()
    for y in range(image.height):
        row = ""
        for x in range(image.width):
            r, g, b = pixels[x, y]
            if (r, g, b) == (255, 255, 255):
                row += "."
            else:
                row += "#"
        print(row)

def draw_pixel(image, x, y, color):
    pixels = image.load()
    pixels[x, y] = color

def erase_pixel(image, x, y):
    draw_pixel(image, x, y, (255, 255, 255))

def save_image(image, filename):
    image.save(filename)

def main():
    parser = argparse.ArgumentParser(description='Simple paint program.')
    parser.add_argument('width', type=int, help='Width of the image')
    parser.add_argument('height', type=int, help='Height of the image')
    args = parser.parse_args()

    image = create_image(args.width, args.height)
    commands = {
        'show': lambda: show_image(image),
        'save': lambda: save_image(image, 'output.png'),
        'help': lambda: print("Commands: show, p x y hex, erase x y, save, q"),
    }

    while True:
        command = input('> ').strip().split()
        if not command:
            continue
        if command[0] == 'q':
            break
        elif command[0] == 'p' and len(command) == 4:
            try:
                x = int(command[1])
                y = int(command[2])
                hex_color = command[3]
                color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
                draw_pixel(image, x, y, color)
            except (ValueError, IndexError):
                print("Invalid command or color")
        elif command[0] == 'erase' and len(command) == 3:
            try:
                x = int(command[1])
                y = int(command[2])
                erase_pixel(image, x, y)
            except ValueError:
                print("Invalid coordinates")
        elif command[0] in commands:
            commands[command[0]]()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == '__main__':
    main()
