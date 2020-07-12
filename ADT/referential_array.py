import ctypes


def build_array(size):
    """
    This function creates an array of references to Python Objects.
    Args:
        size (int): A positive integer, the size of the array.
    Returns:
        An array of python references with the given size.
    """
    if size <= 0:
        raise ValueError("Array size should be larger than 0.")
    if not isinstance(size,  int):
        raise ValueError("Array size should be an integer.")
    array = (size * ctypes.py_object)()
    array[:] = size * [None]
    return array
