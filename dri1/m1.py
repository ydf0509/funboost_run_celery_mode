from funboost import BoosterParams, BrokerEnum


@BoosterParams(queue_name='c1_queue', broker_kind=BrokerEnum.CELERY, qps=1)
def f1(x):
    print(f'f1:{x}')
    return x * 1
