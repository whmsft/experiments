import struct
def read_png_file(file_path):
    with open(file_path, 'rb') as file:
        file.seek(16)  # Skip the PNG file header

        while True:
            try:
                byte_data = file.read(4)  # Read 4 bytes of pixel data
                if len(byte_data) < 4:
                    break  # Reached end of file

                r, g, b, a = struct.unpack('BBBB', byte_data)
                pixel_hex = f'{r:02x}{g:02x}{b:02x}{a:02x}'
                yield pixel_hex
            except struct.error:
                break  # Invalid data

# Example usage
file_path = 'untitled.png'  # Replace with the path to your PNG file
pixels = list(read_png_file(file_path))
for pixel in pixels:
    print(pixel)

print(len(pixels))

