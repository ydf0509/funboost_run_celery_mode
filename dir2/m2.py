from funboost import BoosterParams, BrokerEnum


@BoosterParams(queue_name='c2_queue', broker_kind=BrokerEnum.CELERY, qps=2)
def f2(x):
    print(f'f2:{x}')
    return x * 2
