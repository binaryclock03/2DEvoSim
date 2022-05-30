import netObjects as nt
import simulation as sim
import util

#sensors
# def testSensor(creature, simulation):
#     return 1

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

#actions
# def testAction(self, creature, simulation):
#     print(f"TEST ACTION")

def move_x(self, creature, simulation):
    if self.value < 0:
        simulation.move_creature(creature.id, -1, 0)
    else:
        simulation.move_creature(creature.id, 1, 0)

def move_y(self, creature, simulation):
    if self.value < 0:
        simulation.move_creature(creature.id, 0, -1)
    else:
        simulation.move_creature(creature.id, 0, 1)

sensor_neurons = []
#sensor_neurons.append(nt.SensorNeuron(testSensor))
sensor_neurons.append(nt.SensorNeuron(get_y_pos))
sensor_neurons.append(nt.SensorNeuron(get_x_pos))

action_neurons = []
action_neurons.append(nt.ActionNeuron(move_x, move_x))
action_neurons.append(nt.ActionNeuron(move_y, move_y))