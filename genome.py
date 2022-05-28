from typing import *
import random


Genome = NewType("Genome",object)

class Genome():
    def __init__(self,number_of_genes:int,genes:List = None,max_input:int = 0,max_output:int = 0,max_inter:int = 0) -> None:
        
        self.number_of_genes = number_of_genes
        
        self.genes = []
        
        self.max_input = max_input
        self.max_output = max_output
        self.max_inter = max_inter
        
        if genes != None:
            self.genes = genes
        else:
            if max_input + max_inter + max_inter == 0:
                for x in range(number_of_genes):
                    gene = hex(random.randint(0,(16**8) - 1))
                    self.genes.append(gene.replace("0x", ""))
            else:
                for x in range(number_of_genes):
                    if max_input == 0:
                        max_input = 128
                    if max_output == 0:
                        max_output = 128
                    if max_inter == 0:
                        max_inter = 256
                        
                    strength = hex(random.randint(0,(16**4) - 1)).replace("0x", "")
                    possible_in_adr = list(range(self.max_input+1)) + list(range(128,self.max_inter+1))
                    in_adr = hex(random.choice(possible_in_adr)).replace("0x", "").zfill(2)
                    possible_out_adr = list(range(self.max_input+1)) + list(range(128,self.max_inter+1))
                    out_adr = hex(random.choice(possible_out_adr)).replace("0x", "").zfill(2)
                    gene = in_adr + strength + out_adr
                    self.genes.append(gene)
                   
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
print(Genome(4))
print(Genome(4,max_input=4,max_output=4,max_inter=256))