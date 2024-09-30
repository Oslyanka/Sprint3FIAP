# Sistema de Gerenciamento de Jogadores

Este projeto é uma aplicação em Python que gerencia jogadores e suas partidas, utilizando uma lista auto-ordenada pelos acertos totais e implementando busca binária para localizar jogadores com um número específico de acertos. A aplicação possui um menu interativo para adicionar jogadores, buscar por jogadores e sair do programa.

## Funcionalidades

1. **Adicionar Jogador**:
   - Permite adicionar um novo jogador com informações como ID, nome, curso e data de nascimento.
   - Também permite registrar múltiplas partidas para o jogador, armazenando dados como tempo de jogo, número de acertos, erros e data da partida.
   - O jogador é inserido em uma lista que é automaticamente ordenada pela quantidade total de acertos nas partidas.

2. **Buscar Jogador com X Pontos**:
   - Usa o algoritmo de busca binária para localizar um jogador que tenha exatamente o número de acertos especificado.
   - A busca é feita de maneira eficiente devido à lista ordenada.

3. **Saída**:
   - Permite encerrar a aplicação de forma segura.

## Estrutura do Código

- **Jogador**: Classe que representa um jogador, com ID, nome, curso e uma lista de partidas jogadas.
- **Partida**: Classe que armazena as informações de uma partida específica (ID, tempo de jogo, acertos, erros e data).
- **Funções Principais**:
  - `binary_search_jogador_mais_acertos`: Realiza busca binária para encontrar o jogador com uma certa quantidade de acertos.
  - `adicionar_jogador_ordenado`: Insere um jogador na lista de forma ordenada com base nos acertos.
  - `exibir_menu`: Menu interativo para adicionar e buscar jogadores, além de sair do programa.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado no sistema.

2. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

3. **Navegar até o Diretório**:
   ```bash
   cd seu_repositorio
   ```

4. **Executar o Programa**:
   ```bash
   python sprint3.py
   ```

## Exemplo de Uso

- **Adicionar um Jogador**:
  - Insira os dados do jogador (ID, nome, curso, data de nascimento).
  - Adicione quantas partidas desejar, com seus respectivos dados.

- **Buscar Jogador por Pontos**:
  - Informe a quantidade de acertos que deseja buscar.
  - O sistema retornará o jogador que tiver exatamente essa quantidade de acertos.
