program maxFunc;

var
   a, b, ret : real;

function max(num1, num2: real): real;
var
   result : real;
begin
   if (num1 > num2) then
      result := num1
   else
      result := num2;
   max := result;
end;

begin
   a := 100;
   b := 200;
   ret := max(a, b);
   writeln( 'Max value is :', ret);
end.