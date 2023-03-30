import time
from logging import getLogger

from django.core.management.base import BaseCommand
from django.utils import timezone

logger = getLogger(__name__)


class Command(BaseCommand):
    help = 'My Awesome Command.'

    def handle(self, *args, **options):
        logger.info('Job started.')
        for _ in range(12):
            # logger.info(timezone.localtime())
            print(timezone.localtime(), flush=True)
            time.sleep(10)
        logger.info('Job done.')
