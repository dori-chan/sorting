import unittest
import sorts
import external_sort
import b_tree


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(
            sorts.bubble_sort(simple_array), [1, 5, 6, 7, 9, 45])
        self.assertEqual(sorts.bubble_sort(he_dont_need_sort),
                         [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.bubble_sort(empty_arr), [])
        self.assertEqual(sorts.bubble_sort(negative_arr),
                         [-120, -94, -87, -77, -35, -5, -1])
        self.assertEqual(
            sorts.bubble_sort(mixed_arr),
            [-22, -8, -6, -2, 0, 2, 3, 4, 4, 47])

    def test_shell_sort(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(
            sorts.shell_sort(simple_array), [1, 5, 6, 7, 9, 45])
        self.assertEqual(
            sorts.shell_sort(he_dont_need_sort), [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.shell_sort(empty_arr), [])
        self.assertEqual(
            sorts.shell_sort(negative_arr), [-120, -94, -87, -77, -35, -5, -1])
        self.assertEqual(
            sorts.shell_sort(mixed_arr), [-22, -8, -6, -2, 0, 2, 3, 4, 4, 47])

    def test_insert_sort_with_step(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(sorts.insert_sort_with_step(simple_array, 1, 3),
                         [5, 7, 45, 1, 9, 6])
        self.assertEqual(sorts.insert_sort_with_step(he_dont_need_sort, 5, 2),
                         [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.insert_sort_with_step(empty_arr, 1, 0), [])
        self.assertEqual(sorts.insert_sort_with_step(negative_arr, 5, 1),
                         [-87, -1, -77, -120, -94, -35, -5])
        self.assertEqual(sorts.insert_sort_with_step(mixed_arr, 2, 3),
                         [3, -8, -6, 4, -22, 0, 47, -2, 2, 4])

    def test_insert_sort_without_step(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(
            sorts.insert_sort_without_step(simple_array), [1, 5, 6, 7, 9, 45])
        self.assertEqual(sorts.insert_sort_without_step(he_dont_need_sort),
                         [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.insert_sort_without_step(empty_arr), [])
        self.assertEqual(sorts.insert_sort_without_step(negative_arr),
                         [-120, -94, -87, -77, -35, -5, -1])
        self.assertEqual(sorts.insert_sort_without_step(mixed_arr),
                         [-22, -8, -6, -2, 0, 2, 3, 4, 4, 47])

    def test_heap_sort(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(
            sorts.heap_sort(simple_array), [1, 5, 6, 7, 9, 45])
        self.assertEqual(sorts.heap_sort(he_dont_need_sort),
                         [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.heap_sort(empty_arr), [])
        self.assertEqual(sorts.heap_sort(negative_arr),
                         [-120, -94, -87, -77, -35, -5, -1])
        self.assertEqual(sorts.heap_sort(mixed_arr),
                         [-22, -8, -6, -2, 0, 2, 3, 4, 4, 47])

    def test_quick_sort(self):
        simple_array = [5, 9, 45, 1, 7, 6]
        he_dont_need_sort = [1, 1, 1, 1, 1, 1, 1]
        empty_arr = []
        negative_arr = [-87, -1, -77, -120, -35, -5, -94]
        mixed_arr = [3, -8, 0, 4, -22, 2, 47, -2, -6, 4]
        self.assertEqual(
            sorts.quick_sort(simple_array), [1, 5, 6, 7, 9, 45])
        self.assertEqual(sorts.quick_sort(he_dont_need_sort),
                         [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sorts.quick_sort(empty_arr), [])
        self.assertEqual(sorts.quick_sort(negative_arr),
                         [-120, -94, -87, -77, -35, -5, -1])
        self.assertEqual(sorts.quick_sort(mixed_arr),
                         [-22, -8, -6, -2, 0, 2, 3, 4, 4, 47])
        self.assertEqual(sorts.quick_sort([5, 41]),
                         [5, 41])


class Testexternal_sort(unittest.TestCase):
    def test_external_sort(self):
        actual = external_sort.external_sort('test.txt')
        expected = [0, 1, 4, 5, 22, 55]
        self.assertEqual(actual, expected)

    def test_file_generator(self):
        actual = external_sort.file_generator(3, "test.txt")
        expected = ["0.txt", "1.txt"]
        self.assertEqual(actual, expected)

        actual = external_sort.file_generator(1500, "test.txt")
        expected = ["0.txt"]
        self.assertEqual(actual, expected)

    def test_split_set_of_elements(self):
        actual_gen = external_sort.split_set_of_elements("test.txt", 3)
        self.assertEqual(next(actual_gen), ["5", "4", "22"])
        self.assertEqual(next(actual_gen), ["55", "0", "1"])


class Test_b_tree(unittest.TestCase):
    def setUp(self):
        self.tree = b_tree.BTree(2)
        self.tree.insert_element(5)
        self.tree.insert_element(5)

    def test_node_is_full(self):
        self.assertEqual(self.tree.root.node_is_full(), False)
        self.tree.insert_element(5)
        self.assertEqual(self.tree.root.node_is_full(), True)

    def test_is_leaf(self):
        self.assertEqual(self.tree.root.is_leaf, True)
        self.tree.insert_element(1)
        self.tree.insert_element(5)
        self.assertEqual(self.tree.root.is_leaf, False)

    def test_node_size(self):
        self.assertEqual(self.tree.root.node_size(), 2)
        self.tree.insert_element(5)
        self.assertEqual(self.tree.root.node_size(), 3)

    def test_add_element(self):
        self.tree.root.add_element(0)
        self.assertEqual(self.tree.root.elements, [0, 5, 5])
        self.tree.root.add_element(-20)
        self.assertEqual(self.tree.root.elements, [-20, 0, 5, 5])

    def test_add_child(self):
        node = self.tree.root
        new_node = self.tree.Node(2)
        new_node.add_element(3)
        node.children = node.add_child(new_node)
        self.assertEqual(node.children[0], new_node)

    def test_node_split(self):
        self.tree.root.add_element(-20)
        self.tree.root.add_element(1)
        new_node = self.tree.Node(2)
        new_node = self.tree.root.node_split(new_node, 1)
        self.assertEqual(new_node.elements, [-20, 1])

    def test_insert_element(self):
        self.tree.insert_element(-20)
        self.tree.insert_element(1)

        self.assertEqual(self.tree.root.is_leaf, False)
        self.assertEqual(self.tree.root.elements, [5])
        self.assertEqual(len(self.tree.root.children), 2)
        self.assertEqual(self.tree.root.children[0].elements, [-20, 1])
        self.assertEqual(self.tree.root.children[1].elements, [5])

    def test_make_sorted_array(self):
        self.tree.insert_element(-20)
        self.tree.insert_element(1)
        self.tree.make_sorted_array(self.tree.root)
        self.assertEqual(self.tree.sorted_elements, [-20, 1, 5, 5])

    def test_get_sorted_array(self):
        self.tree.insert_element(-20)
        self.tree.insert_element(30)
        actual = self.tree.get_sorted_array()
        expected = [-20, 5, 5, 30]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
