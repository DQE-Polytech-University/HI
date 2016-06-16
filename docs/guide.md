# HIDDEN INFORMATION Documentation
1. [Preface](index.md)
2. [User's Guide](guide.md)
***

## Quantum Cryptography
Quantum cryptography is the science of exploiting quantum mechanical properties to perform cryptographic tasks. The main advantage of the quantum cryptographic protocol is the inability to make the interference goes unnoticed. it is connected with the property of the wave function which means that any change in the quantum system changes its initial state. When an attacker is trying to find out information he inevitably makes a mistake. When an error is close to the critical value (depending on the protocol) key length tends to zero  and key transfer becomes impossible. The more critical error the more stable system.

We consider one of the confidential information transmission technology. Send the message over the open channel but *specially encrypted*. It is understood the impossibility of obtaining useful information without the *secret key*.
### QKD Protocols
- BB84

[How does the protocol bb84 work?](/https://github.com/DQE-Polytech-University/HI/blob/master/img/bb84-en.jpg)
![](/img/bb84-en.jpg)

*General schematic*:
Traditionally, cryptography legitimate users can be designated as Alice and Bob, and the attacker called Eve. So, let's describe the situation in the cryptographic protocol. Alice needs to send a secret message to Bob, and Eve all the means at its disposal tries to intercept it. In the first stage Alice sends photons to Bob in some arbitrarily chosen basis. Some photons may be sent together or one after the other but there is a limit: Alice and Bob need to establish a one-to-one correspondence between the sent and received photon. Bob measures the received photons in one of the two bases, and arbitrarily selected (regardless of the Alice's choice). At this stage in the case of identical bases they get results completely correlated. However, if they use different bases obtained results uncorrelated. On average, Bob receives a bit string with a 25% error, called a primary key. This error is so large that the use of conventional error correction algorithm is impossible. Nevertheless, it is possible to carry out the following procedure, called matching bases. For each passed state Bob openly reported in which we measured the qubit basis (but does not report the results of measurements). Alice then tells when its base coincides with Bob's base. If the bases are matched -  bit is left, but if not, ignore it. In this case, approximately 50% of the data is discarded. The remaining shorter key is called a "screened". In the absence of interception in the communication channel, Alice and Bob have a fully correlated random string of bits.  If the interception took place, the largest error in the resulting classical communication channel, Alice and Bob can estimate the maximum amount of information available to Eve. There is estimation that if an error in the channel is less than about 11%, the information available to Eve, does not exceed the mutual information between Alice and Bob, and the secret data transfer is possible.

- SARG04

*General schematic*:
The SARG04 protocol is aimed at the improvement of the robustness of the main protocols in quantum cryptography (primarily, BB84 and B92) against the PNS attack in the case of the application of weak coherent pulses instead of the one-particle signals. The SARG04 protocol shares the exact same first phase as BB84. In the second phase, when Alice and Bob determine for which bits their bases matched, Alice does not directly announce her bases. Rather she announces a pair of non-orthogonal states, one of which she used to encode her bit. If Bob used the correct basis, he will measure the correct state. If he chose incorrectly, he will not measure either of Alice's states and he will not be able to determine the bit. Producing multiple photons, however, opens up a new attack known as the photon number splitting (PNS) attack. In PNS, Eve splits off a single photon or a small number of photons from each bit transmission for measurement and allows the rest to pass on to Bob. This would allow Eve to measure her photons without disturbing the photons Bob measures. In addition, the SARG04 protocol is resistant to the PNS because Alice does not directly reveal her bases. She reveals a pair of non-orthogonal states in which the bit might be encoded. If bob chose the correct bases he will discover that he measured one of these two states that Alice revealed. If not Alice and Bob will drop that bit. This means that Eve does not know which bases to use when measuring her copy of the photon even after Alice and Bob agree on the bases used. This forces Eve to guess which will mean she will not know the bit with certainty.

## HI Library

### Concept

### Algorithm

    class Qubit:
    def __init__(self,state_1=None):
    if state_1==None:
    state_1=np.random.random()
    state_2=math.sqrt(1-(state_1**2))
    self.qubit=np.array([[state_1,state_2]])
    def __repr__(self):
    return "qubit: " + str(self.qubit)

Class for qubit describes the state of the qubit on the Bloch sphere, excluding the corners. First, give the state of the vector `def __init__(self,state_1=None):`. If the state_1 is not set then it's entangled states. In other cases, the states are 1 or 0.
Function `def __repr__(self): return "qubit: " + str(self.qubit)` is required to display the qubit on the screen.
In order to set the qubit introduce (the user enters values 1 or 0):

  particle= Qubit(1)
  particle. qubit

Move on to the implementation of Hadamard gate:

    class Hadamard():
    def __init__(self):
    self.apply_Hadamard = np.array([[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]])
    def __repr__(self): #a method for outputting a qubit
    return "Hadamard: " + str(self.apply_Hadamard)

Hadamard Gate is one of the most useful quantum gates. This gate is sometimes defined as "the square root of NOT gate.
This is due to the fact that the gate converts `|0>` part of a qubit in `(|0>+|1>)/√2`. It as a half of way between `|0>` and `|1>` states in the geometric interpretation of the qubit on the Bloch sphere. Accordingly, in the `|1>` part of the qubit Hadamard gate is converted into a combination of `(|0> - |1>)/√2`, which is also a half of way between `|0>` and `|1>`. However, H^2^ gate does not lead to NOT gate, as the algebraic calculations give H^2^ ≡ I. A twofold use of the gate H returns system an initial position. Function looks like this

    matrix= Hadamard()
    matrix. apply_Hadamard

Write class NOT:

    class NOT():
    def __init__(self):
    self.apply_NOT = np.array([[0,1],[1,0]])
    def __repr__(self):
    return "NOT: " + str(self.apply_NOT)

Class changes the state places. That is, of the qubit, which is determined by the matrix (0,1) is obtained (1,0)

Phase gate class:

    class Gate_pi():
    def __init__(self):
    p = complex(0,math.pi/4)
    p = p.imag
    self.apply_gate_pi = np.array([[1,0],[0,p]])
    def __repr__(self):
    return "Gate_pi: " + str(self.apply_gate_pi)

This class needs to rotate the basis vectors at an angle of pi/4. Here, the user does not need to enter anything.

    class Gate_pi8():
    def __init__(self,n):
    p = complex(0,math.pi/8)
    p = p.imag
    self.apply_gate_pi8 = np.array([[math.exp(-p*n),0],[0,math.exp(p*n)]])
    def __repr__(self):
    return "Gate_pi8: " + str(self.apply_gate_pi8)

Phase gate class needs to rotate the basis vectors to pi/8 angle. The user needs to enter the base number to which he wants to turn the vector with respect to the zero base:

    matrix= Gate_pi8 (enter the basis)
    matrix. apply_gate_pi8

Phase gate class needs to rotate the basis vectors at any angle you want.

    class Gate_turn():
    def __init__(self,n,number_bas):
    p = complex(0,math.pi/number_bas)
    p = p.imag
    self.apply_gate_turn = np.array([[math.exp(-p*n),0],[0,math.exp(p*n)]])
    def __repr__(self):
    return "Gate_turn: " + str(self.apply_gate_turn)

You must enter the two elements - basis and turning step:

    matrix= Gate_turn (base number, total number of bases)
    matrix. apply_gate_turn

Two-bit gate acts on the two qubits. Turning their condition:

    class CNOT():
    def __init__(self):
    self.apply_CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    def __repr__(self):
    return "Gate_CNOT: " + str(self.apply_CNOT)

Generator Class. The user needs to enter the amount of bases used in the protocol, the length of the message that will pass (number of transmitted qubits), entanglement index (0 defines a mixed state, if nothing is entered, the state will become confused). `def send(self)` metod transfer qubits: messages may be selected randomly from the bases, then formed the transmitted qubits:

    generator = Actor(the amount of used bases, the length of the message, entanglement index):
    generator. send()
    generator. randomly_bases
    generator. message_qubit

Class for Alice.

    class Alice(Actor):#Here they take their randomly values
    def get_randomly_bases_alice(self):
    self.send()
    self.she_send_randomly_bases=self.randomly_bases
    return self.she_send_randomly_bases
    def send_qubits_alice(self):
    self.qubits_alice=[]
    i=0
    while i<self.long_message:
    q=Gate_turn(self.she_send_randomly_bases[i],self.number_bas)
    c=np.dot(self.message_qubit[i],q.apply_gate_turn)
    self.qubits_alice.append(c)
    i=i+1

It takes the oscillator method and forms the message from a randomly bases. Depending on the selected base turns qubits, acting on their phase rotary gate `Gate_turn a=Alice` (the amount of used bases, the length of the message, entanglement index), `a.get_randomly_bases_alice()` Alice gets random bases, `a.send_qubits_alice()` Alice sends the qubits.

Class for Eve.

    class Eve(Alice,Actor):
    def initialized(self):
    self.send()
    self.eve_send_randomly_bases=self.randomly_bases
    self.get_randomly_bases_alice()
    self.send_qubits_alice()
    self.qubits_alice
    twist=np.random.randint(2,10)
    self.clog =np.random.randint(1,twist-1)
    def intercepts_qubits(self):
    self.initialized()
    a=0
    while a<self.long_message:
    if self.eve_send_randomly_bases[a]==self.she_send_randomly_bases[a]:
    q=Gate_turn(a,self.clog)
    c=np.dot(self.qubits_alice[a],q.apply_gate_turn)
    self.qubits_alice[a]=c
    else:
    pass
    a=a+1
    def removes_qubits(self):
    self.initialized()
    a=0
    while a<self.long_message:
    if self.eve_send_randomly_bases[a] == self.she_send_randomly_bases[a]:
    self.qubits_alice.pop(a)
    else:
    pass
    a=a+1
    def add_qubits(self):
    self.initialized()

Eve can change the qubits, turning them. If the bases are formed by Alice and Eve coincided with the method `def intercepts_qubits(self):`. Eva can delete qubits (withdraw them from the transfer) with the method `def removes_qubits(self):`. Eve can add to the message qubits, with its polarization `def add_qubits(self):`. Number of used bases, length of message, entanglement index `noise=Eve`. Eva initiates communication with Alice `noise.initialized()`. After the point you need to write a method. In our case it turns qubits that are guessed, and introduces an error `noise.intercepts_qubits()`.

Class for Bob.

    class Bob(Actor):
    def get_randomly_bases_bob(self):
    self.send()
    self.he_send_randomly_bases=self.randomly_bases
    return self.he_send_randomly_bases
    def received_qubits_bob(self):
    self.qubits_bob=[]
    i=0
    while i<self.long_message:
    q=Gate_turn(self.he_send_randomly_bases[i],self.number_bas)
    c=np.dot(self.message_qubit[i],q.apply_gate_turn)
    self.qubits_bob.append(c)
    i=i+1

Bob takes the oscillator method and forms the message from a randomly bases. Depending on the selected base turns qubits, acting on their phase rotary gate `Gate_turn`. Number of used bases, length of message, entanglement index `b=Bob`. Bob gets random bases `b.get_randomly_bases_bob()`. Bob gets measured qubits `b.received_qubits_bob()`.

Various operations whith qubits.

class Various_measurement(Alice,Bob,Actor):

    def compare_bob_alice(self): #Alice and Bob compare their bases and this
    #forms the following key. If the bases are equal to the true value,
    #if not - then the value of Bob
    self.taken_qubits=[]
    self.get_randomly_bases_alice()
    self.get_randomly_bases_bob()
    self.send_qubits_alice()
    self.received_qubits_bob()
    i=0
    while i < self.long_message:
    if self.she_send_randomly_bases[i] == self.he_send_randomly_bases[i]:
    self.taken_qubits.append(self.qubits_alice[i])
    else:
    self.taken_qubits.append(self.qubits_bob[i])
    i=i+1
    return self.taken_qubits

    def generate_key(self): #generated by the key itself on the trail
    self.key=[]
    i=0
    while i < self.long_message:
    if self.she_send_randomly_bases[i] == self.he_send_randomly_bases[i]:
    c=self.taken_qubits[i]
    if c[0][0]==0:
    self.key.append(1)
    else:
    self.key.append(0)
    else:
    pass

Various operations qubits are determined by comparing the bases, if Bob guesses the basis correctly, the Alice's qubit is taken , if not, a qubit comes erroneous `def compare_bob_alice(self)`. Number of used bases, length of message, entanglement index `c=Various_measurement`. Alice's and Bob's bases are compared, forming an array of received qubits `c.compare_bob_alice()`. A key is shaped `c.generate_key()`.

### Features

The library allows to create a tool for prototyping protocols of quantum key distribution. It is useful for the study and debugging of quantum protocols. Classes for qubits, methods of generating and receiving messages key are universal and can be used for various tasks of quantum cryptography. The library is a block of code, in which the user can insert  data and obtain the desired result. Using the blocks described above.

### Examples

An example of the key formation of BB84 protocol with Eve's participation:

    a=Alice(4,10,0)
    a.get_randomly_bases_alice()
    a.send_qubits_alice()
    noise=Eve(4,10,0)
    noise.initialized()
    noise.intercepts_qubits()

    b=Bob(4,10,0)
    b.get_randomly_bases_bob()
    b.received_qubits_bob()

    c=Various_measurement(4,10,0)
    c.compare_bob_alice()
    c.generate_key()
    print(c.key)

An example of the key formation of BB84 protocol without Eve's participation:

    a=Alice(4,10,0)
    a.get_randomly_bases_alice()
    a.send_qubits_alice()

    b=Bob(4,10,0)
    b.get_randomly_bases_bob()
    b.received_qubits_bob()

    c=Various_measurement(4,10,0)
    c.compare_bob_alice()
    c.generate_key()
    print(c.key)

***

3. [Acknowledgements](thanks.md)
4. [Reference](ref.md)
