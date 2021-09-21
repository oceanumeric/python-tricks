from typing import Dict
from collections.abc import MutableMapping

class Tool:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'Tool({self.name!r}, {self.weight})'


def populate_rank(votes:Dict, ranks:Dict) -> Dict:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i 


def get_winner(ranks:dict) -> iter:
    return next(iter(ranks))


class SortedDict(MutableMapping):
    def __init__(self) -> None:
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value) -> None:
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]
    
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

    
if __name__ == "__main__":
    tools = [
        Tool('level', 3.5),
        Tool('hammer', 1.25),
        Tool('screwdriver', 0.5),
        Tool('chisel', 0.25)
    ]
    print('Unsorted:', repr(tools))
    tools.sort(key=lambda x: x.name)
    print('\nSorted: ', tools)
    places = ['home', 'work', 'New York', 'Paris']
    places.sort()
    print('Case sensitive: ', places)
    places.sort(key=lambda x: x.lower())
    print('Case insensitive:', places)
    places.sort(key=lambda x: x.lower(), reverse=True)
    print('reversed: ', places)
    votes = {
        'otter': 1281,
        'polar bear': 587,
        'fox': 863
    }
    ranks = {}
    populate_rank(votes, ranks)
    print(ranks)
    winner = get_winner(ranks)
    print(winner)
    sorted_ranks = SortedDict()
    populate_rank(votes, sorted_ranks)
    print(sorted_ranks)
    winner = get_winner(sorted_ranks)
    print(winner)