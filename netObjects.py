from genome import Genome
from util import clamp

class Neuron():
    def __init__(self):
        self._address:int
        self.strength:float
    
    def set_address(self, address:int):
        self._address = clamp(address, 0, 255)

    def get_address(self):
        return self.address
    
class InterNeuron(Neuron):
    def __init__(self):
        super().__init__(self)
    
    def calc_incoming():
        pass

class IONeuron(Neuron):
    def __init__(self):
        super().__init__(self)
        self.function: function

class SensorNeuron(IONeuron):
    def __init__(self):
        super().__init__(self)
    
    def read_sensor(self):
        self.strength = self.function

class ActionNeuron(IONeuron, InterNeuron):
    def __init__(self):
        super().__init__(self)
    
    def preform_action(self):
        self.function()

class Connection():
    def __init__(self, gene):
        self.adr_a = int(gene[0:2], base=16)
        self.adr_b = int(gene[2:4], base=16)
        self._strength = int(gene[4:8], base=16)
        

class NeuralNet():
    def __init__(self):
        self.sensorNeurons:list = []
        self.actionNeurons:list = []
        self.connections:list = []
    
    def build_net(self, genome:Genome):
        for gene in genome.genes:
            self.connections.append(Connection(gene))

    def activate_sensors(self):
        for sensorNeuron in self.sensorNeurons:
            sensorNeuron.read_sensor()
    
    def activate_actions(self):
        for actionNeuron in self.actionNeurons:
            actionNeuron.preform_action()