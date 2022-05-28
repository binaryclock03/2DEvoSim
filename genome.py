from typing import *
import random


Genome = NewType("Genome",object)

class Genome():
    def __init__(self,number_of_genes:int,genes:List = None,) -> None:
        
        self.number_of_genes = number_of_genes
        
        self.genes = []
        
        if genes != None:
            self.genes = genes
        else:
            for x in range(number_of_genes):
                gene = hex(random.randint(0,(16**8)-1))
                self.genes.append(gene.replace("0x", ""))
        
    def __str__(self) -> str:
        output_str = ''
        for gene in self.genes:
            output_str += (str(gene)) + ' '
        return output_str

    def get_gene(self,index:int) -> str:
        return self.genes[index]
    
    def set_gene(self,index:int,gene:str) -> None:
        if index < len(self.genes) and index >= 0:
            self.genes[index] = gene

    def mutate_gene(self,index:int = None) -> Genome:
        if index == None:
            index = random.randint(0,len(self.genes)-1)
        gene = self.genes[index]
        new_gene = ''
        base_to_change = random.randint(0,7)
        for base in range(8):
            if base == base_to_change:
                new_gene += hex(random.randint(0,15)).replace("0x", "")
            else:
                new_gene += gene[base]
        new_genes = self.genes
        new_genes[index] = new_gene
        return Genome(self.number_of_genes,new_genes)