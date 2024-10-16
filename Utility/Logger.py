import logging


class Logger:
    @staticmethod
    def log():
        logging.basicConfig(filename='./Logs/commerce.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)

       # logging.basicConfig(filename='C:/Learning/CommerceProject/Logs/commerce.log', level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info("Logger file created")
        return logger
