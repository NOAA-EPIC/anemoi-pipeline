import logging
import logging.config

DEFAULT_LEVEL = logging.INFO

LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "plain": {
            "format": "[%(name)s][%(levelname)s][%(asctime)s][%(pathname)s:%(lineno)d][%(process)d][%(thread)d]: %(message)s"
        },
    },
    "handlers": {
        "default": {
            "formatter": "plain",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters": [],
        },
    },
    "loggers": {
        "anemoi-pipeline": {
            "handlers": ["default"],
            "level": DEFAULT_LEVEL,
        },
    },
}


def init_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)


init_logging()
LOGGER = logging.getLogger("anemoi-pipeline")
