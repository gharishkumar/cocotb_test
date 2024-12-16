// and_gate.v
module and_gate (
    input wire clk,
    input wire a,
    input wire b,
    output wire y
);
    assign y = a & b;
endmodule