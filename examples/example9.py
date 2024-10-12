def outer2(out_param):
    def inner2():
        return f'Voin v pole: {out_param}'
    return inner2

value = outer2('odin')
print(value())