program testcase4;

var
    a, b: integer;

begin
    b := 0;
    if b <= 0 then
        writeln('b cannot be equal to 0')
    else
        begin
            a := ((50*2) / b);
            writeln('a = ', a);
        end;
end.