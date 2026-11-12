# Roteirização de entregas com A* e Algoritmo Genético

**Disciplina:** Inteligência Artificial  
**Integrantes:** Kauê Cardoso e Francisco Rafael  
**Professor:** Renê Gadelha  
**Data:** [preencher]

## 1. Problema

O problema escolhido é encontrar uma rota curta para um motoboy que deve sair de uma base, visitar oito endereços de entrega uma única vez e retornar à base. A rota precisa definir a ordem de visitação dos endereços.

O modelo usa coordenadas cartesianas fornecidas no material da atividade e distância euclidiana entre cada par de locais. Portanto, os resultados representam unidades de distância em linha reta, não quilômetros reais de ruas.

## 2. Formulação como busca

- **Estado:** `(local atual, conjunto de entregas já visitadas)`.
- **Estado inicial:** Base, com nenhuma entrega realizada.
- **Ações:** deslocar-se a qualquer endereço ainda não visitado.
- **Objetivo:** todas as oito entregas visitadas e retorno à Base.
- **Custo de ação:** distância euclidiana entre o local atual e o próximo endereço.
- **Espaço de soluções completas:** `8! = 40.320` ordens de visita, pois a Base é fixa no início e no fim.

## 3. A*

O A* calcula `f(n) = g(n) + h(n)`, em que `g(n)` é a distância já percorrida e `h(n)` estima um limite inferior para a distância restante. Neste projeto, a heurística soma: (1) a menor ligação entre o local atual e uma entrega ainda pendente; (2) o custo da árvore geradora mínima entre as entregas pendentes; e (3) a menor ligação de uma entrega pendente até a Base. Quando não há entregas pendentes, a heurística é a distância direta de retorno à Base.

Essa estimativa não excede o custo de qualquer continuação válida. Com custos não negativos e esta heurística admissível, o A* retorna uma solução ótima para o modelo definido.

## 4. Algoritmo Genético

Cada cromossomo é uma permutação dos oito endereços, e a aptidão é a distância total da rota (quanto menor, melhor). A população inicial é aleatória. O algoritmo usa seleção por torneio, crossover Order (OX), mutação por troca de duas posições e elitismo para preservar a melhor solução da geração. A execução usa semente fixa 42 para possibilitar reprodução do resultado.

O AG é uma busca estocástica e não garante encontrar o ótimo em todas as instâncias ou execuções. Nesta instância, seu resultado é comparado com a referência ótima obtida pelo A*.

## 5. Resultados

Na execução com os parâmetros definidos no código, os dois algoritmos encontraram a rota abaixo:

**Base → Entrega 6 (Condomínio Lago) → Entrega 5 (Distrito Industrial) → Entrega 4 (Jd. Botânico) → Entrega 3 (Vila Nova) → Entrega 2 (Bairro Alto) → Entrega 1 (Centro) → Entrega 8 (Shopping) → Entrega 7 (Praça Central) → Base**

| Algoritmo | Distância | Resultado |
|---|---:|---|
| A* | 47,42 unidades | Ótimo para o modelo |
| AG (semente 42) | 47,42 unidades | Igual ao ótimo nesta execução |

O A* expandiu 27 estados até encontrar a solução. A diferença de distância do AG em relação ao A* foi 0,00% nesta execução. Isso não prova que o AG sempre produzirá o ótimo; demonstra apenas o resultado com os dados, parâmetros e semente informados.

## 6. Comparação e conclusão

O A* oferece garantia de optimalidade quando a heurística é admissível, mas pode consumir mais memória e tempo conforme o espaço de estados cresce. O AG não garante o ótimo, porém explora boas soluções por população e pode ser adaptado a espaços grandes nos quais a busca exata se torne cara. Para esta instância de oito entregas, ambos encontraram a mesma rota de 47,42 unidades, e o A* serve como referência para avaliar o AG.

Uma limitação importante é que as distâncias euclidianas simplificam o deslocamento real. Uma extensão seria substituir essas distâncias por tempos ou distâncias obtidos de uma malha viária, mantendo o mesmo problema de otimização.

## 7. Execução

Com Python 3.9 ou superior, entre na pasta do projeto e execute `python main.py`. O código não requer bibliotecas externas. O programa imprime as rotas, distâncias e diferença percentual.
