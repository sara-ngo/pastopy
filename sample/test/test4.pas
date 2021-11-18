(* LET <var1> = ((num1 * num2) / <var2>);
type real instead of integer
if var2 is not an integer or is null, throw an error - unfinished
throws error if div by zero - unfinished
all div will be int div - unfinished *)

program testcase4;

var
    a, b: integer;

begin
    b := 0;
    if b <= 0 then
        writeln('b cannot be equal to 0')
    else
        begin
            a := ((50*2) / b);
            writeln('a = ', a);
        end;
end.