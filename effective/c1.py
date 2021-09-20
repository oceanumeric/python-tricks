import itertools


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value 


def to_bytes(bytes_to_str):
    if isinstance(bytes_to_str, str):
        value = bytes_to_str.encode('utf-8')
    else:
        value = bytes_to_str
    return value


def f_print():
    pantry = [
        ('avocados', 1.25),
        ('banana', 2.3),
        ('cherries', 2.9)
    ]

    for i, (item, count) in enumerate(pantry):
        print(f'#{i+1}: {item.title():<10s} = {round(count)}')


def zip_f():
    names = ['Cecilia', 'Lise', 'Marie']
    counts = [len(n) for n in names]
    max_count = 0
    longest_name = None
    print(dict(zip(names, counts)))
    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count
    print(longest_name, max_count)
    names.append('michael')
    for name, count in zip(names, counts):
        print(name, count)
    for name, count in itertools.zip_longest(names, counts):
        print(f'{name}: {count}')


if __name__ == '__main__':
    a = b'h\x65llo'  # bytes contains sequence of values
    b = 'h\x65llo'  # string contains sequence of unicode point
    print(list(a))
    print(list(b))
    print(a)
    print(b'love')
    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))
    print(repr(to_bytes(b'foo')))
    print(to_bytes('bar'))
    f_print()
    zip_f()
    if (length := len(list(b))) > 0:
        print(f'{length} is not zero')

