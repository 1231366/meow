
# 📊 Análise Estatística de Lucros Anuais de Estações Ferroviárias

## ✅ Resumo do Enunciado

**Objetivo:** Analisar os **lucros anuais** de uma estação ferroviária, escolhida pelo utilizador, e gerar uma **análise estatística descritiva**.

### O que se pretende calcular:
- Média
- Desvio padrão
- Mediana
- Moda

Além disso:
- Identificar **valores outliers**
- Determinar **ano mais lucrativo** e **ano menos lucrativo**

---

## 📚 Teoria dos Conceitos Utilizados

### 🔢 1. Média (Mean)
- **O que é:** Soma de todos os valores dividida pelo número total de valores.
- **Para que serve:** Representa o valor "típico" ou "esperado".
- **Exemplo:** `[10, 20, 30] → (10+20+30)/3 = 20`

### 📐 2. Desvio Padrão (Standard Deviation)
- **O que é:** Mede **quanto os valores se afastam da média**.
- **Para que serve:** Se for alto, os valores estão muito dispersos; se for baixo, estão concentrados.
- **Exemplo:** `[10, 11, 12]` tem desvio menor que `[1, 20, 50]`.

### 🔸 3. Mediana (Median)
- **O que é:** Valor que está **no meio** quando os dados estão ordenados.
- **Para que serve:** Indica o “centro” dos dados, e não é afetada por valores extremos.
- **Exemplo:** `[10, 20, 30] → 20`, `[10, 20, 1000] → 20`

### 🔹 4. Moda (Mode)
- **O que é:** Valor **mais frequente** num conjunto de dados.
- **Para que serve:** Mostra o valor que aparece mais vezes.
- **Exemplo:** `[5, 5, 10, 20] → Moda = 5`

### ❗ 5. Outliers
- **O que são:** Valores **muito diferentes dos restantes**, que podem indicar erros ou casos especiais.
- **Como se calcula:** Usando o **IQR (Interquartile Range)**:
  - `IQR = Q3 - Q1`
  - Um valor é outlier se:
    - `valor < Q1 - 1.5 * IQR`
    - `valor > Q3 + 1.5 * IQR`

### 📊 6. Lucro Anual
- **Definição:** Lucro mensal = Receitas - Despesas
- Lucro anual = Soma dos lucros de todos os meses desse ano

### 📈 7. Visualização com gráfico de barras
- Mostra os **lucros por ano** para a estação escolhida.
- Permite **comparar visualmente** anos bons e maus.

---

## 🎓 Extra: Porquê usar Análise Descritiva?
- Dá uma **visão rápida e clara** do comportamento dos dados
- Ajuda a identificar **tendências**, **anomalias** e **extremos**
- Facilita a **tomada de decisões**
