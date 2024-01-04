#!"C:/xampp/perl/bin/perl.exe"
use CGI;
use DBI;

my $user = 'alumno';
my $password = 'pweb1';
my $dsn = "DBI:MariaDB:database=pweb1;host=192.168.0.20";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se pudo conectar!");

my $sth = $dbh->prepare("SELECT * FROM Movie WHERE Year = ?");
$sth->execute(1985);

print "Content-type: text/html\n\n";
print "<html><body>";
print "<h2>Películas de 1985</h2>";
print "<table border='1'><tr><th>Title</th><th>Year</th><th>Director</th></tr>";
while (my ($title, $year, $director) = $sth->fetchrow_array) {
    print "<tr><td>$title</td><td>$year</td><td>$director</td></tr>";
}
print "</table>";
print "</body></html>";

$dbh->disconnect;
