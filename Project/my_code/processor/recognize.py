import loader
from actuator import smap


def setup():
    loader.pictures.load_square_map_images(smap)
    smap.debug_print_edgeless_ids()
    """while True:
        try:
            exec(input())
        except Exception as err:
            print(err)"""


def predict():
    pass


def run():
    setup()
    predict()
