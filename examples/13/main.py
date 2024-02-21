# This file explains how to log in Python
#
# Logging is a way to record events in a program
#
# For example:
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
# This will output the following:
# DEBUG:root:This will get logged
#
# You can also log to a file
# For example:
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This will get logged to a file')
# This will output the following:
# DEBUG:root:This will get logged to a file
#