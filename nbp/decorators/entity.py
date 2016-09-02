from types import FunctionType


def entity(entity_name: str) -> FunctionType:
    """
    >>> @entity("test")
    ... class Test: pass
    >>> Test.entity_name
    'test'
    >>> Test().entity_name
    'test'

    :param entity_name: str
    :return: FunctionType
    """
    def decorator(item):
        item.entity_name = entity_name
        return item

    return decorator
