#!"C:/xampp/perl/bin/perl.exe"
use CGI;
use DBI;

my $cgi = CGI->new;
my $anio = $cgi->param('anio');

my $user = 'alumno';
my $password = 'pweb1';
my $dsn = "DBI:MariaDB:database=pweb1;host=192.168.0.20";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se pudo conectar!");

my $sth = $dbh->prepare("SELECT * FROM Movie WHERE Year = ?");
$sth->execute($anio);

print "Content-type: text/html\n\n";
print "<html><body>";
print "<h2>Películas del año $anio</h2>";
print "<table border='1'><tr><th>Title</th><th>Year</th><th>Director</th></tr>";
while (my ($title, $year, $director) = $sth->fetchrow_array) {
    print "<tr><td>$title</td><td>$year</td><td>$director</td></tr>";
}
print "</table>";
print "</body></html>";

$dbh->disconnect;
