import time
from genome import Genome
import simulation as sim
import functions as f
import display

if __name__ == "__main__":
    simulation = sim.Simulation()

    sensor_neurons = f.sensor_neurons
    action_neurons = f.action_neurons

    for i in range(1,11):
        genome = Genome(1, genes=["0000ffff"])
        creature = sim.Creature(i)
        creature.build_from_genome(genome)
        creature.add_io_neurons(sensor_neurons, action_neurons)
        creature.finalize()
        simulation.add_to_sim(creature)
    
    print("before")
    print(simulation.get_creature_position(1))
    print(simulation.get_creature_position(2))
    
    for i in range(2):
        simulation.simulate()
    
    print("after")
    print(simulation.get_creature_position(1))
    print(simulation.get_creature_position(2))


    # start = time.time()
    # brain.activate(None)
    # end = time.time()
    # print(f"time elapsed {end-start}")

    # start = time.time()
    # end = time.time()
    # print(f"time elapsed {end-start}")
    
    #display.run(brain)