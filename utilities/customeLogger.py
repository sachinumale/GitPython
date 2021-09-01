import logging

class loGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log", datefmt="%H_%M_%S_%d_%m_%y")
        logger =logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
