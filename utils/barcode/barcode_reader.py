from pyzbar import pyzbar


def decode(image):
    decoded_objects = pyzbar.decode(image)
    if len(decoded_objects) == 0:
        return None

    return decoded_objects[0].data
