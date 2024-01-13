import os
import urllib.request as request 
from mlProject_test import logger 
from mlProject_test.utils.common import get_size
import zipfile
import opendatasets as od
from mlProject_test.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # Check if the file is a zip file
        if not zipfile.is_zipfile(self.config.local_data_file):
            print(f"The provided file '{self.config.local_data_file}' is not a valid zip file. Skipping extraction.")
            return

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)