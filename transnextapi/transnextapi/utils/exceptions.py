from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
import logging

logger = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc:  本次请求发生的异常信息
    :param context:  本次请求发送异常的执行上下文
    :return:
    """
    response = exception_handler(exc, context)

    if response is None:
        view = context["view"]
        if isinstance(exc, DatabaseError):
            logger.error('[%s] %s', (view, exc))
            response = Response({'message': '服务器内部错误'},status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
