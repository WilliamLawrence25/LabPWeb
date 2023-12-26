#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;

print "Content-type: text/html\n\n";

my $cgi = CGI->new;
my $expression = $cgi->param('expression');

if ($expression =~ /^([-+]?\d+(\.\d+)?)\s*([\+\-\*\/])\s*([-+]?\d+(\.\d+)?)$/) {
    my $operand1 = $1;
    my $operator = $3;
    my $operand2 = $4;

    my $result;
    eval {
        $result = eval "$operand1 $operator $operand2";
    };

    if ($@) {
        print "Error al calcular la expresión.";
    } else {
        print "El resultado es: $result";
    }
} else {
    print "Expresión no válida. Por favor, ingrese una expresión aritmética válida.";
}
