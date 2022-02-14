from django.test import TestCase
from django_rq import get_worker, get_queue
from fakeredis import FakeStrictRedis
from rq import Queue
# Create your tests here.
from check_printer.models import Check, Printer
from check_printer.service.create_check import create_checks

test_data = {
    "id": 123456,
    "price": 780,
    "items": [
        {
            "name": "Вкусная пицца",
            "quantity": 2,
            "unit_price": 250
        },
        {
            "name": "Не менее вкусные роллы",
            "quantity": 1,
            "unit_price": 280
        }
    ],
    "address": "г. Уфа, ул. Ленина, д. 42",
    "client": {
        "name": "Иван",
        "phone": 9173332222
    },
    "point_id": 1
}


class CheckTestCase(TestCase):
    def setUp(self):
        # создаем принтеры
        Printer.objects.create(name='Printer 1', api_key='zzqwe99', check_type='kitchen', point_id=1)
        Printer.objects.create(name='Printer 2', api_key='zzzz3499', check_type='client', point_id=1)
        Printer.objects.create(name='Printer 3', api_key='zzrtez3499', check_type='kitchen', point_id=2)
        Printer.objects.create(name='Printer 4', api_key='jghjtez3499', check_type='client', point_id=2)
        # TODO: add fake redis and Queue
        # self.queue =Queue(is_async=False, connection=FakeStrictRedis())
        # job = queue.enqueue(my_long_running_job)
        # assert job.is_finished

    def test_create(self):
        """ """

        # get_worker().work(burst=True)  # Processes all jobs then stop.
        self.assertEqual(create_checks(test_data), (True, 'Чеки успешно созданы'))
