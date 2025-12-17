
# A simple Flask application that logs all incoming requests to a file named 'my_file.log'.
# It logs the HTTP method, request path, and response status code.
# The log format includes the timestamp, log level, and message.
# Example log entry: "2024-06-01 12:00:00,000 - INFO - GET / 200"
# Required packages: Flask, logging
# To run the application, use the command: flask run
# Make sure to set the FLASK_APP environment variable to 'module3/saeed_module3_5.py'.
from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('my_file.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@app.after_request
def log_request(response):
    logger.info(f"{request.method} {request.path} {response.status_code}")
    return response

@app.route('/')
def hello():
    return 'Hello, World!'

