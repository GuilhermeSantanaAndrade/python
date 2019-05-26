from Tabela import find, ValidationError
from Aluno import Aluno
from Professor import Professor
from Coordenador import Coordenador
from Disciplina import Disciplina, DisciplinaOfertada
from Matricula import SolicitacaoMatricula
       
class TableDoesntExists(Exception):
    pass

class Database:
    def __init__(self):
        self.Alunos = []
        self.Professores = []
        self.Coordenadores = []
        self.Disciplinas = []
        self.DisciplinasOfertadas = []
        self.Matriculas = []
        
    def locate(self, tabela, id):
        if type(tabela) is Aluno:
            out, idx = find(self.Alunos, id)
            return (out != None), idx, out
        elif type(tabela) is Professor:
            out, idx = find(self.Professores, id)
            return (out != None), idx, out
        elif type(tabela) is Coordenador:
            out, idx = find(self.Coordenadores, id)
            return (out != None), idx, out
        elif type(tabela) is Disciplina:
            out, idx = find(self.Disciplinas, id)
            return (out != None), idx, out
        elif type(tabela) is DisciplinaOfertada:
            out, idx = find(self.DisciplinasOfertadas, id)
            return (out != None), idx, out
        elif type(tabela) is SolicitacaoMatricula:
            out, idx = find(self.Matriculas, id)
            return (out != None), idx, out
        else:
            raise TableDoesntExists('Classe %s inexistente no Banco de Dados' %(type(tabela))) 
        
    def insert(self, obj):
        if type(obj) is Aluno:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe aluno com o ID informado')
            self.Alunos.append(obj)
        elif type(obj) is Professor:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe professor com o ID informado')
            self.Professores.append(obj)
        elif type(obj) is Coordenador:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe coordenador com o ID informado')            
            self.Coordenadores.append(obj)
        elif type(obj) is Disciplina:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe disciplina com o ID informado')
            self.Disciplinas.append(obj)
        elif type(obj) is DisciplinaOfertada:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe disciplina ofertada com o ID informado')
            self.DisciplinasOfertadas.append(obj)
        elif type(obj) is SolicitacaoMatricula:
            obj.validate()                
            if self.locate(obj, obj.id)[0]:
                raise ValidationError('Já existe matricula com o ID informado')
            self.Matriculas.append(obj)
        else:
            raise TableDoesntExists('Classe %s inexistente no Banco de Dados' %(type(obj))) 

    def delete(self, obj):
        out = self.locate(obj, obj.id)
        if type(obj) is Aluno:            
            if not out[0]:
                raise ValidationError('Não existe aluno com o ID informado')
            self.Alunos.pop(out[1])
        elif type(obj) is Professor:
            if not out[0]:
                raise ValidationError('Não existe professor com o ID informado')
            self.Professores.pop(out[1])
        elif type(obj) is Coordenador:
            if not out[0]:
                raise ValidationError('Não existe coordenador com o ID informado')
            self.Coordenadores.pop(out[1])
        elif type(obj) is Disciplina:
            if not out[0]:
                raise ValidationError('Não existe disciplina com o ID informado')
            self.Disciplinas.pop(out[1])
        elif type(obj) is DisciplinaOfertada:
            if not out[0]:
                raise ValidationError('Não existe disciplina ofertada com o ID informado')
            self.DisciplinasOfertadas.pop(out[1])
        elif type(obj) is SolicitacaoMatricula:
            if not out[0]:
                raise ValidationError('Não existe matricula com o ID informado')
            self.Matriculas.pop(out[1])
        else:
            raise TableDoesntExists('Classe %s inexistente no Banco de Dados' %(type(obj))) 

DB = Database()

while True:
    try:
        print('\n\n\n\nOpções (Digite e pressione ENTER): \n1 - Incluir \n2 - Excluir \n3 - Sair')
        value = input()
        aux = None
        
        if value == '1':
            print('\n\n\n\nINCLUIR - \n1 - Aluno \n2 - Professor \n3 - Coordenador \n4 - Disciplina \n5 - DisciplinaOfertada \n6 - Matricula  (Digite e pressione ENTER)')
            print('Digite os dados e pressione ENTER:')
            value2 = input()
            if value2 == '1':
                ent = Aluno()
                ent.id = input('ID:')
                ent.nome = input('NOME:')
                ent.validate()
                DB.insert(ent)
                print('Aluno incluído com sucesso!')
            elif value2 == '2':
                ent = Professor()
                ent.id = input('ID:')
                ent.nome = input('NOME:')
                ent.validate()
                DB.insert(ent)
                print('Professor incluído com sucesso!')
            elif value2 == '3':
                ent = Coordenador()
                ent.id = input('ID:')
                ent.nome = input('NOME:')
                ent.validate()
                DB.insert(ent)
                print('Coordenador incluído com sucesso!')
            elif value2 == '4':
                ent = Disciplina()
                ent.id = input('ID:')
                ent.nome = input('NOME:')
                ent.status = input('STATUS (1-ATIVA / 0-INATIVA):')
                ent.plano_insino = input('PLANO DE ENSINO:')
                ent.carga_horaria = input('CARGA HORARIA:')
                aux = input('ID DO COORDENADOR:')
                if not DB.locate(Coordenador(), aux)[0]:
                    raise ValidationError('Não existe coordenador com o ID informado') 
                ent.id_coordenador = aux            
                
                ent.validate()
                DB.insert(ent)
                print('Disciplina incluída com sucesso!')
            elif value2 == '5':
                ent = DisciplinaOfertada()
                ent.id = input('ID:')

                aux = input('ID DA DISCIPLINA:')
                if not DB.locate(Disciplina(), aux)[0]:
                    raise ValidationError('Não existe disciplina com o ID informado') 
                ent.id_disciplina = aux
                
                aux = input('ID DO PROFESSOR:')
                if not DB.locate(Professor(), aux)[0]:
                    raise ValidationError('Não existe professor com o ID informado') 
                ent.id_professor = aux
                
                ent.ano = input('ANO:')
                ent.semestre = input('SEMESTRE:')
                ent.turma = input('TURMA:')                
                ent.data = input('DATA:')

                ent.validate()
                DB.insert(ent)
                print('Disciplina ofertada incluída com sucesso!')
            elif value2 == '6':
                ent = SolicitacaoMatricula()
                ent.id = input('ID:')
                
                aux = input('ID DO ALUNO:')
                if not DB.locate(Aluno(), aux)[0]:
                    raise ValidationError('Não existe aluno com o ID informado') 
                ent.id_aluno = aux
                
                aux = input('ID DA MATRICULA:')
                if not DB.locate(SolicitacaoMatricula(), aux)[0]:
                    raise ValidationError('Não existe matricula com o ID informado') 
                ent.id_disciplina_ofertada = aux
                
                ent.dt_solicitacao = input('DATA SOLICITACAO:')
                
                aux = input('ID DO COORDENADOR:')
                if not DB.locate(Coordenador(), aux)[0]:
                    raise ValidationError('Não existe coordenador com o ID informado') 
                ent.id_coordenador = aux 
                ent.status = input('STATUS (1-SOLICITADO / 2-INDEFERIDO / 3-MATRICULADO / 4-DESISTENTE / 5-APROVADO / 6-REPROVADO):')

                ent.validate()
                DB.insert(ent)
                print('Matricula incluída com sucesso!')
            else:
                print('Opção inválida')
            print('----------------------------------------\n\n\n\n')
        elif value == '2':           
            print('\n\n\n\nEXCLUIR - \n1 - Aluno \n2 - Professor \n3 - Coordenador \n4 - Disciplina \n5 - DisciplinaOfertada \n6 - Matricula  (Digite e pressione ENTER)')
            print('Digite os dados e pressione ENTER:')
            value2 = input()
            if value2 == '1':
                ent = Aluno()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe aluno com o ID informado')
                DB.delete(out[2])
                print('Aluno excluído com sucesso!')
            elif value2 == '2':
                ent = Professor()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe professor com o ID informado')
                DB.delete(out[2])
                print('Professor excluído com sucesso!')
            elif value2 == '3':
                ent = Coordenador()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe Coordenador com o ID informado')
                DB.delete(out[2])
                print('Coordenador excluído com sucesso!')
            elif value2 == '4':
                ent = Disciplina()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe disciplina com o ID informado')
                DB.delete(out[2])
                print('Disciplina excluída com sucesso!')
            elif value2 == '5':
                ent = DisciplinaOfertada()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe Disciplina Ofertada com o ID informado')
                DB.delete(out[2])
                print('Disciplina Ofertada excluído com sucesso!')
            elif value2 == '6':
                ent = SolicitacaoMatricula()
                aux = input('ID:')
                
                out = DB.locate(ent, aux)
                if not out[0]:
                    raise ValidationError('Não existe Matricula Ofertada com o ID informado')
                DB.delete(out[2])
                print('Matricula excluída com sucesso!')
            else:
                print('Opção inválida')            
            
            
        elif value == '3':
            print('Aplicação finalizada...')
            break        
        else:
            print('Opção inválida!')
    except Exception as inst:
        print('**** ERRO: ', inst)
        print('\n\n\n\n')