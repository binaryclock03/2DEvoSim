import time
from genome import Genome
import netObjects as nt
import multiprocessing as mp

def testSensor():
    return 1

def testAction(self):
    #print(self._address)
    pass

if __name__ == "__main__":
    genome = Genome(100, max_inter=0)
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
    for index in range(1000):
        brain.activate()
    end = time.time()
    print(f"time elapsed {end-start}")