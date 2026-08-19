from redash._enh_rate_b import window_size

def rate_for(n):
    return float(n) / max(1, window_size())
