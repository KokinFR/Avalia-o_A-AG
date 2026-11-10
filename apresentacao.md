# Roteiro para apresentação (3–5 minutos)

## Slide 1 — Tema
**Roteirização de entregas para um motoboy: comparação entre A* e Algoritmo Genético.**

Fala: “Escolhemos comparar dois algoritmos de busca para decidir a ordem de visitação de oito endereços, saindo e voltando à base.”

## Slide 2 — Formulação
- Base fixa como início e fim.
- Oito entregas visitadas uma única vez.
- 8! = 40.320 rotas possíveis.
- Custo: soma das distâncias euclidianas entre pontos.

Fala: “Esse é um problema de otimização combinatória. As coordenadas são as do exemplo disponibilizado; a distância em linha reta simplifica as condições reais de trânsito.”

## Slide 3 — A*
- Estado: posição atual + entregas já visitadas.
- `f(n) = g(n) + h(n)`.
- `g`: distância percorrida.
- `h`: limite inferior baseado nas entregas restantes e retorno à base.
- Garante solução ótima com heurística admissível.

## Slide 4 — Algoritmo Genético
- Cromossomo: ordem das oito entregas.
- Aptidão: distância total (minimizar).
- Seleção por torneio, crossover OX, mutação por troca e elitismo.
- Busca estocástica, sem garantia geral de ótimo.

## Slide 5 — Resultado e conclusão
- A*: 47,42 unidades; 27 estados expandidos.
- AG (semente 42): 47,42 unidades.
- Mesma rota nesta execução; diferença 0%.
- A* confirma o ótimo no modelo; AG encontrou esse ótimo nesta execução.

Fala: “Os dois chegaram à mesma rota. Isso não significa que o AG sempre garanta o ótimo. Em problemas maiores, o AG pode ser útil quando explorar exatamente todas as possibilidades custa muito. O modelo pode ser melhorado usando distâncias reais de ruas.”

## Perguntas que podem surgir

**A rota é ótima?** Sim, no modelo de distâncias euclidianas, segundo o A* com heurística admissível.

**O AG sempre acha essa solução?** Não. É estocástico e seu resultado depende da população, parâmetros e semente.

**Por que usar dois algoritmos?** Para comparar uma busca informada que encontra o ótimo nesta instância com uma busca evolutiva que procura boas soluções sem garantia de ótimo.
