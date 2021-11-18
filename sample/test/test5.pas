(* PRINT(<var1>);
throw error if undefined - unfinished*)
program testcase5;

var
  a: integer;

begin
    a := 2024;
    if a < 2022 then
        writeln(a)
    else
        writeln('we are living the future.');
end.