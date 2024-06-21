import os
import pytest

from PIL import Image


def test_dataset_loaded():
    input_dir = 'datasets'
    assert len(os.listdir(input_dir)) != 0


def test_if_all_jpg():
    input_dir = 'datasets'
    for file in os.listdir(input_dir):
        assert file[-3:] == 'jpg'

if __name__ == '__main__':
    pytest.main()