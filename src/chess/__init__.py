import logging
import logging.config

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s | [%(levelname)s] | %(name)s | %(message)s",
            },
        },
        "handlers": {
            "default": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": "DEBUG", "propagate": True},
            "pychess": {"handlers": ["default"], "level": "DEBUG", "propagate": False},
        },
    }
)

logger = logging.getLogger(__name__)
logger.debug("Initialised Chess Library")
