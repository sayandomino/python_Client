class DefaultLogger:
    def log_prediction(self, message):
        print(message)


def loggerfactory(log_method="Default"):
    loggers = {"Default": DefaultLogger}

    if log_method not in loggers.keys():
        print(" key not present")

    return loggers[log_method]()
