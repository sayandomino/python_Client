import sys
import json


class DefaultLogger:

    def log_prediction(self, message):
        sys.stdout.write(str(json.dumps(message)))


def loggerfactory(log_method="Default"):
    loggers = {
        "Default": DefaultLogger
    }

    if log_method not in loggers.keys():
        print(" key not present")

    return loggers[log_method]()
