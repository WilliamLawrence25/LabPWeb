#! C:\Strawberry\perl\bin\perl.exe
use strict;

sub invertir1 {
  my $entrada=@_;
  my $invertido=reverse $entrada; 
  return $invertido;
}
sub invertir2 {
  my ($entrada)=@_;
  my $longitud=length $entrada;
  my $invertido="";
  for (my $i=$longitud-1; $i>=0; $i--) {
    $invertido.=substr($entrada, $i, 1); 
  }
  return $invertido;
}

print "Ingrese una palabra: ";
my $palabra=<STDIN>;
my $palabraInv=invertir2($palabra);
print "Palabra invertida: $palabraInv\n";