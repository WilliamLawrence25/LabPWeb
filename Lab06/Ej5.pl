#! C:\Strawberry\perl\bin\perl.exe
use strict;
use warnings;

sub celebridad {
  my @matriz=@_;

  my $numPers=scalar @matriz;
  my $celebridad0=0;
  for my $i (1..$numPers-1) {
    if ($matriz[$celebridad0][$i]) {
      $celebridad0=$i;
    }
  }
  for my $i (0..$numPers-1) {
    next if $i==$celebridad0; 
    if ($matriz[$celebridad0][$i] or !$matriz[$i][$celebridad0]) {
      return "No hay celebridad";
    }
  }
  return "La celebridad es la persona $celebridad0";
}

my @matriz=([0, 1, 1, 0],
              [0, 0, 0, 0],
              [1, 1, 0, 1],
              [0, 1, 0, 0]);
    
print celebridad(@matriz)."\n";
