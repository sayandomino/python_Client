from datetime import datetime

import json

from Client import utils
import uuid

from Client.logger import loggerfactory


class PredClient:
    def __init__(self):
        print("Prediction Client initializing ...")

    def init_models(self,
                    feature_names,
                    predict_names,
                    metadata_names=None,
                    instance_id=None
                    ):
        self.feature_names = feature_names
        self.predict_names = predict_names
        self.metadata_names = metadata_names

        if instance_id is None:
            instance_id = utils.get_model_version()
            self.instance_id = instance_id

    def log(self,
            features_dict: dict,
            prediction_dict: dict,
            event_id=None,
            timestamp=None,
            metadata: dict = None,
            instance_id=None):
        if instance_id is None:
            instance_id = utils.get_model_version()
        if event_id is None:
            event_id = uuid.uuid4()
        if timestamp is None:
            timestamp = datetime.utcnow().timestamp() * 1000

        utils.set_event_id(str(event_id))

        message = {
            "features": json.dumps(features_dict),
            "predictions": json.dumps(prediction_dict),
            "event_id": event_id,
            "metadata": json.dumps(metadata),
            "timestamp": timestamp
        }

        logging_type = utils.get_environment_value('LOG_METHOD')
        if logging_type is None:
            logging_type = 'Default'

        custom_logger = loggerfactory(logging_type)

        custom_logger.log_prediction(message)

    def log_prediction(self,
                       feature_values,
                       prediction_values,
                       metadata_values=None,
                       event_id=None,
                       timestamp=None,
                       ):
        if event_id is None:
            event_id = uuid.uuid4()
        if timestamp is None:
            timestamp = datetime.utcnow().timestamp() * 1000

        utils.set_event_id(str(event_id))

        message = {
            "prediction_names": self.predict_names,
            "feature_names": self.feature_names,
            "prediction_values": prediction_values,
            "feature_values": feature_values,
            "metadata_names": self.metadata_names,
            "metadata_values": metadata_values,
            "dmo_pred_event_time": timestamp,
            "dmo_processing_time": timestamp,
            "dmo_event_id": event_id,
            "dmo_prediction_instance_id" : self.instance_id
        }

        message_to_be_flushed = {
            "dominodatalab.predictions.message": message
        }

        logging_type = utils.get_environment_value('LOG_METHOD')
        if logging_type is None:
            logging_type = 'Default'

        custom_logger = loggerfactory(logging_type)

        custom_logger.log_prediction(message_to_be_flushed)
