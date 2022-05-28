from util import clamp
class BaseNeuron():
    def __init__(self):
        _address:int
        _strength:float
    
    def set_address(self, address:int):
        self._address = clamp(address, 0, 255)

    def get_address(self):
        return self.address
    
    def set_strength(self, strength:float):
        self._strength = clamp(strength, -4.0, 4.0)

    def get_strength(self):
        return self._strength
class InterNeuron(BaseNeuron):
    def __init__(self):
        super().__init__(self)
    
    def calc_incoming():
        pass

class IONeuron(BaseNeuron):
    def __init__(self):
        super().__init__(self)
        self.function: function

class SensorNeuron(IONeuron):
    def __init__(self):
        super().__init__(self)
    
    def read_sensor(self):
        pass

class ActionNeuron(IONeuron, InterNeuron):
    def __init__(self):
        super().__init__(self)
    
    def preform_action():
        pass
