(*test function*)
program exFunction;

var
   a : real;
   b : real;
   ret : real;

function max(): string;
var
   result : real;

begin
   writeln('works');
end;

begin
   a := 100;
   b := 200;
   max(); //work with empty arg
   writeln( 'Max value is : ', a);
end.