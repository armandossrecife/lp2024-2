# Exemplo de implementação de um cadastrado simplificado de alunos
# usando uma variável global para ser
# manipulada pelo programa em tempo de memória

# Dicionário para armazenar os alunos
alunos = {}

def matricula_valida(matricula):
  for caractere in matricula:
    if not caractere.isdigit():
      return False
  return True

# Função para inserir um novo aluno
def inserir_aluno():
  matricula = input("Digite a matrícula do aluno: ")

  # Faz a validação da formatacao da matricula
  while not matricula_valida(matricula):
    print("A matrícula deve conter apenas números (0..9)")
    matricula = input("Digite a matrícula do aluno: ")

  # Checa se a matricula ja existe
  while matricula in alunos:
    print('Matrícula já existe!')
    matricula = input("Digite a matrícula do aluno: ")

  nome = input("Digite o nome do aluno: ")
  curso = input("Digite o curso do aluno: ")
  sexo = input("Digite o sexo do aluno [Masculino/Feminino] (M/F): ")

  # Validar sexo
  while sexo not in ("M", "F"):
    sexo = input("Sexo inválido. Digite M para masculino ou F para feminino: ")

  # Adicionar o aluno ao dicionário
  alunos[matricula] = (nome, curso, sexo)
  print("Aluno cadastrado com sucesso!")

# Função para listar todos os alunos
def listar_alunos():
  if alunos:
    print("----------------------------------------")
    print("Lista de Alunos")
    print("----------------------------------------")
    for matricula, info in alunos.items():
      print(f"Matrícula: {matricula}, Nome: {info[0]}, Curso: {info[1]}, Sexo: {info[2]}")
  else:
    print("Nenhum aluno cadastrado.")

# Função para pesquisar aluno por matrícula
def pesquisar_aluno_matricula():
  matricula = input("Digite a matrícula do aluno a ser pesquisado: ")

  if matricula in alunos:
    dados_aluno = (matricula, alunos[matricula][0], alunos[matricula][1], alunos[matricula][2])
    print("----------------------------------------")
    print(f"Aluno encontrado:")
    print(f"Matrícula: {dados_aluno[0]}, Nome: {dados_aluno[1]}, Curso: {dados_aluno[2]}, Sexo: {dados_aluno[3]}")
    print("----------------------------------------")
  else:
    print("Aluno não encontrado.")

# Função para pesquisar aluno por nome
def pesquisar_aluno_nome():
  nome = input("Digite o nome do aluno a ser pesquisado: ")

  alunos_encontrados = []
  for matricula, info in alunos.items():
    if nome.lower() in info[0].lower():
      dados_aluno = (matricula, alunos[matricula][0], alunos[matricula][1], alunos[matricula][2])
      alunos_encontrados.append(dados_aluno)

  if alunos_encontrados:
    print("----------------------------------------")
    print(f"Alunos encontrados com o nome '{nome}':")
    print("----------------------------------------")
    for aluno in alunos_encontrados:
      print(f"Matrícula: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Sexo: {aluno[3]}")
  else:
    print("Aluno não encontrado.")

# Função para atualizar dados de um aluno existente
def atualiza_aluno():
  matricula = input("Digite a matrícula do aluno: ")

  if matricula in alunos:
    nome = input("Digite o novo nome do aluno: ")
    curso = alunos[matricula][1]
    sexo = input("Digite o sexo do aluno [Masculino/Feminino] (M/F): ")

    # Adicionar o aluno ao dicionário
    alunos[matricula] = (nome, curso, sexo)
    print("Aluno atualizado com sucesso!")
  else:
    print("Matrícula não existe!")

# Função para remover um aluno
def remover_aluno():
  matricula = input("Digite a matrícula do aluno a ser removido: ")

  if matricula in alunos:
    del alunos[matricula]
    print("Aluno removido com sucesso!")
  else:
    print("Aluno não encontrado.")

def menu_principal():
  print("#####################################")
  print("## Cadastro Simplificado de Alunos ##")
  print("#####################################")
  print("Opções:")
  print("1. Cadastrar aluno")
  print("2. Listar todos os alunos")
  print("3. Pesquisar aluno por matrícula")
  print("4. Pesquisar aluno por nome")
  print("5. Atualizar dados de um aluno")
  print("6. Remover aluno")
  print("7. SAIR")

# Chama o Menu principal
while True:
  menu_principal()
  opcao = input("Qual sua opção? ")
  if opcao=='1':
    inserir_aluno()
  elif opcao=='2':
    listar_alunos()
  elif opcao=='3':
    pesquisar_aluno_matricula()
  elif opcao=='4':
    pesquisar_aluno_nome()
  elif opcao=='5':
    atualiza_aluno()
  elif opcao=='6':
    remover_aluno()
  elif opcao=='7':
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida!")
