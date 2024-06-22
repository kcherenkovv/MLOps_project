import os
import pytest
import scripts.image_processing

from PIL import Image


def test_generate_image_description_image_string():
    input_path = os.path.join('examples', '852.jpg')
    result = scripts.image_processing.generate_image_description(input_path)

    assert isinstance(result, str)


def test_generate_image_description_image_string_bad_path():
    input_path = "bad_path"

    try:
        scripts.image_processing.generate_image_description(input_path)
        result = False
    except FileNotFoundError:
        result = True

    assert result is True


def test_generate_image_description_image_bytes():
    input_path = os.path.join('examples', 'run.jpg')
    with open(input_path, 'rb') as file:
        image = file.read()

    result = scripts.image_processing.generate_image_description(image)

    assert isinstance(result, str)


def test_generate_image_description_image_pillow():
    input_path = os.path.join('examples', 'run.jpg')
    image = Image.open(input_path)

    result = scripts.image_processing.generate_image_description(image)

    assert isinstance(result, str)


def test_generate_image_description_image_unknown_type():
    image = 0

    try:
        scripts.image_processing.generate_image_description(image)
        result = False
    except ValueError:
        result = True

    assert result is True


if __name__ == '__main__':
    pytest.main()
