(*test function*)
program exFunction;

var
   a : real;
   b : real;
   ret : real;

function max(): string;
var
   result : string;

begin
   writeln('function max works');
end;

begin
   a := 100;
   b := 200;
   max();
   writeln( 'Max value is : ', a);
end.