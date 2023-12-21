#! C:\Strawberry\perl\bin\perl.exe
use strict;

sub numMayor{
  my @entrada=@_;
  my $mayor=$entrada[0];
  for my $numero (@entrada) {
    if ($numero > $mayor) {
      $mayor = $numero;
    }
  }
  return $mayor;
}

print "Ingrese un arreglo de numeros: ";
my $numeros=<STDIN>;
my @arreglo=split ' ', $numeros;
my $numero_mayor=numMayor(@arreglo);

print "El numero mayor es: $numero_mayor\n";
