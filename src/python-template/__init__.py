import logging

temp_logger = logging.getLogger()
console_handler = logging.StreamHandler()

temp_logger.setLevel(logging.INFO)
temp_logger.addHandler(console_handler)
