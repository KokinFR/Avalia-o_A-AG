"""Comparação entre A* e Algoritmo Genético para roteirização de entregas.

Modelo: visitar todos os oito pontos uma vez, partindo e retornando à Base.
As distâncias são euclidianas, como no material da atividade.
"""
from __future__ import annotations
import heapq
import math
import random
from typing import Dict, List, Tuple

POINTS: Dict[str, Tuple[float, float]] = {
    "Base": (0, 0),
    "Entrega 1 - Centro": (2, 4),
    "Entrega 2 - Bairro Alto": (5, 9),
    "Entrega 3 - Vila Nova": (8, 3),
    "Entrega 4 - Jd. Botânico": (6, -2),
    "Entrega 5 - Distrito Industrial": (1, -5),
    "Entrega 6 - Condomínio Lago": (-3, -4),
    "Entrega 7 - Praça Central": (-4, 2),
    "Entrega 8 - Shopping": (-1, 7),
}
NAMES = list(POINTS)
BASE = 0
N = len(NAMES)
DELIVERY_COUNT = N - 1
DIST = [[math.dist(POINTS[a], POINTS[b]) for b in NAMES] for a in NAMES]
FULL_MASK = (1 << DELIVERY_COUNT) - 1


def route_distance(route: List[int]) -> float:
    """Distância Base -> entregas na ordem dada -> Base."""
    full = [BASE, *route, BASE]
    return sum(DIST[a][b] for a, b in zip(full, full[1:]))


def mst_cost(nodes: Tuple[int, ...]) -> float:
    """Custo da árvore geradora mínima completa nos nós restantes."""
    if len(nodes) < 2:
        return 0.0
    used = {nodes[0]}
    total = 0.0
    while len(used) < len(nodes):
        cost, target = min((DIST[a][b], b) for a in used for b in nodes if b not in used)
        total += cost
        used.add(target)
    return total


def heuristic(current: int, mask: int) -> float:
    """Limite inferior admissível: conexão atual + MST restante + volta à base."""
    remaining = tuple(i for i in range(1, N) if not (mask & (1 << (i - 1))))
    if not remaining:
        return DIST[current][BASE]
    return (min(DIST[current][r] for r in remaining)
            + mst_cost(remaining)
            + min(DIST[r][BASE] for r in remaining))


def astar() -> Tuple[List[int], float, int]:
    """A* em estados (local atual, conjunto de entregas visitadas)."""
    start = (BASE, 0)
    queue = [(heuristic(BASE, 0), 0.0, BASE, 0)]
    best_g = {start: 0.0}
    parent = {}
    expanded = 0
    while queue:
        _, g, current, mask = heapq.heappop(queue)
        state = (current, mask)
        if g != best_g.get(state):
            continue
        expanded += 1
        if mask == FULL_MASK:
            # A volta à base é o custo final do estado.
            final_cost = g + DIST[current][BASE]
            order = []
            while state != start:
                previous, delivered = parent[state]
                order.append(delivered)
                state = previous
            order.reverse()
            return order, final_cost, expanded
        for nxt in range(1, N):
            bit = 1 << (nxt - 1)
            if mask & bit:
                continue
            next_mask = mask | bit
            next_state = (nxt, next_mask)
            next_g = g + DIST[current][nxt]
            if next_g < best_g.get(next_state, math.inf):
                best_g[next_state] = next_g
                parent[next_state] = (state, nxt)
                heapq.heappush(queue, (next_g + heuristic(nxt, next_mask), next_g, nxt, next_mask))
    raise RuntimeError("Nenhuma rota encontrada")


def genetic_algorithm(seed: int = 42, population_size: int = 120,
                      generations: int = 250, mutation_rate: float = 0.15):
    """AG permutacional com torneio, crossover order (OX), mutação e elitismo."""
    rng = random.Random(seed)
    genes = list(range(1, N))
    def individual(): return rng.sample(genes, len(genes))
    def tournament(pop): return min(rng.sample(pop, 3), key=route_distance)[:]
    def ox(a, b):
        left, right = sorted(rng.sample(range(len(a)), 2))
        child = [None] * len(a)
        child[left:right + 1] = a[left:right + 1]
        fill = [gene for gene in b if gene not in child]
        cursor = 0
        for i in list(range(right + 1, len(a))) + list(range(0, left)):
            child[i] = fill[cursor]
            cursor += 1
        return child
    pop = [individual() for _ in range(population_size)]
    best_seen = min(pop, key=route_distance)[:]
    for _ in range(generations):
        pop.sort(key=route_distance)
        if route_distance(pop[0]) < route_distance(best_seen):
            best_seen = pop[0][:]
        next_pop = [pop[0][:]]  # elitismo: preserva o melhor
        while len(next_pop) < population_size:
            child = ox(tournament(pop), tournament(pop))
            if rng.random() < mutation_rate:
                i, j = rng.sample(range(len(child)), 2)
                child[i], child[j] = child[j], child[i]
            next_pop.append(child)
        pop = next_pop
    candidate = min(pop, key=route_distance)
    if route_distance(candidate) < route_distance(best_seen):
        best_seen = candidate[:]
    return best_seen, route_distance(best_seen)


def show(label: str, route: List[int], distance: float) -> None:
    itinerary = [NAMES[BASE], *(NAMES[i] for i in route), NAMES[BASE]]
    print(f"{label}: {distance:.2f} unidades")
    print("  " + " -> ".join(itinerary))


if __name__ == "__main__":
    exact_route, exact_distance, expanded = astar()
    ga_route, ga_distance = genetic_algorithm()
    show("A* (ótimo)", exact_route, exact_distance)
    print(f"  Estados expandidos: {expanded}")
    show("AG (melhor encontrado)", ga_route, ga_distance)
    print(f"  Diferença para o ótimo: {ga_distance - exact_distance:.2f} unidades "
          f"({(ga_distance / exact_distance - 1) * 100:.2f}%)")
