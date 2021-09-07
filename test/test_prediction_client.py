import datetime
import os
import unittest
import uuid
from Client import utils
from Client.prediction_client import PredictionClient


class PredictionClientTest(unittest.TestCase):

    def setUp(self):
        os.environ['HOSTNAME'] = 'model-6100391064067162909bf2f2-7d75566cb-49l9j'

    def test_prtediction_client(self):

        pred_client = PredictionClient()

        feature_names = ['dropperc', 'mins', 'consecmonths', 'income', 'age']
        feature_values = ['dropperc', 'mins', 'consecmonths', 'income', 'age']

        features_dict = dict(zip(feature_names, feature_values))

        predict_names = ['y']
        predict_values = [100]

        predict_dict = dict(zip(predict_names, predict_values))

        # Record eventID and current time
        event_id = uuid.uuid4()
        event_time = datetime.datetime.now()

        # Custom metadata I want to track for this event
        metadata = {'cohort': 'cohort_id'}
        metadata_names = ['cohort']
        metadata_values = ['cohort_id']

        pred_client.init_models(feature_names, predict_names, metadata_names)

        message = pred_client.log_prediction(feature_values, predict_values, metadata_values, event_id, event_time)

        fetched_event_id = message.get("dmo_event_id")

        assert fetched_event_id == event_id

    def testGetModelVersion(self):
        os.environ['HOSTNAME'] = 'model-6100391064067162909bf2f2-7d75566cb-49l9j'
        fetched_model_version = utils.get_model_version()
        assert fetched_model_version == '6100391064067162909bf2f2'

    def testSetEventId(self):
        mock_event_id = 'event_id'
        utils.set_event_id(mock_event_id)
        fetched_event_id = os.environ.get('EVENT_ID')
        assert fetched_event_id == mock_event_id


if __name__ == '__main__':
    unittest.main()
