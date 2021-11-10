(* LET <var1> = <var2>;
throw error if var1 is undefined - unfinished*)

var
  a, b: integer;

begin
  a := 10;
  b := a;
  writeln('a = ', a);
  writeln('b = ', b);
end.