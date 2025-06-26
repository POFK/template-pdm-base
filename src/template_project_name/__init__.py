from loguru import logger

logger.add(
    "template_project_name.log",
    rotation="50 MB",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)
