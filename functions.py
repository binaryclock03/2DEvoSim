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

def get_x_pos(creature, simulation):
    x_pos = simulation.get_creature_position(creature.id)[0]
    x_bound = simulation.grid_bounds[0]
    output = util.scale(x_pos,0,x_bound,-1,1)
    return output

def get_y_pos(creature, simulation):
    y_pos = simulation.get_creature_position(creature.id)[1]
    y_bound = simulation.grid_bounds[1]
    output = util.scale(y_pos,0,y_bound,-1,1)
    return output

def get_x_dist(creature,simulation):
    x_pos = simulation.get_creature_position(creature.id)[0]
    x_bound = simulation.grid_bounds[0]
    output = util.scale(x_pos,0,x_bound,0,1)
    return output

def get_y_dist(creature,simulation):
    y_pos = simulation.get_creature_position(creature.id)[1]
    y_bound = simulation.grid_bounds[1]
    output = util.scale(y_pos,0,y_bound,0,1)
    return output

def oscillator(creature, simulation):
    return math.sin(simulation.tick*math.pi*0.25)
    
#actions
def do_nothing():
    pass

def move_x(self, creature, simulation):
    if creature.delta[0] == 0:
        if self.value < 0:
            delta = simulation.move_creature(creature.id, -1, 0)
            if delta != [0,0]:
                creature.dir[0] = -1
        else:
            delta = simulation.move_creature(creature.id, 1, 0)
            if delta != [0,0]:
                creature.dir[0] = 1
        creature.delta = delta

def move_y(self, creature, simulation):
    if creature.delta[1] == 0:
        if self.value < 0:
            delta = simulation.move_creature(creature.id, 0, -1)
            if delta != [0,0]:
                creature.dir[1] = -1
        else:
            delta = simulation.move_creature(creature.id, 0, 1)
            if delta != [0,0]:
                creature.dir[1] = 1
        creature.delta = delta
        
def move_fwd(self,creature,simulation):
    if creature.delta == [0,0]:
        dir = creature.dir
        if self.value < 0:
            delta = simulation.move_creature(creature.id, -1*dir[0], -1*dir[1])
        else:
            delta = simulation.move_creature(creature.id, dir[0], dir[1])
        creature.delta = delta
    
def move_rnd(self,creature,simulation):
    delta_target = [random.randint(-1,1),random.randint(-1,1)]
    if creature.delta == [0,0]:
        if self.value < 0:
            delta = simulation.move_creature(creature.id, -1*delta_target[0], -1*delta_target[1])
            creature.dir = delta
        else:
            delta = simulation.move_creature(creature.id, delta_target[0], delta_target[1])
            creature.dir = delta
        creature.delta = delta



sensor_neurons = []
sensor_neurons.append(nt.SensorNeuron(always_on))
sensor_neurons.append(nt.SensorNeuron(always_off))
sensor_neurons.append(nt.SensorNeuron(get_x_pos))
sensor_neurons.append(nt.SensorNeuron(get_y_pos))
sensor_neurons.append(nt.SensorNeuron(get_x_dist))
sensor_neurons.append(nt.SensorNeuron(get_y_dist))
sensor_neurons.append(nt.SensorNeuron(oscillator))

action_neurons = []
action_neurons.append(nt.ActionNeuron(move_x, move_x))
action_neurons.append(nt.ActionNeuron(move_y, move_y))
action_neurons.append(nt.ActionNeuron(move_fwd, move_fwd))
action_neurons.append(nt.ActionNeuron(move_rnd, move_rnd))

neuron_name_dict = {
    0:"always on",
    1:"always off",
    2:"cbias x",
    3:"cbias y",
    4:"pos x",
    5:"pos y",
    6:"age",
    256:"do_nothing",
    257:"move x",
    258:"move y",
    259:"move rand",
    260:"move FB",
    261:"move RL"
}