class biblioteca:
    
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):  
        self.livros.append(livro)  
        print(f'O livro "{livro.titulo}" foi adicionado a Biblioteca')

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f'Livro "{titulo}" removido da biblioteca.')
                return
        print(f'Livro "{titulo}" não encontrado.')
    
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None
    
    def listar_livros(self):
        if not self.livros:
            print('A biblioteca está vazia.')
        else:
            print("\nLista de livros na biblioteca:")
            for livro in self.livros:
                print(livro.titulo.upper())  # Transforma o título do livro em maiúsculas

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.ano})'

def exibir_menu():
    print("\nMenu da Biblioteca")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro")
    print("4. Listar Todos os Livros")
    print("5. Sair")
    return input("Selecione uma opção: ")

def main():
    biblioteca_instancia = biblioteca()
    
    biblioteca_instancia.adicionar_livro(Livro("Dom Quixote", "Miguel de Cervantes", 1605))
    biblioteca_instancia.adicionar_livro(Livro("Orgulho e Preconceito", "Jane Austen", 1813))
    biblioteca_instancia.adicionar_livro(Livro("1984", "George Orwell", 1949))
    biblioteca_instancia.adicionar_livro(Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967))
    biblioteca_instancia.adicionar_livro(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943))
    biblioteca_instancia.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954))
    biblioteca_instancia.adicionar_livro(Livro("A Menina que Roubava Livros", "Markus Zusak", 2005))
    biblioteca_instancia.adicionar_livro(Livro("O Código Da Vinci", "Dan Brown", 2003))
    biblioteca_instancia.adicionar_livro(Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997))
    
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano de publicação: "))  # Convertendo para int
            novo_livro = Livro(titulo, autor, ano)  # Criando uma instância de livro
            biblioteca_instancia.adicionar_livro(novo_livro)  # Adicionando o novo livro à biblioteca
        elif opcao == '2':
            titulo = input("Título do livro a ser removido: ")
            biblioteca_instancia.remover_livro(titulo)
        elif opcao == '3':
            titulo = input("Título do livro a ser buscado: ")
            livro = biblioteca_instancia.buscar_livro(titulo)
            if livro:
                print(f'Livro encontrado: {livro}')
            else:
                print(f'Livro "{titulo}" não encontrado.')
        elif opcao == '4':
            biblioteca_instancia.listar_livros()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
