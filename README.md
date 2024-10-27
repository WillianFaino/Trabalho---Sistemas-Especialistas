## AnimalGuess - Sistema Especialista

**Código:** O código Python apresentado cria um sistema de inferência baseado em regras para adivinhar o nome de um animal com base em suas características. Ele utiliza a biblioteca `experta` para definir as regras e realizar a inferência.

**Funcionalidades:**

* **Instalação da biblioteca `termcolor`:** Verifica se a biblioteca está instalada e a instala caso necessário, para permitir a impressão de texto colorido na saída.
* **Conversão de respostas:** A função `tof` converte as respostas do usuário (S/N) em valores booleanos (True/False) para facilitar o processamento.
* **Definição de características:** A classe `caracts` define as características que serão utilizadas para identificar os animais.
* **Regras de inferência:** As regras são definidas como métodos da classe `SE_AnimalGuess`, relacionando as características com os nomes dos animais.
* **Interface do usuário:** O código interage com o usuário para coletar as informações sobre o animal e, em seguida, utiliza o mecanismo de inferência para apresentar o resultado.

**README Sugerido:**

## Sistema de Inferência para Identificação de Animais

**Descrição:**

Este sistema Python, desenvolvido utilizando a biblioteca `experta`, é capaz de identificar o nome de um animal com base em suas características. O usuário fornece informações sobre o animal, como presença de pelo, capacidade de voar, habitat, etc., e o sistema, através de um conjunto de regras pré-definidas, tenta determinar o animal mais provável.

**Funcionalidades:**

* **Base de conhecimento:** Possui uma base de conhecimento com diversas espécies de animais e suas respectivas características.
* **Inferência:** Utiliza um mecanismo de inferência baseado em regras para deduzir o nome do animal.
* **Interface amigável:** Interage com o usuário de forma simples e intuitiva, solicitando informações sobre as características do animal.
* **Saída colorida:** Utiliza a biblioteca `termcolor` para destacar o resultado final.

**Como usar:**

1. **Executar o código:** Execute o script Python.
2. **Responder às perguntas:** O sistema fará perguntas sobre as características do animal. Responda com "S" para sim e "N" para não.
3. **Resultado:** O sistema exibirá o nome do animal que mais se encaixa nas características informadas.

**Tecnologias utilizadas:**

* **Python:** Linguagem de programação utilizada para desenvolver o sistema.
* **Biblioteca `experta`:** Biblioteca Python para sistemas de produção.
* **Biblioteca `termcolor`:** Biblioteca Python para imprimir texto colorido no terminal.

**Observações:**

* A base de conhecimento de animais pode ser facilmente expandida, adicionando novas regras e características.
* O sistema pode ser aprimorado com a implementação de uma interface gráfica para facilitar a interação do usuário.
* A precisão das respostas depende da qualidade e quantidade das regras definidas.

**Exemplo de uso:**

```
Você possui a biblioteca 'Termcolor' instalada? (S/N)
S

O animal possui pelagem? (S/N)
S
O animal possui penas? (S/N)
N
...
```

**Considerações Adicionais:**

* **Melhorias:** Poderíamos adicionar uma função para permitir que o usuário adicione novas espécies de animais à base de conhecimento.
* **Documentação:** Aumentar a documentação dentro do código, explicando cada função e classe de forma mais detalhada.
* **Testes:** Implementar testes unitários para garantir a qualidade do código e evitar regressões.
* **Interface gráfica:** Criar uma interface gráfica usando bibliotecas como Tkinter ou PyQt para tornar a interação mais amigável.
