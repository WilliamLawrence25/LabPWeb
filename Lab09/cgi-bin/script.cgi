#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;

# Configuración de la cabecera
print "Content-type: text/html\n\n";

# Función para procesar el archivo .csv
sub procesar_archivo {
    my ($consulta) = @_;

    my $csv = Text::CSV->new({ binary => 1, auto_diag => 1, sep_char => '|' });

    open my $fh, '<:encoding(utf8)', 'Programas de Universidades.csv' or die "No se pudo abrir el archivo CSV: $!";

    my @resultados;

    while (my $row = $csv->getline($fh)) {
        # Utilizar expresiones regulares para buscar la consulta en los campos deseados
        if (utf8_lc($row->[1]) =~ /$consulta/i || utf8_lc($row->[17]) =~ /$consulta/i) {
            push @resultados, $row;
        }
    }

    close $fh;

    return @resultados;
}

# Función para convertir a minúsculas manteniendo la codificación UTF-8
sub utf8_lc {
    my ($text) = @_;
    return lc(Encode::decode_utf8($text));
}

# Obtener la consulta del formulario
my $cgi = CGI->new;
my $consulta = $cgi->param('consulta') || '';

# Imprimir el formulario HTML
print <<HTML;
<html>
<head>
    <title>Consulta de Universidades Licenciadas</title>
    <style>
        body { font-family: Arial, sans-serif; }
        form { margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Consulta de Universidades Licenciadas</h1>
    <form method="post" action="script.cgi">
        <label for="consulta">Consulta:</label>
        <input type="text" name="consulta" id="consulta" value="$consulta">
        <input type="submit" value="Buscar">
    </form>
    <h2>Resultados:</h2>
HTML

# Procesar la consulta y mostrar resultados
my @resultados = procesar_archivo($consulta);
if (@resultados) {
    print "<table>";
    print "<tr><th>Nombre Universidad</th><th>Periodo Licenciamiento</th><th>Departamento Local</th><th>Denominación Programa</th></tr>";
    foreach my $row (@resultados) {
        print "<tr><td>$row->[0]</td><td>$row->[1]</td><td>$row->[2]</td><td>$row->[3]</td></tr>";
    }
    print "</table>";
} else {
    print "<p>No se encontraron resultados.</p>";
}

print <<HTML;
</body>
</html>
HTML
