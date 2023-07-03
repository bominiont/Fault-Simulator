class Node:
    def __init__(self, name, inputs, operator, output):
        self.name = name
        self.inputs = inputs
        self.operator = operator
        self.output = output

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

def construct_circuit(circuit_description):
    circuit = {'A': Node('A', [], None, None),
    'B': Node('B', [], None, None),
    'C': Node('C', [], None, None),
    'D': Node('D', [], None, None)
    }
    for line in circuit_description:
        if line.startswith('net_'):
            node_name, expression = line, circuit_description[line]
            gate_type, inputs = parse_expression(expression)
            circuit[node_name] = Node(node_name,gate_type, inputs)
        elif line.startswith('Z'):
            node_name, expression = line, circuit_description[line]
            gate_type, inputs = parse_expression(expression)
            circuit[node_name] = Node(node_name,gate_type, inputs)
    return circuit

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


booleans = ["A","B","C","D"]
def find_input_nodes(circuit:dict,faulty_node:Node,ans,output):
    for x in circuit.values():
        if faulty_node.name == x.name:
            ans.append(x)
    for y in ans:
        for k in y.inputs:
            if k not in booleans:
                ans.remove(y)
                print(ans,y.name)
                find_input_nodes(circuit,y,ans)
    return ans

def evaluate_circuit(inputs:dict, circuit:dict):
    for node in circuit.values():
        if node.name in booleans:
            node.output = inputs[node.name]
    for node in circuit.values():
        inp=[0,0]
        inp[0] = circuit[node.inputs[0]].output
        inp[1] = circuit[node.inputs[-1]].output
        if node.operator == 'AND':
            circuit[node.name].output = inp[0] & inp[1]
        elif node.operator == 'OR':
            circuit[node.name].output = inp[0] | inp[1]
        elif node.operator == 'NOT':
            circuit[node.name].output = not inp[0]
        elif node.operator == 'XOR':
            circuit[node.name].output = inp[0] ^ inp[1]
    return circuit

input_combinations=generate_input_combinations()

circuit = construct_circuit(circuit_description)

def generate_fault_pattern(circuit,fault_node,fault_type,nodes):
    ans=[]
    find_input_nodes(circuit,circuit[fault_node],ans)
    nodes=[]
    for i in ans:
        for s in i.inputs:
            nodes.append(s)

    if fault_type == "SA0":
        for i in range(len(nodes)):
            
    pass


# Write the output to a file
with open("output.txt", "w") as file:
    file.write("Input Vector: {}\n".format(input_vector))
    file.write("Expected Output: {}\n".format(expected_output))