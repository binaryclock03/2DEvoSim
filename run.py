import time
from genome import Genome
import netObjects as nt
import display

def testSensor():
    return 1

def testAction(self):
    print(f"TEST ACTION REPORT: {self._address}")

if __name__ == "__main__":
    genome = Genome()

    genome = Genome(15, max_input_index=4, max_output_index=4, max_inter_index=4)
    brain = nt.NeuralNet()
    brain.build_net(genome)

    for index in range(127):
        neuron = nt.SensorNeuron(testSensor)
        neuron.set_address(index)
        brain.insertNeuron(index, neuron)

    for index in range(127):
        neuron = nt.ActionNeuron(testAction, testAction)
        neuron.set_address(index+256)
        brain.insertNeuron(index+256, neuron)
    
    brain.optimize()

    start = time.time()
    brain.activate()
    end = time.time()
    print(f"time elapsed {end-start}")

    # start = time.time()
    # end = time.time()
    # print(f"time elapsed {end-start}")
    
    display.run(brain)