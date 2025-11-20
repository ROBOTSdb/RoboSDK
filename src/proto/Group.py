"""A Group node contains children nodes without introducing a new transformation. It is equivalent to a Transform node without the "translation" and "rotation" fields."""
from .Proto import Proto
class GROUP(Proto):
    ...