def is_val_positive_deco(orig_func):
        def temp_func(val):
                if val < 0:
                        return 0
                else:
                        return orig_func(val)
        return temp_func

@is_val_positive_deco
def sqrt(val):
        import math
        return math.pow(val, (1.0/2))

print(sqrt(-1))
print(sqrt(4))
