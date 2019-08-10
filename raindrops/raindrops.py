# my function
def convert(number):
    raindrops = ''
    sounds = {3: 'Pling', 5: 'Plang', 7:'Plong'}
    for k, v in sounds.items():
        if not(number%k):
            raindrops += v
    if raindrops:
        return raindrops
    else:
        return str(number)

# Example 1
def convert(number):
    splashes = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    sounds = ''.join([sound for fac, sound in splashes if not number % fac])
    # join函数，列表生成式中用if
    return sounds or f'{number}'
    # return ... or ...

# Example 2
def convert(number):
    drops = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    speak = [s for f, s in drops if n % f == 0]
    return "".join(speak) if speak else str(n)
    # return ... if ... else ...