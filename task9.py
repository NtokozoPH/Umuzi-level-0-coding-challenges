def vowels(name):
    name = name.lower()
    vowels = ('a','e','i','o','u')
    v = []
    for l in name:
        if l in vowels:
            if l not in v:
                v.append(l)
                  
    v = ', '.join(v)
    print('Vowels:', v)