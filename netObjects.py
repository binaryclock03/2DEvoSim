from genome import Genome
from util import clamp, scale
import random
import math
import copy

class Neuron():
    def __init__(self):
        self._address:int = 0
        self.value:float = 0
        self.incoming:list = []
        self.incoming_last:list =[]
        self.incoming_next:list = []
        self.depth:int = None
    
    def set_address(self, address:int):
        self._address = clamp(address, 0, 384)

    def get_address(self):
        return self._address

    def activate(self, creature, simulation, action):
        pass

class InterNeuron(Neuron):
    def __init__(self):
        super().__init__()

    def activate(self, creature, simulation, action):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming)+sum(self.incoming_last))
            self.incoming = []
        if action == "Action":
            self.incoming_last = self.incoming_next.copy()
            self.incoming_next = []

class SensorNeuron(Neuron):
    def __init__(self, function):
        super().__init__()
        self.function =  function
        self.depth:int = 0
    
    def activate(self, creature, simulation, action):
        if action == "Sensor":
            self.value = self.function(creature, simulation)

class ActionNeuron(Neuron):
    def __init__(self, pos_function, neg_function):
        super().__init__()
        self.pos_function =  pos_function
        self.neg_function =  neg_function
    
    def activate(self, creature, simulation, action):
        if action == "Sum":
            self.value = math.tanh(sum(self.incoming)+sum(self.incoming_last))
            self.incoming = []
        if action == "Action" and random.random()<abs(self.value):
            if self.value > 0:
                self.pos_function(self, creature, simulation)
            else:
                self.neg_function(self, creature, simulation)
            self.incoming_last = self.incoming_next
            self.incoming_next = []

class Connection():
    def __init__(self, gene):
        self.adr_a = int(gene[0:2], base=16)
        self.adr_b = int(gene[2:4], base=16)
        self.strength = scale(int(gene[4:8], base=16), 0, 65535, -4.0, 4.0)

class NeuralNet():
    def __init__(self):
        self.neurons:dict = {}
        self.connections:list = []
        self.max_depth:int = 1
    
    def build_net(self, genome:Genome):
        for gene in genome.genes:
            self.connections.append(Connection(gene))
        
        for index in range(384):
            neuron = Neuron()
            neuron.set_address(index)
            self.neurons.update({index:neuron})
    
    def insert_neuron(self, index:int, neuron:Neuron):
        self.neurons[index] = copy.copy(neuron)

    def optimize(self):
        valid_neurons = self.check_paths()
        for index in range(len(self.neurons)):
            if not(index in valid_neurons):
                del self.neurons[index]
        
        todel = []
        for x, connection in enumerate(self.connections):
            adr_a = connection.adr_a
            adr_b = connection.adr_b
            if adr_b < 128:
                adr_b += 256

            if not(adr_a in valid_neurons) or not(adr_b in valid_neurons):
                todel.append(x)
        
        todel.sort(reverse=True)
        for i in todel:
            del self.connections[i]
        
        for key in self.neurons.keys():
            if self.max_depth < self.neurons[key].depth:
                self.max_depth = self.neurons[key].depth
        #self.max_depth += 1

    def activate(self, creature, simulation):
        for key in self.neurons:
            self.neurons[key].activate(creature, simulation, "Sensor")

        for i in range(self.max_depth):
            for connection in self.connections:
                adr_a = connection.adr_a
                adr_b = connection.adr_b
                if adr_b < 128:
                    adr_b += 256

                value = self.neurons[adr_a].value
                value = value * connection.strength
                if self.neurons[adr_a].depth >= self.neurons[adr_b].depth:
                    self.neurons[adr_b].incoming_next.append(value)
                    #print(f"backcon adr_a {adr_a} d {self.neurons[adr_a].depth} adr_b {adr_b} d {self.neurons[adr_b].depth}")
                else:
                    self.neurons[adr_b].incoming.append(value)
                
            for key in self.neurons:
                self.neurons[key].activate(creature, simulation, "Sum")

        for key in self.neurons:
            self.neurons[key].activate(creature, simulation, "Action")
    
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
                    if self.neurons[connection.adr_b+256].depth == None or self.neurons[connection.adr_b+256].depth < neuron.depth + 1:
                        self.neurons[connection.adr_b+256].depth = neuron.depth + 1
                    
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