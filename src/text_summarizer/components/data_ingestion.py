import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_size
from pathlib import Path
from text_summarizer.entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, 
            self.config.local_data_file)
            logger.info(f"{filename} downloaded successfully! with following headers: {headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists! of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        zip_file_path = str
        Extracts the zip file into the root_dir
        Function return None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)