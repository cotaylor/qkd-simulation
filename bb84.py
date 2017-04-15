import numpy as np
import qit
from utils import *

def bb84(n, verbose=True):
    """Simulation of Bennett & Brassard's 1984 protocol for quantum key distribution.
    Assumes the presence of an eavesdropper attempting an intercept-resend attack.
    """

#    if verbose: print("\n-=BB84 protocol - %d initial bits with eavesdropping=-\n\n") % n

    # TODO: for now this is just a wrapper
    bb84Noiseless(n, True)

def bb84Noiseless(n, verbose=True):
    """Performs BB84, assuming no eavesdropper is present.
    See bb84(n, verbose) for details.
    """
    
    if verbose: print("\n-=BB84 protocol - %d initial bits with no eavesdropping=-\n\n") % n
    
    # Alice generates a random bit string to be encoded
    rawKey = getRandomBits(n)

    # Alice also randomly chooses which basis to use when encoding each bit
    # 0: computational basis; 1: Hadamard basis
    aBases = getRandomBits(n)

    if verbose:
        print("Alice's raw key:\n%s") % bitFormat(rawKey)
        print("Alice's basis choices:\n%s") % bitFormat(aBases)

    # Alice prepares n qubits, with the kth qubit in state |0> or |1> in either the computational
    # basis or the Hadamard basis, depending on the value of the kth bit in each bitstring
    sent = encodeRawKey(rawKey, aBases)

    # Alice sends each qubit one at a time to Bob, who measures each in a randomly chosen basis
    bBases = getRandomBits(n)
    bKey = []
    for k in range(n):
        bKey.append(decodeState(sent[k], bBases[k]))

    if verbose: print("Bob's measurement results:\n%s") % bitFormat(bKey)