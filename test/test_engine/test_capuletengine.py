import unittest
from engine.capulet_engine import CapuletEngine

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 0
        current_mileage = 30002
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 0
        current_mileage = 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


