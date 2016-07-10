import numpy as np
import math



class Qubit:
    
    def __init__(self,state_1=None):
        if state_1 == None:
            state_1 = np.random.choice([1/math.sqrt(2),-1/math.sqrt(2)])
        state_2 = math.sqrt(1-(state_1**2))
        self.qubit = np.array([state_1,state_2])
    
    def __repr__(self): #a method for outputting a qubit
        return "qubit: " + str(self.qubit)
        
class Entangled_state:
    
    def __init__(self,state_1=None,state_2=None):
        if state_1 == None and state_1 == None:
            state_1 = np.random.choice([1/math.sqrt(2),-1/math.sqrt(2)])
            state_2 = np.random.choice([-1/math.sqrt(2),1/math.sqrt(2)]) 
        self.Bell_state = np.array([state_1,state_1]) * np.array([0 , 1]) + np.array([state_2,state_2]) * np.array([1 , 0])
        
class Hadamard():
    def __init__(self): 
        self.apply_Hadamard = np.array([[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]])
    
    def __repr__(self): #a method for outputting a qubit
        return "Hadamard: " + str(self.apply_Hadamard)

class NOT():
    def __init__(self):
        self.apply_NOT = np.array([[0,1],[1,0]])
        
    def __repr__(self): 
        return "NOT: " + str(self.apply_NOT)
        
        
class Gate_pi():
    def __init__(self):
        p = complex(0,math.pi/4)
        p = p.imag
        self.apply_gate_pi = np.array([[1,0],[0,p]])
        
    def __repr__(self): 
        return "Gate_pi: " + str(self.apply_gate_pi)
        
class Gate_pi8():
    def __init__(self,n):
        p = complex(0,math.pi/8)
        p = p.imag
        self.apply_gate_pi8 = np.array([[math.exp(-p*n),0],[0,math.exp(p*n)]])
        
    def __repr__(self): 
        return "Gate_pi8: " + str(self.apply_gate_pi8)
        
class Gate_turn():
    def __init__(self,turning_sector,number_bas):
        p = complex(0,math.pi/number_bas)
        p = p.imag
        self.apply_gate_turn = np.array([[math.exp(-p*turning_sector),0],[0,math.exp(p*turning_sector)]])
        
    def __repr__(self): 
        return "Gate_turn: " + str(self.apply_gate_turn)
        
class CNOT():
    def __init__(self):
        self.apply_CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
        
    def __repr__(self): 
        return "Gate_CNOT: " + str(self.apply_CNOT)

        


class Actor():
    def __init__(self, number_bas,long_message,index_entanglement):#
        self.long_message = long_message
        self.number_bas = number_bas
        self.index_entanglement = index_entanglement

    def send(self):

        a=0
        self.message_qubit = []
        self.normal_view = []
        self.randomly_bases=np.random.randint(0,int(self.number_bas),self.long_message)
        while a<self.long_message:
            if self.index_entanglement == 0:
                i=np.random.choice([0,1])
            else:
                i=np.random.choice([-1/(math.sqrt(2)),1/(math.sqrt(2))])
            q=Qubit(i)
            self.message_qubit.append(q.qubit)
            if q.qubit[0] == 1:
                self.normal_view.append(0)
            elif q.qubit[0] == 0:    
                self.normal_view.append(1)
            else :
                self.normal_view.append(np.random.choice([0,1]))
            a=a+1
            
    def send_entangled(self,the_number_of_entangled_qubits_sent):
        a = 0
        self.message_Bell_state = []
        while a < the_number_of_entangled_qubits_sent:
            port = Entangled_state()
            the_number_of_entangled_qubits_sent.append(port.Bell_state)
            a=a+1
            
            

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
       # return self.qubits_alice
         
        
class Eve(Actor):
    
    def initialized(self):
        self.send()
        self.eve_creates_bases = self.randomly_bases
        self.eve_overhears_qubits = self.message_qubit
        self.clog =np.random.randint(1,10)
        self.clog_1 =np.random.randint(1,10)
        
    def intercepts_qubits(self):
        self.eve_overhears_qubits_alice=[]
        a=0
        while a<self.long_message:
            q=Gate_turn(a,self.clog)
            eve_turns_qubit=np.dot(self.eve_overhears_qubits[a],q.apply_gate_turn)
            self.eve_overhears_qubits_alice.append(eve_turns_qubit)
            a=a+1
       # return self.eve_overhears_qubits_alice
                   
        
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
       # return self.qubits_bob
        
class Various_measurement(Alice,Eve,Bob):
    
    def begin(self):
        self.get_randomly_bases_alice()
        self.get_randomly_bases_bob()
        self.send_qubits_alice()
        self.received_qubits_bob()
        self.initialized()
        self.intercepts_qubits()
        
    def intervention(self):
        i=0
        while i<self.long_message:
            if self.she_send_randomly_bases[i]==self.eve_creates_bases[i]:
                self.qubits_alice[i]=self.eve_overhears_qubits_alice[i]
            else:
                self.qubits_alice[i]=self.qubits_alice[i]
            i=i+1
        
    
    def compare_bob_alice(self): #Alice and Bob compare their bases and this
    #forms the following key. If the bases are equal to the true value,
    #if not - then the value of Bob
        self.taken_qubits=[]
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
                if c[0] == 0:
                    self.key.append(1)
                else:
                    self.key.append(0)
            else:
                pass
            i=i+1
            
    def __repr__(self): 
        return "Key: " + str(self.key)
      
        
class Effect:
    
    def __init__(self,gate_impact, state_1=None):
        gate_impact = int(gate_impact)
        if state_1 == None:
            state_1 = np.random.choice([0,1])
        state_2=math.sqrt(1-(state_1**2))
        self.qubit = np.array([[state_1,state_2]])
        if gate_impact == 1:
            a = Hadamard()
            self.impact_result = np.dot(self.qubit,a.apply_Hadamard)
        if gate_impact == 2:
            a = NOT()
            self.impact_result=np.dot(self.qubit,a.apply_NOT)
        if gate_impact == 3:
            a = Gate_pi()
            self.impact_result=np.dot(self.qubit,a.apply_gate_pi)
        if gate_impact == 4:
            a = Gate_pi8()
            self.impact_result=np.dot(self.qubit,a.apply_gate_pi8)
        if gate_impact == 5:
            a = Gate_turn()
            self.impact_result=np.dot(self.qubit,a.apply_gate_turn)
        if gate_impact == 6:
            a = CNOT()
            self.impact_result=np.dot(self.qubit,a.apply_CNOT)
            
class Transformations:
     
    def __init__(self,array_qubits):
        self.array_qubits = array_qubits

    def to_entangle(self):
        a=0
        self.entangle= self.array_qubits[a]
        while a < len(self.array_qubits)-1:
            b=a+1
            if self.entangle == self.array_qubits[b]:
                self.entangle = 0
            else:
                self.entangle = 1
            a=a+1           
            
            
#alica=np.array([0,1,0,1,0,1,1])
#coc = Transformations(alica)
#coc.to_entangle()
#print(coc.entangle)
            
            
            
#a=Alice(4,10,0)
#a.get_randomly_bases_alice()
#a.send_qubits_alice()

#noise=Eve(4,10,0) kto budet chitat' cod? da nicto konechno
#noise.initialized()
#noise.intercepts_qubits()

#b=Bob(4,10,0)
#b.get_randomly_bases_bob()
#b.received_qubits_bob()




        
        
        


