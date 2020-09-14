#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from qiskit import(QuantumCircuit, execute, Aer)


# In[3]:


qc = QuantumCircuit(2,2)
#First a RY(np.pi/2) gate and then RX(np.pi) gate on qubit 0 to obtain a H gate with a phase.
qc.ry((np.pi/2), 0)
qc.rx((np.pi),0)
#Second a RX(np.pi) gate on qubit 1 to obtain a X gate with a phase.
qc.rx((np.pi),1)
#Third a CX gate on control qubit 0 and target qubit 1
qc.cx(0,1)
qc.barrier()
#Finally the measurement
qc.measure([0,1],[0,1])
qc.draw()


# In[4]:


#Simulation for 1 measurement
#We use qams_simulator which is Noisy quantum circuit simulator backend.
simulator = Aer.get_backend('qasm_simulator')
job=execute(qc, simulator,shots=1)
result = job.result()
counts= result.get_counts(qc)
print("\nTotal count for 01 and 10 are:",counts)


# In[5]:


#Simulation for 10 measurements
simulator = Aer.get_backend('qasm_simulator')
job=execute(qc, simulator,shots=10)
result = job.result()
counts= result.get_counts(qc)
print("\nTotal count for 01 and 10 are:",counts)


# In[6]:


#Simulation for 100 measurements
simulator = Aer.get_backend('qasm_simulator')
job=execute(qc, simulator,shots=100)
result = job.result()
counts= result.get_counts(qc)
print("\nTotal count for 01 and 10 are:",counts)


# In[7]:


#Simulation for 1000 measurements
simulator = Aer.get_backend('qasm_simulator')
job=execute(qc, simulator,shots=1000)
result = job.result()
counts= result.get_counts(qc)
print("\nTotal count for 01 and 10 are:",counts)


# In[8]:


#Simulation for 10000 measurements
simulator = Aer.get_backend('qasm_simulator')
job=execute(qc, simulator,shots=10000)
result = job.result()
counts= result.get_counts(qc)
print("\nTotal count for 01 and 10 are:",counts)


# In[9]:


#I am sure I am producing the correct state because the phase is multiplying the whole state, not just a part.

