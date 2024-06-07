n = int(input('n = '))
if not n:
    print('zero')
else:
    ONE_NINE = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    sd, e = divmod(n, 10)
    s, d = divmod(sd, 10)
    res = []
    if s:
        res.append(ONE_NINE[s-1] + ' hundred')
    if d == 1:
        res.append(('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen')[e])
    else:
        if d > 1:
            res.append(('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                        'ninety')[d-2])
        if e:
            res.append(ONE_NINE[e-1])
    print(*res)