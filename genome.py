from operator import index
from typing import *
import random


Genome = NewType("Genome",object)

class Genome():
    def __init__(self,number_of_genes:int,max_input_index:int = None,max_output_index:int = None,max_inter_index:int = None,genes:List = None) -> None:
        
        self.number_of_genes = number_of_genes
        
        self.genes = []
        
        self.max_input_index = max_input_index
        self.max_output_index = max_output_index
        self.max_inter_index = max_inter_index
        
        if genes != None:
            self.genes = genes
        else:
            if max_input_index == None and max_output_index == None and max_inter_index == None:
                for x in range(number_of_genes):
                    gene = hex(random.randint(0,(16**8) - 1))
                    self.genes.append(gene.replace("0x", "").zfill(8))
            else:
                for x in range(number_of_genes):  
                    strength = hex(random.randint(0,(16**4) - 1)).replace("0x", "").zfill(4)
                    possible_in_adr = list(range(self.max_input_index)) + (list(range(128,self.max_inter_index+128)))
                    in_adr = hex(random.choice(possible_in_adr)).replace("0x", "").zfill(2)
                    possible_out_adr = list(range(self.max_output_index)) + (list(range(128,self.max_inter_index+128)))
                    out_adr = hex(random.choice(possible_out_adr)).replace("0x", "").zfill(2)
                    gene = in_adr + out_adr + strength
                    self.genes.append(gene)
                   
    def __str__(self,separator:str = ' ') -> str:
        output_str = ''
        for gene in self.genes:
            output_str += (str(gene) + separator)     
        return output_str.strip(' ')

    def get_gene(self,index:int) -> str:
        return self.genes[index]
    
    def set_gene(self,index:int,gene:str) -> None:
        if index < len(self.genes) and index >= 0:
            self.genes[index] = gene

    def mutate_gene(self,index_of_gene:int = None) -> Genome:
        if index_of_gene == None:
            index_of_gene = random.randint(0,len(self.genes)-1)
        gene = self.genes[index_of_gene]
        new_gene = ''
        base_to_change = random.randint(0,7)
        for base in range(8):
            if base == base_to_change:
                new_gene += hex(random.randint(0,15)).replace("0x", "").zfill(1)
            else:
                new_gene += gene[base]
        new_genes = self.genes.copy()
        new_genes[index_of_gene] = new_gene
        return Genome(self.number_of_genes,genes = new_genes)
    
    def mutate_gene_but_better(self,index_of_gene:int = None) -> str:
        if index_of_gene == None:
            index_of_gene = random.randint(0,len(self.genes)-1)
        to_change = random.randint(0,2)
        if to_change == 0:
            possible_in_adr = list(range(self.max_input_index)) + (list(range(128,self.max_inter_index+128)))
            in_adr = hex(random.choice(possible_in_adr)).replace("0x", "").zfill(2)
            new_gene = in_adr + self.genes[index_of_gene][2:]

        elif to_change == 1:
            possible_out_adr = list(range(self.max_output_index)) + (list(range(128,self.max_inter_index+128)))
            out_adr = hex(random.choice(possible_out_adr)).replace("0x", "").zfill(2)
            new_gene = self.genes[index_of_gene][0:2] + out_adr + self.genes[index_of_gene][4:]
        else:
            strength = hex(random.randint(0,(16**4) - 1)).replace("0x", "").zfill(4)
            new_gene = self.genes[index_of_gene][0:4] + strength
        return new_gene
            
            
    
    def gene_bit_flip(self,index_of_gene:int = None) -> str:
        if index_of_gene == None:
            index_of_gene = random.randint(0,len(self.genes)-1)
        gene = bin(int('0x'+self.genes[index_of_gene],16))
        while len(gene) < 34:
            gene = gene.replace('0b','0b0')
        new_gene = '0b'
        binary_base_to_flip = random.randint(0,31)
        for base in range(32):
            if base == binary_base_to_flip:
                if gene[base+2] == '1':
                    new_gene += '0'
                else:
                    new_gene += '1'
            else:
                new_gene += gene[base+2]
        new_gene = hex(int(new_gene,0)).replace('0x','').zfill(8)
        return new_gene
    
    def mutate_genome(self,mutation_rate:float) -> Genome:
        new_genes = []
        for gene in range(len(self.genes)):
            if random.random() < mutation_rate:
                new_genes.append(self.mutate_gene_but_better(gene))
            else:
                new_genes.append(self.genes[gene])
        self.genes = new_genes
        
    def copy(self) -> Genome:
        return Genome(self.number_of_genes,self.max_input_index,self.max_output_index,self.max_inter_index,genes = self.genes)

