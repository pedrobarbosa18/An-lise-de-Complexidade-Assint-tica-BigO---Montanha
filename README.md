# Análise de Complexidade Assintótica – Big-O

Esse repositório é a entrega do exercício da Aula 03 de Estruturas de Dados e Análise de Algoritmos. O tema da vez foi notação Big-O — aquela história de entender o quanto um algoritmo "sofre" quando a entrada começa a crescer.

---

## Por que isso importa?

Imagina que você tem um código que funciona bem com 10 elementos. Mas e com 10 mil? E com 1 milhão? É exatamente aí que a análise de complexidade entra — ela te ajuda a prever se o seu algoritmo vai continuar de boa ou vai travar geral quando os dados aumentarem.

Não é sobre cronômetro. É sobre entender o *comportamento* do código.

---

## O que tem nesse repositório

- **`exercicios_bigO.py`** — os 10 códigos do exercício, organizados e comentados, com uma seção de testes no final pra você rodar e ver funcionando na prática.
- **`analise_bigO.md`** — o documento com a análise de cada exercício: qual a complexidade e o raciocínio por trás da resposta.

---

## Os 10 exercícios

| # | Função | Complexidade |
|---|---|---|
| 1 | `verificar_primeiro` | O(1) |
| 2 | `somar_lista` | O(n) |
| 3 | `busca_binaria` | O(log n) |
| 4 | `pares_com_soma` | O(n²) |
| 5 | `imprimir_pares_e_soma` | O(n²) |
| 6 | `potencias_de_dois` | O(log n) |
| 7 | `fibonacci_recursivo` | O(2ⁿ) |
| 8 | `ordenacao_bolha` | O(n²) |
| 9 | `produto_de_matrizes` | O(n³) |
| 10 | `merge_sort` | O(n log n) |

---

## Como rodar

Sem segredo. Só precisa ter Python instalado:

```bash
python exercicios_bigO.py
```

---

## Cola rápida das complexidades

Se quiser lembrar a ordem do "mais rápido pro mais lento":

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

O Fibonacci recursivo ali no O(2ⁿ) é um bom exemplo de como uma solução "que funciona" pode ser inviável na prática — pra n=50, são mais de um quadrilhão de chamadas. 😅

---

*Estruturas de Dados e Análise de Algoritmos — Prof. Alexandre de Oliveira — 2026*
