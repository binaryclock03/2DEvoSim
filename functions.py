import netObjects as nt

#sensors
def testSensor(simulation):
    return 1

#actions
def testAction(self, simulation):
    print(f"TEST ACTION")

def move_x(self, simulation):
    if self.value < 0:
        simulation.move_creature(1, -1, 0)
    else:
        simulation.move_creature(1, 1, 0)

sensor_neurons = []
sensor_neurons.append(nt.SensorNeuron(testSensor))

action_neurons = []
action_neurons.append(nt.ActionNeuron(move_x, move_x))