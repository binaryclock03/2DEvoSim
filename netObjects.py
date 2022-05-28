from genome import Genome
from util import clamp
import random
import math

class Neuron():
    def __init__(self):
        self._address:int = 0
        self.value:float = 0
        self.incoming:list = []
        self.depth:int = None
    
    def set_address(self, address:int):
        self._address = clamp(address, 0, 384)

    def get_address(self):
        return self._address

    def activate(self, action):
        pass

class InterNeuron(Neuron):
    def __init__(self):
        super().__init__()

    def activate(self, action):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming))

class SensorNeuron(Neuron,):
    def __init__(self, function):
        super().__init__()
        self.function =  function
    
    def activate(self, action):
        if action == "Sensor":
            self.value = self.function()

class ActionNeuron(Neuron):
    def __init__(self, function):
        super().__init__()
        self.function =  function
    
    def activate(self, action):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming))
        if action == "Action" and random.random()<self.value:
            self.function(self)

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
        
        for index in range(384):
            neuron = Neuron()
            neuron.set_address(index)
            self.neurons.append(neuron)
    
    def insertNeuron(self, index:int, neuron:Neuron):
        self.neurons[index] = neuron

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
            neuron.activate("Action")
    
    def _check_path(self,index:int,to_return:set = set(),depth:int = 0,valid:set = set()) -> set:
        if depth == 0:
            to_return = set()
        neuron = self.neurons[index]
        
        # Checks neuron already has a depth if it needs to be overwritten
        if neuron.depth == None:
            neuron.depth = depth
        elif depth < neuron.depth:
            neuron.depth = depth
        end = True
        for connection in self.connections:
            current_path = set()
            # Checks if connection is from current neuron               no touch #and not (connection.adr_b in to_return or connection.adr_b + 256 in to_return)
            if connection.adr_a == index :
                end = False
                if connection.adr_b < 128: #Check if next neuron is an action neuron                       
                    current_path.add(connection.adr_b+256)
                elif connection.adr_b in valid:
                    current_path.add(connection.adr_b)
                elif (connection.adr_a != connection.adr_b) and (self.neurons[connection.adr_b].depth == None or 
                    self.neurons[connection.adr_b].depth > neuron.depth): #Check if next interneuron is self and if its depth is lower
                    current_path = self._check_path(connection.adr_b,to_return,depth+1,valid)      #Check path of next neuron
                
                if current_path != set(): #Checks if theres anything to add
                    current_path.add(index)
                    to_return.update(current_path)
            # Check for backwards connections
            elif self.neurons[connection.adr_b].depth != None and connection.adr_a == index and self.neurons[connection.adr_b].depth < neuron.depth: 
                to_return.add(index)
        if end:
            return set()
        else:
            return to_return     
    
    def check_paths(self) -> set:
        active_adrs = set()
        for connection in self.connections:
            if connection.adr_a < 128:
                active_adrs.update(set(self._check_path(connection.adr_a,valid=active_adrs)))
        return active_adrs