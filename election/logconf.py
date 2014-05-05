import logging.config

def singleton(cls):
    instances={}
    def get_instance():
        if cls not in instances:
            instances[cls]=cls()
        return instances[cls]
    return get_instance()

@singleton
class Logger:
    def __init__(self,fname):
        logging.config.fileConfig('logging.conf')
        logging.basicConfig(filename=fname,filemode='a'
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',datefmt='%H:%M:%S',
                            level=logging.INFO)
        self.logger.logging.getLogger('root')

        
        
