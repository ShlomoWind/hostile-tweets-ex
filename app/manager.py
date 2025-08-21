from app import fetcher
from app import processor

class Manager:
    def __init__(self):
        self.connector= fetcher.Connection()
        self.processor = processor.Process(self.connector.get_data_frame())

    def run(self):
        processed_data = self.processor.get_processed_data()
        return processed_data.to_dict(orient='records')