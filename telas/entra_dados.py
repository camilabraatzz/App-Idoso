from pessoa import Pessoa


def EntraDados():
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento')
    pessoa = Pessoa(nome, data_nascimento)
    return pessoa.getNome(), pessoa.getDataNascimento()


print(EntraDados())