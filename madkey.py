import random
noun = []
while True:
    print('Enter the noun ' +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    noun = noun + [name]  # list concatenation

verb = []
while True:
    print('Enter the verb ' +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    verb = verb + [name]


def r_verb():
    # import random
    ran = random.choice(verb)
    return ran


def r_noun():
    # import random
    rav = random.choice(noun)
    return rav


print('kjerkejhkjh', r_noun(), 'iueyro')
