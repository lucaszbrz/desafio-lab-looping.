📚 Calculadora de Médias – Desafio do 1º Semestre

Este é um programa em Python desenvolvido como desafio no meu primeiro semestre de faculdade.
O objetivo era praticar laços de repetição, tratamento de exceções e condicionais para processar notas de alunos e calcular suas médias.

🎯 Objetivo do Programa

O programa:

Lê as notas de 3 avaliações (C1, C2 e C3) de 10 alunos.

Calcula a média de cada aluno.

Indica se o aluno foi aprovado ou se precisa de avaliação final.

Conta quantos alunos foram aprovados sem ressalvas (média ≥ 7).

📝 Funcionalidades

Entrada de notas com validação:

O programa verifica se a entrada é um número (float).

Se o usuário digitar algo inválido, ele solicita novamente.

Cálculo de média:

Média = (C1 + C2 + C3) / 3

Condição de aprovação:

Média ≥ 7: aprovado sem ressalvas.

Média < 7: precisa fazer avaliação final:

Média ponderada: 60% da média original + 40% da avaliação final.

Resultado final decide aprovação ou reprovação.

Contador de alunos aprovados sem ressalvas:

Ao final, o programa imprime quantos alunos passaram diretamente.

💻 Exemplo de Uso
Informe a nota da C1: 8
Informe a nota da C2: 7.5
Informe a nota da C3: 9
Aluno 1, sua média é 8.17
Aprovado sem ressalvas.

Informe a nota da C1: 4
Informe a nota da C2: 5
Informe a nota da C3: 6
Aluno 2, sua média é 5.00
Informe a nota da avaliação final: 7
Aprovado

Quantidade de alunos que passou sem ressalvas foi 1

🛠️ Tecnologias Usadas

Linguagem: Python 3.x

Conceitos aplicados:

Laços de repetição (for)

Condicionais (if/else)

Tratamento de exceções (try/except)

Entrada de dados (input)

Operações matemáticas básicas

🔧 Como Rodar

Certifique-se de ter o Python 3.x instalado.

Salve o código em um arquivo notas_alunos.py.

Execute no terminal:

python notas_alunos.py


Siga as instruções na tela para inserir as notas.

📈 Melhorias Futuras

Permitir que o número de alunos seja dinâmico (não fixo em 10).

Adicionar validação de notas válidas (entre 0 e 10).

Armazenar resultados em arquivo CSV para consultas futuras.

Criar um relatório final com médias e status de todos os alunos.

🏆 Conclusão

Este programa foi uma excelente prática de controle de fluxo e tratamento de erros, habilidades essenciais no início da jornada em programação.
