# #!/usr/bin/env python
#
# import logging
#
#
# #create logger
# logger = logging.getLogger("loksabha_members")
# logger.setLevel(logging.DEBUG)
#
# #create console logger and set level to error
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# #create file logger and set level to debug
# fh = logging.FileHandler("loksabha_members.log")
# fh.setLevel(logging.DEBUG)
#
# #create formatter
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(messages)s")
#
# #add formatter to file and console handlers
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# #add console and file to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# logger.debug("Debug Message")
# logger.info("info message")
# logger.warn("warning message")
# logger.error("error message")
# logger.critical("critical message")

# def singleton(cls):
#     instances={}
#     def get_instance():
#         if cls not in instances:
#             instances[cls]=cls()
#         return instances[cls]
#     return get_instance()
#
# @singleton
# class Logger:
#     def __init__(self,fname):
#         logging.config.fileConfig('logging.conf')
#         logging.basicConfig(filename=fname,filemode='a'
#                             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',datefmt='%H:%M:%S',
#                             level=logging.INFO)
#         self.logger.logging.getLogger('root')
