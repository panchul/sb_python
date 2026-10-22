import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"
)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


## adding a custom logger with a stream handler

logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))

logger.addHandler(handler)
logger.info("Application started")

logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")
logger.debug("This is a debug message") ## !!! won't see it because of the logging level set to INFO
logger.info("This is an info message")
