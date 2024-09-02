
from funboost import BoosterParams, BrokerEnum
from funboost.assist.celery_helper import CeleryHelper
from dir2.m2 import f2
from dri1 import m1




@BoosterParams(queue_name='c4_queue', broker_kind=BrokerEnum.CELERY, qps=1)
def f4(x):
    print(f'f4:{x}')
    return x * 4

if __name__ == '__main__':
    for i in range(1000):
        m1.f1.push(i)
        f2.delay(i)
        f4.push(i)
    CeleryHelper.realy_start_celery_worker(worker_concurrency=300, is_start_consume_all_queues=True)
