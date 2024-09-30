# Representa um jogador com ID, nome, curso, data de nascimento e suas partidas jogadas.
class Jogador:
    def __init__(self, id_usuario, nome, curso, data_nasc):
        self.id_usuario = id_usuario
        self.nome = nome
        self.curso = curso
        self.data_nasc = data_nasc
        self.partidas = []  # Lista de partidas do jogador
    
    def gerar_partida(self, partida):
        self.partidas.append(partida)
    
    def total_acertos(self):
        return sum(partida.qnt_acertos for partida in self.partidas)  # Soma os acertos de todas as partidas
    
    def __repr__(self):
        return f"Jogador(ID: {self.id_usuario}, Nome: {self.nome}, Curso: {self.curso}, Data de Nascimento: {self.data_nasc})"

# Representa uma partida com ID, tempo, acertos, erros e data.
class Partida:
    def __init__(self, id_partida, tempo_jogo, qnt_acertos, qnt_erros, data):
        self.id_partida = id_partida
        self.tempo_jogo = tempo_jogo
        self.qnt_acertos = qnt_acertos
        self.qnt_erros = qnt_erros
        self.data = data
    
    def __repr__(self):
        return (f"Partida(ID: {self.id_partida}, Tempo: {self.tempo_jogo}, Acertos: {self.qnt_acertos}, "
                f"Erros: {self.qnt_erros}, Data: {self.data})")

# Busca binária para encontrar jogador com uma certa quantidade de acertos.
def binary_search_jogador_mais_acertos(jogadores, acertos_alvo):
    low, high = 0, len(jogadores) - 1
    while low <= high:
        mid = (low + high) // 2
        total_acertos = jogadores[mid].total_acertos()
        
        if total_acertos == acertos_alvo:
            return jogadores[mid]  # Encontrado
        elif total_acertos < acertos_alvo:
            low = mid + 1  # Busca na metade superior
        else:
            high = mid - 1  # Busca na metade inferior
    return None  # Não encontrado

# Adiciona jogador à lista e a mantém ordenada pelos acertos.
def adicionar_jogador_ordenado(jogadores, jogador):
    jogadores.append(jogador)
    jogadores.sort(key=lambda x: x.total_acertos())  # Ordena por acertos totais

# Menu interativo para adicionar e buscar jogadores.
def exibir_menu():
    jogadores = []  # Lista de jogadores
    
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Jogador")
        print("2. Buscar Jogador com X Pontos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            id_usuario = int(input("Digite o ID do Jogador: "))
            nome = input("Digite o Nome do Jogador: ")
            curso = input("Digite o Curso do Jogador: ")
            data_nasc = input("Digite a Data de Nascimento (YYYY-MM-DD): ")
            
            novo_jogador = Jogador(id_usuario, nome, curso, data_nasc)
            
            while True:
                add_partida = input("Deseja adicionar uma partida? (s/n): ").lower()
                if add_partida == 's':
                    id_partida = int(input("Digite o ID da Partida: "))
                    tempo_jogo = input("Digite o tempo de jogo (ex: 30:00): ")
                    qnt_acertos = int(input("Digite a quantidade de acertos: "))
                    qnt_erros = int(input("Digite a quantidade de erros: "))
                    data = input("Digite a data da partida (YYYY-MM-DD): ")
                    
                    nova_partida = Partida(id_partida, tempo_jogo, qnt_acertos, qnt_erros, data)
                    novo_jogador.gerar_partida(nova_partida)
                else:
                    break
            
            adicionar_jogador_ordenado(jogadores, novo_jogador)
            print(f"Jogador {novo_jogador.nome} adicionado com sucesso!")

        elif escolha == "2":
            if not jogadores:
                print("Nenhum jogador cadastrado ainda.")
            else:
                pontos_alvo = int(input("Digite a quantidade de acertos a ser buscada: "))
                jogador_encontrado = binary_search_jogador_mais_acertos(jogadores, pontos_alvo)
                
                if jogador_encontrado:
                    print(f"Jogador encontrado: {jogador_encontrado}")
                else:
                    print(f"Nenhum jogador encontrado com {pontos_alvo} acertos.")

        elif escolha == "3":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
exibir_menu()
