import os
from core.rest_client import RestClient
from common.read_data import data
if __name__ == "__main__":
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(BASE_PATH)