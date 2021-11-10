(* LET <var1> = ((num1 * num2) / <var2>);
type real instead of integer
a :5 :1 for numbers after decimal
if var2 is not an integer or is null, throw an error - unfinished
throws error if div by zero - unfinished
all div will be int div - unfinished*)

var
    a, b: real;

begin
    b := 25;
    a := ((50*2) / b);
    write('a = ', a :5 :1)
end.