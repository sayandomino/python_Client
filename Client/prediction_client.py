from datetime import datetime

import json

from Client import utils
import uuid

from Client.logger import loggerfactory


class PredClient:
    def __init__(self):
        print("Prediction Client initializing ...")

    def log(self,
            features_dict: dict,
            prediction_dict: dict,
            event_id=None,
            timestamp=None,
            metadata: dict = None,
            instance_id=None):
        if instance_id is None:
            instance_id = utils.get_model_version()
        print(instance_id)
        if event_id is None:
            event_id = uuid.uuid4()
        if timestamp is None:
            timestamp = datetime.utcnow().timestamp() * 1000

        utils.set_event_id(event_id)

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


