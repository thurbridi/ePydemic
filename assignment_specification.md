# ePydemic - Especificação do Projeto
**Trabalho de Implementação 1 para INE5425@UFSC**

## Requisitos Funcionais
1. Implementar o autômato celular para simulação de epidemias segundo a dissertação (G. MELOTTI, 2009). O projeto deve apresentar resultados similares aos apresentados na dissertação.
2. Mostrar estatísticas ao final da execução
    - Tempo de simulação
    - Série temporal com o número de células por tipo (infectado, suscetível, recuperado) a cada instânte da simulação
3. Configurar o tamanho da área simulada (número de indivíduos) através da interface gráfica.
4. Configurar os parâmetros do autômato através da interface gráfica (probabilidades, infecciosidade da doença, proporção de infectados iniciais)

## Requisitos Não-Funcionais
1. Utilizar Qt para implementar interface gráfica
2. Implementar o simulador específico utilizando Python 
3. Implementar a lógica fuzzy com scikit-fuzzy

---
## Bibliografia:
* G. MELOTTI. 2009. ["Aplicação de Autômatos Celulares em Sistemas Complexos: Um Estudo de Caso em Espalhamento de Epidemias."](https://www.ppgee.ufmg.br/documentos/Defesas/802/Dissertacao_Gledson_final.pdf) Universidade Federal de Minas Gerais.