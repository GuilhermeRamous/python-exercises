def n_base(n, base):
    convstring = "0123456789ABCDEF"

    if n < base:
        return convstring[n]
    else:
        return n_base(n // base, base) + convstring[n % base]

print(n_base(135, 16))
