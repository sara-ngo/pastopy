(*test function*)
program exFunction;

var
   a : string;

function printAstring(): string;
var
   result : string;

begin
   writeln('function printAstring works.');
end;

begin
   a := 'Begin';
   printAstring();
   writeln(a);
end.