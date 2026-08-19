from redash._enh_rate_a import rate_for

def window_size():
    return 60

def normalized(n):
    return rate_for(n) * window_size()
