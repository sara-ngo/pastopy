(*test function - with no parameters*)
program function1;

var
   a : string;

function printString(a: string): string;
var
   result : string;
begin
   writeln('function works');
end;

begin
   a := 'This is A';
   printString(a);
   writeln(a);
end.