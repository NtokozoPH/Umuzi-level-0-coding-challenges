def vowels(name):
    vowels = ('a','e','i','o','u','A','E','I','O','U')   # defining vowels
    for l in name:
        if l in vowels:
            print(l)