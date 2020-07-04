from models import Pessoas

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


if __name__=='__main__':
    #insere_pessoas()
    #alterar_pessoa()
    #exclui_pessoa()
    consulta_pessoas()