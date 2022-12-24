def sack_compartments(input):
    sacks: list = input.splitlines()
    sum: int = 0

    for sack in sacks:
        # split the sack in half
        mid = len(sack) // 2
        comp_1 = sack[:mid]
        comp_2 = sack[mid:]
        duplicate: str = ''.join(set(comp_1)&set(comp_2))
        sum += item_to_rank(duplicate)
    return sum

def item_to_rank(item: str):
    """returns the rank of the item"""
    if item.isupper():
        return ord(item) -38
    else:
        return ord(item) - 96

input = """"""

print(sack_compartments(input))