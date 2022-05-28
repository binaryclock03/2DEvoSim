from genome import Genome
from util import clamp
import random
import math

class Neuron():
    def __init__(self):
        self._address:int = 0
        self.value:float = 0
        self.incoming:list = []
    
    def set_address(self, address:int):
        self._address = clamp(address, 0, 255)

    def get_address(self):
        return self.address

    def activate(self, action="None"):
        pass

class InterNeuron(Neuron):
    def __init__(self):
        super().__init__(self)

    def activate(self, action="None"):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming))

class SensorNeuron(Neuron):
    def __init__(self):
        super().__init__(self)
    
    def activate(self, action="None"):
        if action == "Sensor":
            self.value = self.function

class ActionNeuron(Neuron):
    def __init__(self):
        super().__init__(self)
    
    def activate(self, action="None"):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming))
        if action == "Action" and random.random()<self.value:
            self.function()

class Connection():
    def __init__(self, gene):
        self.adr_a = int(gene[0:2], base=16)
        self.adr_b = int(gene[2:4], base=16)
        self.strength = int(gene[4:8], base=16)

class NeuralNet():
    def __init__(self):
        self.neurons:list = []
        self.connections:list = []
    
    def build_net(self, genome:Genome):
        for gene in genome.genes:
            self.connections.append(Connection(gene))
        
        for index in range(383):
            self.neurons.append(Neuron())

    def activate(self):
        for neuron in self.neurons:
            neuron.activate("Sensor")

        for connection in self.connections:
            adr_a = connection.adr_a
            adr_b = connection.adr_b
            if adr_b < 128:
                adr_b += 256

            value = self.neurons[adr_a].value
            value = value * connection.strength
            self.neurons[adr_b].incoming.append(value)
            
        for neuron in self.neurons:
            neuron.activate("Sum")

        for neuron in self.neurons:
            neuron.activate("Activate")