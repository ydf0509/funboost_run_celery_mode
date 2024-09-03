from celery.schedules import crontab
from datetime import timedelta
from funboost import BoostersManager, BoosterParams, BrokerEnum
from funboost.assist.celery_helper import CeleryHelper


@BoosterParams(queue_name='c3_queueb', broker_kind=BrokerEnum.CELERY, )
def f3(a,b):
    print(f'f3 a:{a} b:{b}')


beat_schedule = {  # 这是100% 原汁原味的celery 定时任务配置方式
    'add-every-10-seconds_job': {
        'task': f3.queue_name,
        'schedule': timedelta(seconds=10),
        'args': (10000, 20000),
    },
    'celery_beat_crontab': {
        'task': f3.queue_name,
        'schedule': crontab(minute=30, hour=18),
        'kwargs': {'a': 20, 'b': 30}
    }
}

if __name__ == '__main__':
    CeleryHelper.celery_start_beat(beat_schedule) # 启动定时发布任务
    f3.push(a=666,b=888)
    CeleryHelper.realy_start_celery_worker(worker_concurrency=300,start_consume_queue_name_list=[f3.queue_name]) # 启动work消费。
