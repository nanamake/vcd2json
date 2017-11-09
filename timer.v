`timescale 1ns/1ns

module timer (
    input           clock,
    input           reset,
    output  reg     pulse
);

    reg [3:0]   count;
    wire        count_eq11;

    always @(posedge clock) begin
        if (reset | count_eq11) begin
            count <= 4'd0;
        end else begin
            count <= count + 1'b1;
        end
    end

    assign  count_eq11 = (count == 4'd11);

    always @(posedge clock) begin
        pulse <= count_eq11;
    end

endmodule


module tb_timer;

    reg     clock;
    reg     reset;
    wire    pulse;

    timer u_timer (
        .clock  (clock  ),
        .reset  (reset  ),
        .pulse  (pulse  )
    );

    initial begin
        forever begin
            clock = 0; #10;
            clock = 1; #10;
        end
    end

    initial begin
        reset = 0;
        repeat(5) @(posedge clock);
        reset <= 1;
        repeat(5) @(posedge clock);
        reset <= 0;
    end

    initial begin
        forever begin
            @(reset);
            $display("reset=%b at time %0d", reset, $time);
        end
    end

    initial begin
        forever begin
            @(pulse);
            $display("pulse=%b at time %0d", pulse, $time);
        end
    end

    initial begin
        #1000;
        $display("Simulation finished.");
        $finish;
    end

    initial begin
        $dumpfile("timer.vcd");
        $dumpvars(0, tb_timer);
    end

endmodule
