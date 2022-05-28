from genome import Genome
import netObjects as nt

genome = Genome(4)
brain = nt.NeuralNet()
brain.build_net(genome)
brain.activate()