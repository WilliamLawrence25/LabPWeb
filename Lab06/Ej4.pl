#! C:\Strawberry\perl\bin\perl.exe
use List::Util qw(min max);
use strict;
use warnings;

sub encontrarPosicion {
  my ($eliminar, @array)=@_;
  my $posicion=-1;
  for my $i (0..$#array){
    if($array[$i]==$eliminar){
      $posicion=$i;
      last;
    }
  }
  return $posicion;
}

sub eliminar_duplicar {
  my @notas=@_;
  my $min=min @notas;
  my $posicionMin=encontrarPosicion($min, @notas);
  splice(@notas, $posicionMin, 1);

  my $max=max @notas;
  my $posicionMax=encontrarPosicion($max, @notas);
  splice(@notas, $posicionMax, 0, $notas[$posicionMax]);

  return @notas;
}

sub promedio {
  my @notas=@_;
  my $promedio=0;
  for my$i (0..$#notas){
    $promedio+=$notas[$i];
  }
  return ($promedio/scalar @notas);
}

print "Ingrese las notas :";
my $notas=<STDIN>;
my @arreglo=split(' ', $notas);  
my @notas1=eliminar_duplicar(@arreglo);
my $promedio=promedio(@notas1);
$promedio=sprintf("%.2f", $promedio);
print "\nArray modificado: @notas1\n";
print "Promedio de las notas: $promedio";