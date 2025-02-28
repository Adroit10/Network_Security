import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data ingestion commpleted")
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        datavalidation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation")
        data_validation_artifact = datavalidation.initiate_data_validation()
        logging.info("Data validation commpleted")
        print(data_validation_artifact)
        logging.info(f"Data Transformation initiated")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info(f"Data transformation completed")
        print(data_transformation_artifact)
        
        logging.info("Model training strated")
        modle_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=modle_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created ")
        print(model_trainer_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)