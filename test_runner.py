import cocotb_test.simulator
import os

def test_and_gate():
    # Define the path to the Verilog source file and the test module
    verilog_sources = [os.path.join(os.getcwd(), "and_gate.v")]

    # Run the test
    cocotb_test.simulator.run(
        verilog_sources=verilog_sources,
        toplevel="and_gate",
        module="test_and_gate",
        simulator="questa"
    )

if __name__ == "__main__":
    test_and_gate()
