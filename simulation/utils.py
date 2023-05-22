# convert 32 bytes to 256 bits
def serialize(m):
    m_bits = [0]*256
    for i in range(256):
        m_bits[i] = (m[i//8] >> (i%8)) & 0x01
    return m_bits

# eta =2
# (107, 2705) 0 0 0 0 1  ok
#             0 0 1 1 0
#             0 1 0 1 0
# s[i]       -2 -1 0 1 2
one_range_start = 833
one_range_end = 2496
def cond1(ku, kv, exp):
    for s in range(-2, 3):
        mp = (kv - ku * s) % 3329
        if mp >= one_range_start and mp <= one_range_end:
            if exp[s+2] == 0:
                return False
        else:
            if exp[s+2] == 1:
                return False
    return True

# ku is True for cond1 and cond2
# ku 就可以起到恢复私钥的作用，也可以起到使得消息一定为0的作用
def cond2(ku, kv):
    for s in range(-2, 3):
        mp = (kv -ku * s) % 3329
        if mp >= one_range_start and mp <= one_range_end:
            return False
    return True


# look for satisfying ku and kv
def chosen_ct():
    exp = [0, 0, 1, 0, 0]
    for ku in range(3329):
        for kv in range(3329):
            if cond1(ku, kv, exp):
                for kvp in range(3329):
                    if cond2(ku, kvp):
                        print("ku = {}, kv = {} is ok!".format(ku, kv))











if __name__ =="__main__":
    chosen_ct()
