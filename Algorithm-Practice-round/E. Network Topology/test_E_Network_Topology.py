# from E_Network_Topology import get_best_nodes
E_Network_Topology = __import__(
    'E_Network_Topology',
    fromlist=['get_best_nodes', 'fill_matrix', 'fill_matrix_iterate']
)

test_generator = __import__(
    'test_generator',
    fromlist=['generate_test']
)


def test_get_best_nodes():
    get_best_nodes = E_Network_Topology.get_best_nodes

    # Standard tests
    assert get_best_nodes(3, '1 2; 2 3') in ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2))
    assert get_best_nodes(6, '1 2; 3 2; 2 4; 4 5; 4 6') in ((2, 4), (4, 2))

    # Other
    assert get_best_nodes(9, '1 2; 2 3; 2 5; 4 5; 6 5; 5 7; 7 8; 7 9') in ((2, 5), (5, 2), (5, 7), (7, 5))


def test_fill_matrix_iterate():
    generate_test = test_generator.generate_test

    fill_matrix_expected = E_Network_Topology.fill_matrix
    fill_matrix_actual = E_Network_Topology.fill_matrix_iterate

    # Test iterate
    for test_num, (node_count, edges) in enumerate(generate_test(100000)):
        assert fill_matrix_expected(edges) == fill_matrix_actual(edges)
        print(f"Test {test_num + 1} -- Passed")

