import random 
  
class Individual: 
    ''' 
    Class representando um indivídio da população.
    '''
    def __init__(self, chromosome, TARGET):
        self.TARGET = TARGET
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness()
  
    def cal_fitness(self): 
        ''' 
        Calcula o fittness score.
        O valor representa o número de caracteres errados.
        '''
        fitness = 0
        for gs, gt in zip(self.chromosome, self.TARGET): 
            if gs != gt: fitness+= 1
        return fitness 


class AG:
    '''
        Class representando o AG completo
    '''
    def __init__(self, POPULATION_SIZE, GENES, TARGET): 
        self.POPULATION_SIZE = POPULATION_SIZE # Número de indivíduos por geração
        self.GENES = GENES # Genes válidos
        self.TARGET = TARGET # Objetivo
        self.generation = 1 # Geração atual
        self.population = self._make_initial_population() # População
        
    def _make_initial_population(self):
        population = []
        ## 1. Cria a população inicial
        for i in range(self.POPULATION_SIZE): 
            gnome = self._create_gnome() 
            population.append(Individual(gnome, self.TARGET))
        return population

    def _mutated_genes(self): 
        ''' 
        Cria um gene para mutação.
        '''
        gene = random.choice(self.GENES) 
        return gene 
  
    def _create_gnome(self): 
        ''' 
        Cria um cromossomo.
        '''
        gnome_len = len(self.TARGET) 
        return [self._mutated_genes() for i in range(gnome_len)] 


    def mate(self, part1, par2): 
        ''' 
        Realiza o crossover/mutação e gera um novo indivíduo .
        '''
  
        # Cromossomos do filho
        child_chromosome = [] 
        for gp1, gp2 in zip(part1.chromosome, par2.chromosome):     
  
            # Probabilidade
            prob = random.random() 
  
            # Se prob for menor que 0.45, insere o gene do pai 1
            if prob < 0.45: 
                child_chromosome.append(gp1) 
            # Se prob estiver entre 0.45 e 0.90, insere o gene do pai 2
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
            # Caso contrário, realiza a mutação
            else: 
                child_chromosome.append(self._mutated_genes()) 
  
        return Individual(child_chromosome, self.TARGET)

    def run(self):
        ## 2. Enquanto não convergir
        while True:
            ## 2.1 Verifica se convergiu
            # Ordena a população pelo fitness score
            self.population = sorted(self.population, key = lambda x:x.fitness) 
            # Se um indivíduo convergir finaliza o processo
            if self.population[0].fitness <= 0:
                break

            ## 2.2 Gera uma nova população 
            new_generation = [] 

            # 10% da população passará a diante
            s = int((10*self.POPULATION_SIZE)/100) 
            new_generation.extend(self.population[:s]) 

            # 50% da população irá cruzar gerando novos filhos
            s = int((90*self.POPULATION_SIZE)/100) 
            for _ in range(s): 
                parent1 = random.choice(self.population[:50]) 
                parent2 = random.choice(self.population[:50]) 
                child = self.mate(parent1, parent2) 
                new_generation.append(child) 

            # Atualiza a população
            self.population = new_generation 

            print("Generation: %s String: %s Fitness: %s" % (
                self.generation, ''.join(self.population[0].chromosome),
                self.population[0].fitness)) 
            # Atualiza a geração
            self.generation += 1

        print("Generation: %s String: %s Fitness: %s" % (
            self.generation, ''.join(self.population[0].chromosome),
            self.population[0].fitness)) 