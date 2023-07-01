class BTree:
    class Node:
        def __init__(self, min_degree):
            self.is_leaf = True
            self.elements = list()
            self.children = list()
            self.min_degree = min_degree

        def node_split(self, parent, element):
            """Делит ноду пополам, если она переполнена"""
            new_node = BTree.Node(self.min_degree)
            middle = self.node_size() // 2
            middle_element = self.elements[middle]
            parent.add_element(middle_element)
            new_node.children = self.children[middle + 1:]
            new_node.elements = self.elements[middle + 1:]
            self.children = self.children[:middle + 1]
            self.elements = self.elements[:middle]
            if len(new_node.children) > 0:
                new_node.is_leaf = False
            parent.children = parent.add_child(new_node)
            if element < middle_element:
                return self
            else:
                return new_node

        def node_is_full(self):
            """Проверяет, переполнена ли нода"""
            return self.node_size() == 2 * self.min_degree - 1

        def node_size(self):
            """Возвращает размер ноды"""
            return len(self.elements)

        def add_element(self, value):
            """Добавляет элемент в ноду и сортирует ее"""
            self.elements.append(value)
            self.elements.sort()

        def add_child(self, new_node):
            """Добавляет дочернюю ноду"""
            counter = len(self.children) - 1
            while counter >= 0 and self.children[counter].elements[0] > \
                    new_node.elements[0]:
                counter -= 1
            result = self.children[:counter + 1]
            result += [new_node] + self.children[counter + 1:]
            return result

    def __init__(self, min_degree):
        self.min_degree = min_degree
        if self.min_degree <= 1:
            raise ValueError("Степень дерева должна быть >= 2")
        self.root = self.Node(min_degree)
        self.sorted_elements = list()

    def insert_element(self, element):
        """Вставляет элемент в дерево"""
        current_node = self.root
        if current_node.node_is_full():
            new_root = self.Node(self.min_degree)
            new_root.children.append(self.root)
            new_root.is_leaf = False
            current_node = current_node.node_split(new_root, element)
            self.root = new_root

        while not current_node.is_leaf:
            i = current_node.node_size() - 1
            while i > 0 and element < current_node.elements[i]:
                i -= 1
            if element > current_node.elements[i]:
                i += 1
            next_node = current_node.children[i]
            if next_node.node_is_full():
                current_node = next_node.node_split(current_node, element)
            else:
                current_node = next_node
        current_node.add_element(element)

    def get_sorted_array(self):
        """Возвращает отсортированные элементы из дерева"""
        current_node = self.root
        self.make_sorted_array(current_node)
        return self.sorted_elements

    def make_sorted_array(self, current_node):
        """Рекурсивный обход элементов"""
        if current_node.is_leaf:
            for num in current_node.elements:
                self.sorted_elements.append(num)
        else:
            counter = 0
            for child_node in current_node.children:
                self.make_sorted_array(child_node)
                if counter < len(current_node.elements):
                    self.sorted_elements.append(current_node.elements[counter])
                    counter += 1
