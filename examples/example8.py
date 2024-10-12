def outer(out_param):
    def inner(in_param):
        return f'Odin v pole: {in_param}'
    return inner(out_param)
print(outer('voin'))