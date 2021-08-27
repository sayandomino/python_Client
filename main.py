import datetime
import uuid

from Client.prediction_client import PredClient

pred_client = PredClient()

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

loggers = {
    "Default": "DefaultLogger"
}

pred_client.log(features_dict, predict_dict, event_id=event_id,
                timestamp=event_time, metadata=metadata)
