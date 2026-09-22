# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Crie um jogo da Forca em Python para praticar manipulação de strings, uso de listas, laços de repetição e tomada de decisões com base na entrada do usuário.

## 📝 Tasks

### 🛠️ Seleção da Palavra

#### Descrição
Crie uma lista com palavras predefinidas e escolha uma delas aleatoriamente para iniciar o jogo.

#### Requisitos
O programa concluído deve:

- Armazenar pelo menos 5 palavras em uma lista.
- Selecionar uma palavra aleatória para o jogo.
- Converter a palavra para um formato de progresso visível, como `_ _ _ _`.

### 🛠️ Adivinhando Letras

#### Descrição
Permita que o jogador insira letras e atualize o estado da palavra escondida conforme as respostas forem corretas ou incorretas.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra ao usuário com `input()`.
- Verificar se a letra está presente na palavra secreta.
- Mostrar o progresso atual da palavra após cada tentativa.
- Informar quando a letra for repetida ou inválida.

### 🛠️ Controle de Tentativas e Fim de Jogo

#### Descrição
Implemente a lógica para contar erros, encerrar o jogo ao final e exibir mensagens de vitória ou derrota.

#### Requisitos
O programa concluído deve:

- Acompanhar a quantidade de vidas ou tentativas restantes.
- Diminuir o contador quando a letra for incorreta.
- Encerrar o jogo quando a palavra for completamente revelada.
- Encerrar o jogo quando o jogador exceder o número máximo de erros.
- Exibir uma mensagem final clara para vitória ou derrota.