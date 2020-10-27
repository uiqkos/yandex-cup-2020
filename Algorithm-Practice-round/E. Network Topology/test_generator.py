import random

def choice(population: list):
    exist_nodes = [1]
    while len(population) > 0:

        node1, node2 = random.choice(exist_nodes), random.choice(population)
        yield node1, node2

        exist_nodes.append(node2)
        population.remove(node2)

def generate_test(test_count):
    for i in range(test_count):
        node_count = random.randint(2, 20)
        nodes = list(range(2, node_count + 1))

        edge_count = node_count - 1
        edges = []
        for choice_ in choice(nodes):
            edges.append(choice_)
        yield node_count, edges


for node_count, pairs in generate_test(10):
    print(node_count)
    print(', '.join([' -> '.join([str(pair[0]), str(pair[1])]) for pair in pairs]))