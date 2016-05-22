# HIDDEN INFORMATION Documentation
1. [Preface](preface.md)
2. [User's Guide](guide.md)
***

## Quantum Cryptography
Quantum cryptography is the science of exploiting quantum mechanical properties to perform cryptographic tasks. The main advantage of the quantum cryptographic protocol is the inability to make the interference goes unnoticed. it is connected with the property of the wave function which means that any change in the quantum system changes its initial state. When an attacker is trying to find out information he inevitably makes a mistake. When an error is close to the critical value (depending on the protocol) key length tends to zero  and key transfer becomes impossible. The more critical error the more stable system.

We consider one of the confidential information transmission technology. Send the message over the open channel but *specially encrypted*. It is understood the impossibility of obtaining useful information without the *secret key*.
### QKD Protocols
- BB84

![BB84](/img/bb84.jpg)

*General schematic*:
Traditionally, cryptography legitimate users can be designated as Alice and Bob, and the attacker called Eve. So, let's describe the situation in the cryptographic protocol. Alice needs to send a secret message to Bob, and Eve all the means at its disposal tries to intercept it. In the first stage Alice sends photons to Bob in some arbitrarily chosen basis. Some photons may be sent together or one after the other but there is a limit: Alice and Bob need to establish a one-to-one correspondence between the sent and received photon. Bob measures the received photons in one of the two bases, and arbitrarily selected (regardless of the Alice's choice). At this stage in the case of identical bases they get results completely correlated. However, if they use different bases obtained results uncorrelated. On average, Bob receives a bit string with a 25% error, called a primary key. This error is so large that the use of conventional error correction algorithm is impossible. Nevertheless, it is possible to carry out the following procedure, called matching bases. For each passed state Bob openly reported in which we measured the qubit basis (but does not report the results of measurements). Alice then tells when its base coincides with Bob's base. If the bases are matched -  bit is left, but if not, ignore it. In this case, approximately 50% of the data is discarded. The remaining shorter key is called a "screened". In the absence of interception in the communication channel, Alice and Bob have a fully correlated random string of bits.  If the interception took place, the largest error in the resulting classical communication channel, Alice and Bob can estimate the maximum amount of information available to Eve. There is estimation that if an error in the channel is less than about 11%, the information available to Eve, does not exceed the mutual information between Alice and Bob, and the secret data transfer is possible.

- SARG04

*General schematic*:
The SARG04 protocol is aimed at the improvement of the robustness of the main protocols in quantum cryptography (primarily, BB84 and B92) against the PNS attack in the case of the application of weak coherent pulses instead of the one-particle signals. The SARG04 protocol shares the exact same first phase as BB84. In the second phase, when Alice and Bob determine for which bits their bases matched, Alice does not directly announce her bases. Rather she announces a pair of non-orthogonal states, one of which she used to encode her bit. If Bob used the correct basis, he will measure the correct state. If he chose incorrectly, he will not measure either of Alice's states and he will not be able to determine the bit. Producing multiple photons, however, opens up a new attack known as the photon number splitting (PNS) attack. In PNS, Eve splits off a single photon or a small number of photons from each bit transmission for measurement and allows the rest to pass on to Bob. This would allow Eve to measure her photons without disturbing the photons Bob measures. In addition, the SARG04 protocol is resistant to the PNS because Alice does not directly reveal her bases. She reveals a pair of non-orthogonal states in which the bit might be encoded. If bob chose the correct bases he will discover that he measured one of these two states that Alice revealed. If not Alice and Bob will drop that bit. This means that Eve does not know which bases to use when measuring her copy of the photon even after Alice and Bob agree on the bases used. This forces Eve to guess which will mean she will not know the bit with certainty.
***

3. [Acknowledgements](thanks.md)
4. [Reference](ref.md)
