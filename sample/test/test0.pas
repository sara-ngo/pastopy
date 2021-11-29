program testcase0;

var
    a, b, c, d : integer;

begin
    a := 10;
    b := 2;
    c := (a * b);
    d := (a % b);
    writeln('a * b =', c);
    writeln('a mod b =', d);
end.