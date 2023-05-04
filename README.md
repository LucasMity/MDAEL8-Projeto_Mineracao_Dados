# MDAEL8-Projeto_Mineracao_Dados
 Projeto desenvolvido durante a disciplina de Mineração de dados no curso de Engenharia de Computação do IFSP BRI.

---
# Base de dados "Loan Data Set"

A base de dados ["Loan Data Set"](https://www.kaggle.com/datasets/mirzahasnine/loan-data-set?resource=download) está relacionada a concessão de crédito ou empréstimo mobiliário para uma pessoa de acordo com algumas características apresentadas por ela.

Dessa forma a base possui os seguintes 11 atributos:

* **Gender** - "Male" ou "Female".
* **Married** - "Yes" ou "No".
* **Dependents** - 0, 1, 2 ou 3+.
* **Education** - "Graduate" ou "Not Graduate".
* **Self_Employed** - "Yes" ou "No".
* **Applicant_Income** - Um valor inteiro, representando a renda do requerente.
* **Coapplicant_Income** - Um valor inteiro, representando a renda do co-requerente.
* **Loan_Amount** - Um valor inteiro, representando o valor do empréstimo.
* **Term** - Um valor inteiro, representando o prazo (em meses) para quitar o empréstimo.
* **Credit_History** - 1 ou 0, checa se a pessoa possui um histórico de quitação de dívida.
* **Area** - "Rural", "Semiurban" ou "Urban", área do imóvel que o requerente quer o empréstimo.

E, por fim, temos o atributo de rótulo:
* **Status** - "Y" ou "N", empréstimo aceito ou negado.

---
# Pré-processamento de Dados
## Limpeza de dados
A base de dados apresenta alguns dados faltantes, como segue a tabela:

Atributo|Dados Faltantes
---|---
Gender|13
Married|3
Dependents|15
Education|0
Self_Employed|32
Applicant_Income|0
Coapplicant_Income|0
Loan_Amount|0
Term|14
Credit_History|50
Area|0
Status|0

A fim de completar os dados faltantes, foi utilizado o método de **moda**.

## Colunas categóricas para numéricas
Para melhor manipular e analisar os dados da base de dados, foram convertidas as colunas categóricas para numéricas:
Coluna|Valor Categórico|Valor Numérico
---|---|---
Gender|  "Female", "Male"| 1, 0
Married|  "Yes", "No"| 1, 0
Dependents|  0, 1, 2, 3+| 0, 1, 2, 3
Education|  "Graduate", "Not Graduate"| 1, 0
Self_Employed| "Yes", "No"| 1, 0
Area|  "Rural", "Urban", "Semiurban"| 0, 1, 2
Status| "Y" ou "N"| 1, 0

---
## Normalização e redução de dados

---
# Análise descritiva de dados
## Visualização
## Medidas
---

# A fazer

* Balanceamento de base
* Validação cruzada
