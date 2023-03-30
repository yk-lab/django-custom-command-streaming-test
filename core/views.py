import subprocess
from logging import getLogger

from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

logger = getLogger(__name__)


def run_process_as_generator(*args, **kwargs):
    """
    サブプロセス結果をジェネレータで返す。
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.STDOUT)

    popen = subprocess.Popen(*args, **kwargs)

    while True:
        line = popen.stdout.readline()
        if line:
            yield line

        if not line and popen.poll() is not None:
            break


def task():
    """
    バッチを実行
    """
    command = 'python3 ./manage.py long_time_job'
    return run_process_as_generator(
        command,
        shell=True,
    )


@csrf_exempt
@require_POST
def stream_logs(request):
    return StreamingHttpResponse(
        task(),
        content_type='text/plain',
    )


@csrf_exempt
@require_POST
def non_stream_logs(request):
    return HttpResponse(
        task(),
        content_type='text/plain',
    )
