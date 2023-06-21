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
## Procedimentos realizados:
* Seleção e pré-processamento de Dados
  * Limpeza de dados
  * Balanceamento de dados
* Normalização e redução de dados
  * Implementação do min-max e z-score
  * PCA
  * Avaliação dos principais componentes
* Análise descritiva de dados
  * Distribuição de frequência
  * Técnicas de visualização de dados
  * Medidas resumo
* Análise de grupos
  * Algoritmo K-means
  * Algoritmo GMM
  * Avaliação da qualidade dos agrupamentos
* Classificação
  * Árvore de Decisão (*Decision Tree*)
  * KNN (*K-Nearest Neighbors*)
  * SVM (*Support Vectors Machine*)
  * Rede Neural MLP (Multilayer Perceptron)
  * Técnicas de divisão de base:
    * Holdout (TReinamento 70% e Teste 30%)
    * Cross-Validation (k=10)
  * Métricas
    * Matrix de confusão
    * Acurácia
    * F1 Score
  * Comparação final
---
## Todos os procedimentos e seus resultados podem ser vistos em [projeto.ipynb](./projeto.ipynb)