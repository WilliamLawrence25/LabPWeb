#!"C:/xampp/perl/bin/perl.exe"
use CGI;
use DBI;

my $user = 'alumno';
my $password = 'pweb1';
my $dsn = "DBI:MariaDB:database=pweb1;host=192.168.0.20";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se pudo conectar!");

my $sth = $dbh->prepare("SELECT Name FROM Actor WHERE ActorID = ?");
$sth->execute(5);
my ($actor_name) = $sth->fetchrow_array;
$sth->finish;

print "Content-type: text/html\n\n";
print "<html><body>";
print "<h2>Nombre del actor con ID 5: $actor_name</h2>";
print "</body></html>";

$dbh->disconnect;
