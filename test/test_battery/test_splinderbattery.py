from datetime import date
import unittest
from battery.spindler_battery import SpindlerBattery

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2021-08-07")
        current_date = date.fromisoformat("2024-08-09")
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2022-08-07")
        current_date = date.fromisoformat("2023-08-06")
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())