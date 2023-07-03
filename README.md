# Fault-Simulator

This Python code solves the problem of identifying a fault at a given node in a circuit and generating the input vector required to detect the fault. It uses circuit simulation techniques to evaluate the circuit and determine the fault.

## Problem Statement

The problem is to design an algorithm and write code to identify a fault at a given node in a circuit and generate the input vector required to detect the fault. The circuit is built using AND, OR, NOT, and XOR gates, and has 4 boolean inputs. The fault types can be SA0 (stuck-at-0) or SA1 (stuck-at-1). The code should output the input vector and the expected value of the final output to confirm the fault.

## Approach

1. Read the circuit file and fault information.
2. Evaluate the circuit using the given inputs and gates.
3. Generate the input pattern to test the fault by setting the appropriate values at the inputs participating in the faulty node output.
4. Evaluate the circuit for two cases: one where the output at the faulty node is set to 1 and the other where it is set to 0.
5. Print the input vector and the expected value of the final output (Z) to confirm the fault detection.
6. Write the output to a file named "output.txt" in the run directory.

## Usage

1. Install Python (version 3.10.8 or higher) on your system.
2. Clone the repository or download the code files.
3. Modify the circuit file and fault information as required.
4. Run the code using the command: `python fault_detection.py`
5. Check the "output.txt" file for the generated input vector and expected output.

## Dependencies

This code does not require any external libraries or dependencies. It uses standard Python libraries for file handling and circuit simulation.

## Limitations

- The code assumes a fixed circuit format with 4 inputs and specific gate types.
- It only supports SA0 and SA1 fault types.
- It does not handle circuit files with complex logic or multiple faults.

## Contributors

- KhushikaShringi khushikashringi09@gmail.com

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
```

Please modify the information in the README file according to your specific implementation and include any additional details you find relevant.
