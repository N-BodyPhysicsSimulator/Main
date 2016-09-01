def entity(entity_name):
    def decorator(c):
        c.entity_name = entity_name
        return c

    return decorator
