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
tree.insert(1)
tree.insert(0)
tree.insert(2)

bst.algorithms.search(tree.root, 0)
# Node(key=0, value=None)
```
