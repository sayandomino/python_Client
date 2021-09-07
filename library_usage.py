import datetime
import uuid

from Client.prediction_client import PredictionClient

pred_client = PredictionClient()

feature_names = ["dropperc", "mins", "consecmonths", "income", "age"]
feature_values = ["dropperc", "mins", "consecmonths", "income", "age"]

features_dict = dict(zip(feature_names, feature_values))

predict_names = ["y"]
predict_values = [100]

predict_dict = dict(zip(predict_names, predict_values))

# Record eventID and current time
event_id = uuid.uuid4()
event_time = datetime.datetime.now().timestamp() * 1000

# Custom metadata I want to track for this event
metadata = {"cohort": "cohort_id"}
metadata_names = ["cohort"]
metadata_values = ["cohort_id"]

pred_client.init_models(feature_names, predict_names, metadata_names)

pred_client.log_prediction(feature_values, predict_values, metadata_values, event_id, event_time)
