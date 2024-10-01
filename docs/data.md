## Manipulação de Data e Hora em Python: 

**O módulo `datetime` é a ferramenta principal em Python para trabalhar com datas e horas.** Ele oferece uma variedade de classes e funções para criar, modificar e comparar datas e horas de forma precisa.

https://docs.python.org/3/library/datetime.html

### Classes Principais

* **`date`:** Representa uma data (ano, mês, dia).
* **`time`:** Representa um horário (hora, minuto, segundo, microsegundo).
* **`datetime`:** Combina data e hora em um único objeto.
* **`timedelta`:** Representa um intervalo de tempo.

### Funcionalidades Básicas

* **Criando objetos:**
  ```python
  import datetime

  # Criando uma data
  data_hoje = datetime.date.today()

  # Criando um horário
  horario_agora = datetime.datetime.now().time()

  # Criando um datetime específico
  data_nascimento = datetime.datetime(1990, 1, 15)
  ```
* **Formatando datas e horas:**
  ```python
  data_formatada = data_hoje.strftime("%d/%m/%Y")  # 15/03/2024
  ```
* **Operações aritméticas:**
  ```python
  # Adicionando 10 dias a uma data
  nova_data = data_hoje + datetime.timedelta(days=10)
  ```
* **Comparando datas e horas:**
  ```python
  if data1 > data2:
      # ...
  ```
* **Extraindo componentes:**
  ```python
  ano = data_hoje.year
  mes = data_hoje.month
  dia = data_hoje.day
  ```
  **Dia da semana**
  ```python
  dia_semana = data_hoje.weekday()

  # funcao para mostrar o dia da semana: 
  def dia_da_semana(dia_semana):
    if dia_semana == 0:
      return 'segunda-feira'
    elif dia_semana == 1:
      return 'terça-feira'
    elif dia_semana == 2:
      return 'quarta-feira'
    elif dia_semana == 3:
      return 'quinta-feira'
    elif dia_semana == 4:
      return 'sexta-feira'
    elif dia_semana == 5: 
      return 'sabado-feira'
    elif dia_semana == 6: 
      return 'domingo'

  print(f"{dia}/{mes}/{ano} - {dia_da_semana(dia_semana)}")

  ```

### Funcionalidades Avançadas

* **Fusos horários:** O módulo `pytz` oferece suporte a fusos horários.
* **Localizando datas:** Encontrar a próxima ocorrência de um dia da semana, por exemplo.
* **Parseando strings de data e hora:** Convertendo strings em objetos `datetime`.
* **Calculando diferenças entre datas:** Calculando a idade de uma pessoa, por exemplo.

### Exemplos Práticos

* **Calculando a idade de uma pessoa:**
  ```python
  from datetime import date

  def calcular_idade(data_nascimento):
      hoje = date.today()
      return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

  data_nasc = date(1990, 1, 15)
  idade = calcular_idade(data_nasc)
  print(idade)
  ```
* **Formatando datas para relatórios:**
  ```python
  from datetime import datetime

  data_hora = datetime.now()
  data_formatada = data_hora.strftime("%A, %d de %B de %Y - %H:%M:%S")
  print(data_formatada)
  ```

### Por que usar o módulo `datetime`?

* **Precisão:** Garante cálculos precisos de datas e horas.
* **Flexibilidade:** Permite uma ampla variedade de operações.
* **Facilidade de uso:** A sintaxe é intuitiva e bem documentada.

**Em resumo,** o módulo `datetime` é uma ferramenta essencial para qualquer desenvolvedor Python que precise lidar com datas e horas em seus projetos. Com ele, você pode realizar desde tarefas simples como formatar datas até cálculos complexos envolvendo fusos horários e intervalos de tempo.
