(*test function - with parameters*)
program function2;

var
   a, b, res : real;

function total(num1, num2: real): real;
var
   result : real;

begin
   result := num1 + num2;
   sum := result;
end;

begin
   a := 100;
   b := 200;
   res := total(a, b);
   writeln( 'Total is :', res);
end.