
nbr_letras = 1;

nbr1 = 1;
nbr2 = 1;
nbr3 = 0;
nbr4 = 0;
nbr5 = 1;
nbr6 = 0;


//base
cube([90, 120, 10]);
//1
if ( nbr1 == 1){
translate([30, 90, 10])
sphere(r = 10, $fn= 20);
}

//2
if ( nbr2 == 1){
translate([60, 90, 10])
sphere(r = 10, $fn= 20);
}

//3
if ( nbr3 == 1){
translate([30, 60, 10])
sphere(r = 10, $fn= 20);
}

//4
if ( nbr4 == 1){
translate([60, 60, 10])
sphere(r = 10, $fn= 20);
}

//5
if ( nbr5 == 1){
translate([30, 30, 10])
sphere(r = 10, $fn= 20);
}

//6
if ( nbr6 == 1){
translate([60, 30, 10])
sphere(r = 10, $fn= 20);
}