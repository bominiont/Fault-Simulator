# Generate all possible input combinations
def generate_input_combinations():
    input_combinations = []
    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    input_combinations.append({"A":A, "B":B,"C": C,"D": D})
    return input_combinations

# Open the circuit file for reading
file_path = "C:/Users/KHUSHIKA SHRINGI/OneDrive/Documents/example_input.txt"  # Replace "input.txt" with your actual file path
with open(file_path, 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

# Process the lines to extract the circuit description
circuit_description = {}
for line in lines:
    line = line.strip()
    if line:
        # Split the line by '=' to separate the net and expression
        net, expression = line.split('=')
        net = net.strip()
        expression = expression.strip()
        # Add the net and expression to the circuit description dictionary
        circuit_description[net] = expression

class Gate:
    def __init__(self,name, gate_type, inputs):
        self.gate_type = gate_type
        self.name= name
        self.inputs = inputs
        self.output = None

#this will give the correct answer

booleans = ["A","B","C","D"]
def execute(gate:Gate,inputs,copy_circuit):
    ans=[]
    for i in range(len(gate.inputs)):
        if gate.inputs[i] in booleans:
            ans.append( inputs[gate.inputs[i]])
        else:
            ans.append (copy_circuit[gate.inputs[i]].output)
    return ans

def evaluate_circuit(inputs, copy_circuit):
    # Evaluate the circuit
  #  print(copy_circuit,circuit,"eval")
    print(inputs,"inputs")
    for gate in circuit.values():
        inp = execute(gate,inputs,copy_circuit)
      #  print(inp,"INP")
        print(circuit["Z"].output,copy_circuit["Z"].output,"evAL1")
        if gate.gate_type == 'AND':
            copy_circuit[gate.name].output = inp[0] & inp[1]
        elif gate.gate_type == 'OR':
            copy_circuit[gate.name].output = inp[0] | inp[1]
        elif gate.gate_type == 'NOT':
            copy_circuit[gate.name].output = not inp[0]
        elif gate.gate_type == 'XOR':
            print(circuit["Z"].output,copy_circuit["Z"].output,"evAL2a")
            print(copy_circuit[gate.name].output, circuit[gate.name].output)
            store=circuit[gate.name].output 
            copy_circuit[gate.name].output = inp[0] ^ inp[1]
            print(circuit["Z"].output,copy_circuit["Z"].output,"evAL2b")
        print(circuit["Z"].output,copy_circuit["Z"].output,"evAL2")
    return copy_circuit['Z']


def detect_fault(copy_circuit,circuit,input_combinations, fault_node, fault_type):
    correct_output=[]
    print(circuit,copy_circuit,"detect1",circuit["Z"].output,copy_circuit["Z"].output)
    for i in input_combinations:
        result = evaluate_circuit(i, copy_circuit)  
        correct_output.append(result.output)
        print(correct_output)
        print(circuit,copy_circuit,"in detect fault",circuit["Z"].output,copy_circuit["Z"].output,"bef")
        for z in circuit.keys():
            copy_circuit[z] = circuit[z]
        print(circuit,copy_circuit,"in detect fault",circuit["Z"].output,copy_circuit["Z"].output,"af")        
    print(correct_output,fault_node,fault_type)

    faulty_output=[]
    print(circuit,copy_circuit,"detect2",circuit["Z"].output,copy_circuit["Z"].output)
    circuit[fault_node].output = int(fault_type[2])
    copy_circuit[fault_node].output = int(fault_type[2])
    print(circuit,copy_circuit,"detect3",circuit["Z"].output,copy_circuit["Z"].output)
    for i in input_combinations:
        result = evaluate_circuit(i, copy_circuit)  
        faulty_output.append(result.output)
  #      print(circuit,copy_circuit,"in detect fault")
        for z in circuit.keys():
            copy_circuit[z] = circuit[z]
    print(faulty_output)
    print(circuit,copy_circuit,"detect4",circuit["Z"].output,copy_circuit["Z"].output)

def construct_circuit(circuit_description):
    circuit = {}
    copy_circuit={}
    for line in circuit_description:
        if line.startswith('net_'):
            node_name, expression = line, circuit_description[line]
            gate_type, inputs = parse_expression(expression)
            circuit[node_name] = Gate(node_name,gate_type, inputs)
            copy_circuit[node_name] = Gate(node_name,gate_type, inputs)
        elif line.startswith('Z'):
            node_name, expression = line, circuit_description[line]
            gate_type, inputs = parse_expression(expression)
            circuit[node_name] = Gate(node_name,gate_type, inputs)
            copy_circuit[node_name] = Gate(node_name,gate_type, inputs)
    
    return circuit,copy_circuit

def parse_expression(expression):
    gate_type = None
    inputs = []

    if '&' in expression:
        gate_type = 'AND'
        inputs = expression.split(' & ')
    elif '|' in expression:
        gate_type = 'OR'
        inputs = expression.split(' | ')
    elif '~' in expression:
        gate_type = 'NOT'
        inputs = [expression[2:]]
    elif '^' in expression:
        gate_type = 'XOR'
        inputs = expression.split(' ^ ')

    return gate_type, inputs

# Construct the circuit based on the provided circuit description
circuit,copy_circuit = construct_circuit(circuit_description)
print(circuit,copy_circuit,"initi")
# Specify the fault
fault_node = 'net_f'
fault_type = 'SA0'
input_combinations= generate_input_combinations()

detect_fault(copy_circuit,circuit,input_combinations, fault_node, fault_type)
