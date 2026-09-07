

def list_print(x: list):
    if len(x) < 10:
        return "sry too long of a list (not rly)"
    return "\n".join([str(i) for i in x])
