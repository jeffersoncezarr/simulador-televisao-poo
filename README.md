📺 Simulador de TV & Controle Remoto


🚀 Sobre o Projeto
O projeto busca simular a interação entre objetos do mundo real. Neste caso, a pilha alimenta o controle remoto, que por sua vez é responsável por gerenciar e realizar os comandos da televisão. Vale ressaltar que a televisão pode ser operada tanto por meio do controle remoto quanto diretamente.


🛠️ Conceitos Aplicados
- Associação entre classes: A classe ControleRemoto consome a energia da Pilha para alterar o estado da instância da classe Televisao.
- Encapsulamento: Utilização de atributos privados para proteger o estado interno dos objetos, evitando alterações diretas indesejadas.
- Getters e Setters (@property): Uso de métodos validadores para garantir que os valores atribuídos respeitem as regras e requisitos do sistema.


📚 Fontes de Estudo e Inspiração
A realização deste projeto foi inspirada no conteúdo dos meus veículos de estudos atuais:

Cursos:
Python 3 - Mundo 3 / POO — Curso em Vídeo (Prof. Gustavo Guanabara)
Programação em Python do Básico ao Avançado — Geek University (Udemy)
Livro:
Introdução à Programação com Python: Algoritmos e Lógica de Programação para Iniciantes — Nilo Ney Coutinho Menezes


📂 Estrutura do projeto:
|-> __main__.py | Responsável pelo loop principal do projeto, permitindo ao usuário interagir com os objetos
|--> televisao.py | Responsável pelo molde dos objetos de televisão, com lógica para alterar canais, volume e estado (ligado/desligado)
|---> controle_remoto.py | Responsável por conectar os comandos à televisão
|----> pilha.py | Responsável por fornecer energia ao controle remoto
