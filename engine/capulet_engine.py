from engine.engine import Engine
class CapuletEngine(Engine):
    def __init__(self,current_milage,last_service_milage):
        self.current_milage=current_milage
        self.last_service_milage=last_service_milage

    def needs_service(self):
        return self.current_milage-self.last_service_milage>30000