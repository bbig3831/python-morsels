

def parse_ranges(sequence: str):
    """Return iterable based on string of number ranges"""
    result = []
    for item in sequence.split(','):
        if '-' in item:
            start, stop = item.split('-')
            result += list(range(int(start), int(stop)+1))
        else:
            result.append(int(item))

    return iter(result)