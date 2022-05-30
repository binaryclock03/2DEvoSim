import netObjects as nt
import simulation as sim
import util
import math
import random

#sensors
def always_on(creature, simulation):
    return 1

def always_off(creature, simulation):
    return 0

def get_y_pos(creature, simulation):
    y_pos = simulation.get_creature_position(creature.id)[1]
    y_bound = simulation.grid_bounds[1]
    output = util.scale(y_pos,0,y_bound,-1,1)
    return output

def get_x_pos(creature, simulation):
    x_pos = simulation.get_creature_position(creature.id)[0]
    x_bound = simulation.grid_bounds[0]
    output = util.scale(x_pos,0,x_bound,-1,1)
    return output

def get_y_dist(creature,simulation):
    y_pos = simulation.get_creature_position(creature.id)[1]
    y_bound = simulation.grid_bounds[1]
    output = util.scale(y_pos,0,y_bound,0,1)
    return output

def get_x_dist(creature,simulation):
    x_pos = simulation.get_creature_position(creature.id)[0]
    x_bound = simulation.grid_bounds[0]
    output = util.scale(x_pos,0,x_bound,0,1)
    return output

def oscillator(creature, simulation):
    return math.sin(simulation.tick*math.pi*0.25)
    
#actions
def move_random(self, creature, simulation):
    x = random.randrange(-1,1)
    y = random.randrange(-1,1)
    simulation.move_creature(creature.id, x, y)

def move_x(self, creature, simulation):
    if self.value < 0:
        simulation.move_creature(creature.id, -1, 0)
        creature.dir = 2
    else:
        simulation.move_creature(creature.id, 1, 0)
        creature.dir = 0

def move_y(self, creature, simulation):
    if self.value < 0:
        simulation.move_creature(creature.id, 0, -1)
        creature.dir = 3
    else:
        simulation.move_creature(creature.id, 0, 1)
        creature.dir = 1



sensor_neurons = []
sensor_neurons.append(nt.SensorNeuron(always_on))
sensor_neurons.append(nt.SensorNeuron(always_off))
sensor_neurons.append(nt.SensorNeuron(get_y_pos))
sensor_neurons.append(nt.SensorNeuron(get_x_pos))
sensor_neurons.append(nt.SensorNeuron(get_y_dist))
sensor_neurons.append(nt.SensorNeuron(get_x_dist))
sensor_neurons.append(nt.SensorNeuron(oscillator))

action_neurons = []
action_neurons.append(nt.ActionNeuron(move_random, move_random))
action_neurons.append(nt.ActionNeuron(move_x, move_x))
action_neurons.append(nt.ActionNeuron(move_y, move_y))

neuron_name_dict = {
    0:"always on",
    1:"always off",
    2:"get y pos",
    3:"get x pos",
    4:"get y dist",
    5:"get x dist",
    6:"oscillator",
    256:"move rand",
    257:"move x",
    258:"move y"
}