import fetcher
import processor

class Manager:
    def __init__(self):
        self.connector= fetcher.Connection()
        self.processor = processor.Process(self.connector.get_data_frame())

    def run(self):
        processed_data = self.processor.get_processed_data()
        print(processed_data)