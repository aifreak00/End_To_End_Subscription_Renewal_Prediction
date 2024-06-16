from AI4Renewals.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()
# from AI4Renewals.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()
# from AI4Renewals.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig,ModelEvaluationConfig, ModelPusherConfig
# from AI4Renewals.components.data_ingestion import DataIngestion
# from AI4Renewals.components.data_validation import DataValidation
# from AI4Renewals.components.data_transformation import DataTransformation
# from AI4Renewals.components.model_trainer import ModelTrainer
# from AI4Renewals.components.model_evaluation import ModelEvaluation
# from AI4Renewals.components.model_pusher import ModelPusher

# # DATA ingestion instance
# di_ins = DataIngestion(DataIngestionConfig)
# di_art = di_ins.initiate_data_ingestion()

# #Data validation instance
# dv_ins = DataValidation(data_ingestion_artifact=di_art, data_validation_config=DataValidationConfig)

# # #datavalidation artifact
# dv_art = dv_ins.initiate_data_validation()

# # #Data transformation isntance
# dt_ins = DataTransformation(data_ingestion_artifact=di_art, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_art)

# # #Data transformation artifact
# dt_art = dt_ins.initiate_data_transformation()


# # #Lets create modeltrainer instance
# mt_ins = ModelTrainer(data_transformation_artifact=dt_art, model_trainer_config=ModelTrainerConfig)

# # #ModelTrainer Artifact
# mt_art = mt_ins.initiate_model_trainer()

#Model evaluation instance
# me_ins = ModelEvaluation(model_eval_config=ModelEvaluationConfig, data_ingestion_artifact=di_art, model_trainer_artifact=mt_art)
# #Model evaluation artifact
# me_art = me_ins.initiate_model_evaluation()