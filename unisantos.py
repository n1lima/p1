from typing import List
from xml.dom import ValidationErr

class Pessoa:
    def __init__(self, cpf: str, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def __str__(self):
        info = (f'CPF: {self.__cpf}\n'
                f'Nome: {self.__nome}\n')
        return info

class Aluno(Pessoa):
    def __init__(self, cpf: str, nome: str, matricula: int, nota:float):
        super().__init__(cpf, nome)
        self.__matricula = matricula
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def __str__(self):
        info = super().__str__()
        info += (f'Matricula: {self.__matricula}\n'
                 f'Nota: {self.__nota}\n')
        return info

class Professor(Pessoa):
    def __init__(self, cpf: str, nome: str, registro: int):
        super().__init__(cpf, nome)
        self.__registro = registro

    def __str__(self):
        info = super().__str__()
        info += (f'Registro do Professor: {self.__registro}\n')
        return info

class Disciplina:
    def __init__(self, cod: int, nome: str, prof: Professor, alunos: List[Aluno]):
        self.__cod = cod
        self.__nome = nome
        self.prof = prof
        self.__alunos = alunos

    def media_notas(self):
        sum = 0
        for alunos in self.__alunos:
            sum += alunos.get_nota()
        media = sum/len(self.__alunos)
        return media

    def get_cod(self):
        return self.__cod
    
    def __str__(self):
        info = (f'Codigo: {self.__cod}\n'
                f'Disciplina: {self.__nome}\n'
                f'Professor:\n{self.prof}\n'
                f'Media das Notas dos Alunos: {self.media_notas()}\n')
        return info

class Turma:
    def __init__(self, ano: int, semestre: int):
        self.__ano = ano
        self.__semestre = semestre
        self.__disciplinas: List[Disciplina] = []

    def add_disciplina(self, disciplina: Disciplina):
            for d in self.__disciplinas:
                if d.get_cod() == disciplina.get_cod():
                    raise ValidationErr ('Esse código já existe!')        
            self.__disciplinas.append(disciplina)
    
    def __str__(self):
        info = (f'Ano: {self.__ano}\n'
                f'Semestre: {self.__semestre}\n')
        for disciplina in self.__disciplinas:
            info += (f'{disciplina}\n')
        return info


