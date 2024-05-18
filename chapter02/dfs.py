from tree_data import Tree, tree_01


def dfs(tree: Tree | None):
    if not tree:
        return

    dfs(tree.left_child)
    dfs(tree.right_child)
    print(tree.value)


dfs(tree_01)
