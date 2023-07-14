from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self,current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
