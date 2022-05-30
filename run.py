import time
from genome import Genome
import simulation as sim
import functions as f
#import display
import population as pop

if __name__ == "__main__":


    sensor_neurons = f.sensor_neurons
    action_neurons = f.action_neurons
    
    #Initialize Population
    population = pop.Population("6")
    population.generate_genomes(250,4,2,2,1)
    population.save_generation()
    
    for gen in range(1000):
        start = time.time()
        simulation = sim.Simulation()
        
        for i in range(250):
            creature = sim.Creature(i+1)
            creature.build_from_genome(population.genomes[i])
            creature.add_io_neurons(sensor_neurons, action_neurons)
            creature.finalize()
            simulation.add_to_sim(creature)

        for x in range(200):
            simulation.simulate()

        survivors = []

        for creep in simulation.creatures:
            if simulation.get_creature_position(creep.id)[1] < 16:
                survivors.append(creep.genome)
        
        print(len(survivors))
        population.new_generation(survivors,0.01)
        
        end = time.time()
        print(f"time elapsed {end-start}")
        
        print("Generation: " +  str(gen))
    
    # start = time.time()
    # 
    # end = time.time()
    # print(f"time elapsed {end-start}")

    # start = time.time()
    # end = time.time()
    # print(f"time elapsed {end-start}")
    
    #display.run(brain)
