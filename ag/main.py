from ag import AG

# Número de indivíduos por geração
POPULATION_SIZE = 100
  
# Genes válidos
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}''' # 88 caracteres
  
# Objetivo
TARGET = "I love ICOM" # 11 caracteres

# Por análise combinatória: n ^ m = 4.390927778387004e+91

ag = AG(POPULATION_SIZE, GENES, TARGET)
ag.run()
