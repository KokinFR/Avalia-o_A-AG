# Busca de rota de entregas: A* e Algoritmo Genético

Projeto da atividade de Inteligência Artificial.

## Equipe

- Kauê Cardoso
- Francisco Rafael
 Compara dois algoritmos para o mesmo problema: visitar oito endereços de entrega, saindo e retornando à Base, minimizando a distância total.

## Problema e espaço de busca

Cada solução é uma permutação dos oito endereços. Há `8! = 40.320` ordens possíveis. As distâncias entre pontos são euclidianas, calculadas a partir das coordenadas do exemplo fornecido na atividade. O modelo supõe que a distância em linha reta representa o custo de deslocamento; não considera ruas, trânsito ou sentido de vias.

## Algoritmos

- **A\*:** estado `(local atual, entregas visitadas)`, custo acumulado `g(n)` e heurística `h(n)`. A heurística soma o menor custo de conexão do ponto atual às entregas restantes, a árvore geradora mínima dessas entregas e o menor custo de retorno à Base. É um limite inferior para qualquer continuação válida; assim, A* encontra uma rota ótima nesse modelo.
- **AG:** cromossomo permutacional, população aleatória, seleção por torneio, crossover Order (OX), mutação por troca e elitismo. É uma busca estocástica: pode encontrar uma rota muito boa, mas não garante o ótimo.

## Como executar

Requer Python 3.9 ou superior. Não há dependências externas.

```bash
python main.py
```

O programa imprime a distância e o itinerário de cada método, estados expandidos pelo A* e a diferença percentual do AG em relação ao ótimo. O AG usa semente fixa (`42`) para tornar a execução reproduzível.

## Como interpretar

A* é usado como referência ótima para esta instância pequena. O AG pode retornar a mesma distância ótima, mas isso é resultado daquela execução parametrizada, não uma garantia geral. Para avaliar o comportamento estocástico, altere a semente e compare várias execuções. Em problemas maiores, o espaço de busca pode crescer rapidamente; o AG pode ser útil quando uma busca exata custa demais.

## Estrutura

- `main.py`: implementação e execução dos dois algoritmos.
- `relatorio.md`: texto-base para apresentar e entregar.
- `requirements.txt`: dependências (nenhuma além da biblioteca padrão).
