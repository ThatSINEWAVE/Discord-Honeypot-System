import os
import json


def list_image_names(directory):
    image_names = []
    images_dir = os.path.join(os.path.dirname(__file__), '..', 'Database/images')
    for filename in os.listdir(images_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_names.append(filename)
    return image_names


def natural_sort_key(s):
    # Key function for natural sorting
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def save_image_names_to_json(image_names, filename):
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'Database')
    filepath = os.path.join(database_dir, filename)
    with open(filepath, 'w') as file:
        json.dump(sorted(image_names, key=natural_sort_key), file, indent=4)


if __name__ == "__main__":
    image_names = list_image_names("images")
    save_image_names_to_json(image_names, "images.json")
