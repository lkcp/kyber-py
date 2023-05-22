
import os
from kyber import *
from .utils import serialize
N = 4 #parallel

params = DEFAULT_PARAMETERS["kyber768"]
n = params["n"]
k = params["k"]
q = params["q"]
eta_1 = params["eta_1"]
eta_2 = params["eta_2"]
du = params["du"]
dv = params["dv"]

ct_pair = [(107, 2705), (624, 1837), (1252, 0)]

# 107 * 3 = 321
# 624 * 3 = 1837 0, 624, 1248
# 之前选的密文对不一定能用，
# the first N bits is zero
def construct_ct():
    

    return True


# return hamming distance of every block
def leak(m_bits, N):
    assert m_bits[:N] == [0]*N,  "the first block must be zero"
    assert len(m_bits) % N == 0, "length of message must divisible for N"
    hd = []
    for i in range(0, len(m_bits), N):
        hd.append(sum(m_bits[i:i+N]))
    return hd
    
    


kem = Kyber(params)
pk, sk = kem.keygen()

ct = construct_ct()

message = kem._cpapke_dec(sk, ct)

m_bits = serialize(message)

leakage = leak(m_bits, N)

# distrib = leakage_to_prob()
