def init():
    result = dict()
    result[1] = "P-38"
    result[2] = "L-049"
    result[3] = "U-2"
    return result


def search_db(id):
    result = init()
    return result.get(id, None)
