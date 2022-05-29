from email import generator
from typing import *
import genome
import csv
import os
import random

Population = NewType("Genome",object)

class Population():
    def __init__(self,name:str = '') -> None:
        if name == '':
            valid = False
            while not valid:
                for x in range(4):
                    name += chr(random.randint(65, 90))
                path = 'Populations\\' + self.name + '.csv'
                if not os.path.exists(path):
                    valid = True
        self.name = name
        self.generation = 0
        self.amount_of_genomes = 0
        self.genomes = []
    
    def generate_genomes(self,genomes:int,genes:int,max_input_index:int = None,max_output_index:int = None,max_inter_index:int = None) -> None:
        for x in range(genomes):
            self.genomes.append(genome.Genome(genes,max_input_index,max_output_index,max_inter_index))
    
    def save_generation(self) -> None:
        file = open('Populations\\' + self.name + '.csv','a')
        csv_writer = csv.writer(file, lineterminator='\n')
        csv_writer.writerow(self.genomes)

    def load_generation(self,generation_number:int) -> None:
        file = open('Populations\\' + self.name + '.csv','r')
        csv_reader = csv.reader(file, lineterminator='\n')
        self.genomes = csv_reader[generation_number]
        
    def mutate_population(self):
        for genome in self.genomes:
            genome.mutate_gene()