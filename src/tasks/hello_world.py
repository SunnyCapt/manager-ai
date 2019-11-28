from time import sleep

from src.settings import logger
from src.tasks.base import BaseTask


class HelloWorldTask(BaseTask):
    """Simple task example"""

    def run(self) -> None:
        """Task execution logic"""

        logger.info(f"Executes {self.name} task")
        sleep(1)
        self.notifier.notify("Hello World!")

        return None
