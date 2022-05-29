import netObjects as nt
import random as rand

class Simulation():
    def __init__(self):
        self.grid_bounds = (16, 16)
        self.grid = [[0]*self.grid_bounds[0] for i in range(self.grid_bounds[1])]
        self.creatures:list = []
    
    def add_to_sim(self, creature):
        creature.simulation = self
        while True:
            x = rand.randrange(0, self.grid_bounds[0])
            y = rand.randrange(0, self.grid_bounds[1])
            if self.grid[x][y] == 0:
                break
        self.grid[x][y] = creature.id
        self.creatures.append(creature)

    def get_creature_position(self, id):
        for x, row in enumerate(self.grid):
            try:
                y = row.index(id)
                return (x,y)
            except:
                pass
        print(f"creature with id:{id} not found")

    def move_creature(self, id, dx, dy):
        x, y = self.get_creature_position(id)
        # print(f"x{x} y{y}")
        try:
            if self.grid[x+dx][y+dy] == 0:
                self.grid[x][y] = 0
                self.grid[x+dx][y+dy] = id
        except:
            # print("tried to move creature out of bounds")
            pass
    
    def simulate(self):
        for creature in self.creatures:
            creature.simulate()

class Creature():
    def __init__(self, id):
        self.id = id
        self.brain = None
        self.genome = None
        self.simulation = None

    def simulate(self):
        self.brain.activate(self, self.simulation)
        pass

    def build_from_genome(self, genome):
        self.genome = genome
        self.brain = nt.NeuralNet()
        self.brain.build_net(self.genome)
        pass

    def add_io_neurons(self, sensor_neurons, action_neurons):
        for i, neuron in enumerate(sensor_neurons):
            self.brain.insert_neuron(i, neuron)
        
        for i, neuron in enumerate(action_neurons):
            self.brain.insert_neuron(i+256, neuron)
    
    def finalize(self):
        self.brain.optimize()