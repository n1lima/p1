from unisantos import *

aluno1 = Aluno(436474, 'nicoly', 873443, 10)
aluno2 = Aluno(4343574, 'haru', 948543, 9.30)

lista_alunos = [aluno1, aluno2]

professor1 = Professor(498548, 'thi', 87347)
professor2 = Professor(48948, 'ku', 87847)

disciplina1 = Disciplina(77, 'POO', professor1, lista_alunos)
disciplina2 = Disciplina(78, 'IHC', professor2, lista_alunos)

turma = Turma(2024, 4)
turma.add_disciplina(disciplina1)
turma.add_disciplina(disciplina2)

print(turma)
