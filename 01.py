class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_value(root):
    if root is None:
        return None

    current = root

    while current.right is not None:
        current = current.right

    return current.value

def find_min_value(root):
    if root is None:
        return None

    current = root
    # Переходимо до лівогоmost вузла
    while current.left is not None:
        current = current.left

    return current.value


def find_sum_of_values(root):
    if root is None:
        return 0

    # Сума значення поточного вузла, лівого та правого піддерев
    return root.value + find_sum_of_values(root.left) + find_sum_of_values(root.right)


# Створюємо дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

# Знаходимо найбільше значення
max_value = find_max_value(root)
print("Найбільше значення у дереві:", max_value)

# Знаходимо найменше значення
min_value = find_min_value(root)
print("Найменше значення у дереві:", min_value)

# Знаходимо суму всіх значень у дереві
sum_of_values = find_sum_of_values(root)
print("Сума всіх значень у дереві:", sum_of_values)
