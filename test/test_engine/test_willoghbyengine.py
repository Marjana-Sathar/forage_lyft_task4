import unittest
from engine.willoughby_engine import WilloughbyEngine

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 0
        current_mileage = 60002
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 0
        current_mileage = 50000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())