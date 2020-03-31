import qiskit as qk

#create qubits
q=qk.QuantumRegister(2)

#create classic bits
c=qk.ClassicalRegister(2)
circuit=qk.QuantumCircuit(q,c)

#Hadamard Gate on first qubit
circuit.h(q[0]),
circuit.h(q[1])

#CNOT Gate on first and second qubit
circuit.cx(q[0],q[1])

#measure qubits
circuit.measure(q,c)

print (circuit)
