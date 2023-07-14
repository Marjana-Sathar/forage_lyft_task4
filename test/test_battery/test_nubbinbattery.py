from datetime import date
import unittest
from battery.nubbin_battery import NubbinBattery

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2010-08-07")
        current_date = date.fromisoformat("2014-08-09")
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2022-08-07")
        current_date = date.fromisoformat("2023-08-06")
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())