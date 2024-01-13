from mlProject_test.config.configuration import ConfigurationManager
from mlProject_test.components.data_validation import DataValiadtion
from mlProject_test import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try: 
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataValiadtionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e
