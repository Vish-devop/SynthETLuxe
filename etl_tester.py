from data_extractor import ETLDataExtractor
from data_loader import ETLDataLoader
from data_transformer import ETLDataTransformer
from data_validator import ETLDataValidator

class ETLTester:
    def __init__(self,num_records):
        self.num_records=num_records

    def run_etl(self):
        data_extractor=ETLDataExtractor(self.num_records)
        extracted_data=data_extractor.extract_data()

        if extracted_data is not None: 
            data_transformer=ETLDataTransformer(extracted_data)
            transformed_data=data_transformer.transform_data()

            if transformed_data is not None: 
                data_loader=ETLDataLoader(transformed_data)
                data_loader.load_data()

                data_validator=ETLDataValidator(transformed_data)
                validation_results=data_validator.validate_data()
                print("ETL Testing completd successfully.")
                print("Validation Results: ",validation_results)
            else: 
                print("Data Transformation Failed!")
        else: 
            print("Data Extraction is failed!! Please check the pipeline of data extraction")