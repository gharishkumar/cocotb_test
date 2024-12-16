import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_and_gate(dut):
    """Test the AND gate with all possible input combinations."""

    for a in [0, 1]:
        for b in [0, 1]:
            dut.a.value = a
            dut.b.value = b

            await Timer(10, units='ns')  # wait for 10 nanoseconds

            assert dut.y.value == a & b, f"Test failed with a={a}, b={b}, y={dut.y.value}"
            print(f"Test passed with a={a}, b={b}, y={dut.y.value}")
