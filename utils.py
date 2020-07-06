from models import Pessoas, Usuarios

#Inserção dados na tabela.
def insere_pessoas():
    pessoa = Pessoas(nome='TiagoSsa', idade=45)
    print(pessoa)
    pessoa.save()

#Consulta dados da tabela.
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    print(pessoa.idade)

#Altera dados da tabela.
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Santos').first()
    pessoa.nome = 'Ssa'
    pessoa.save()

#Exclui dados da tabela.
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ssa').first()
    pessoa.delete()

#Inserir Ususarios:
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

#Consulta todos os Usuarios:
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__=='__main__':
    insere_usuario('tiago', '1234')
    insere_usuario('silva', '4321')
    consulta_pessoas()
    #insere_pessoas()
    #alterar_pessoa()
    #exclui_pessoa()
