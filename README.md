# bst

![CI](https://github.com/wpwilkes/bst/actions/workflows/python-package.yml/badge.svg?branch=develop)

Binary Search Trees

## Installation

Clone the repository using https://github.com/wpwilkes/bst.git.
Use `pip` to run the installation process.

```bash
pip install path/to/bst/
```

## Test

After installing the package, be sure to run the tests to ensure the
software works as intended.

```bash
pytest path/to/tests/
```

## Usage

```python
import bst

tree = bst.BinarySearchTree()
avl_tree = bst.AVLTree()

for i in range(10):
    tree.insert(i)
    avl_tree.insert(i)

bst.algorithms.search(tree.root, 0)
# Node(key=0, value=None)

bst.algorithms.search_range(tree.root, 5, 6)
#[Node(key=5, value=None), Node(key=6, value=None)]

bst.algorithms.height(tree.root)
# 9

bst.algorithms.height(avl_tree.root)
# 3
```
