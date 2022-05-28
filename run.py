import time
from genome import Genome
import netObjects as nt
import display

def testSensor():
    return 1

def testAction(self):
    print(self._address)

if __name__ == "__main__":
    genome = Genome(10, max_input=10, max_output=10, max_inter=5)
    brain = nt.NeuralNet()
    brain.build_net(genome)

    for index in range(127):
        neuron = nt.SensorNeuron(testSensor)
        neuron.set_address(index)
        brain.insertNeuron(index, neuron)

    for index in range(127):
        neuron = nt.ActionNeuron(testAction)
        neuron.set_address(index+256)
        brain.insertNeuron(index+256, neuron)

    start = time.time()
    for index in range(1):
        brain.activate()
    end = time.time()
    print(f"time elapsed {end-start}")

    display.run(brain, max_input=10, max_output=10, max_inter=5)