k1 = 1;
k2 = 3;
ko = 30;
lc = .1; // 0.4 0.2 0.1
lc1 = k1 * lc;
lc2 = k2 * lc;
lo = ko  * lc;

// ----------------------------------------------------------------------
//                                Inner Sphere
// ----------------------------------------------------------------------
Point(1) = {0.0,0.0,0.0,lc};
Point(2) = {1,0.0,0.0,lc};
Point(3) = {0,1,0.0,lc};
Point(4) = {-1,0,0.0,lc};
Point(5) = {0,-1,0.0,lc};
Point(6) = {0,0,-1,lc};
Point(7) = {0,0,1,lc};

Circle(1) = {2,1,3};
Circle(2) = {3,1,4};
Circle(3) = {4,1,5};
Circle(4) = {5,1,2};
Circle(5) = {3,1,6};
Circle(6) = {6,1,5};
Circle(7) = {5,1,7};
Circle(8) = {7,1,3};
Circle(9) = {2,1,7};
Circle(10) = {7,1,4};
Circle(11) = {4,1,6};
Circle(12) = {6,1,2};

Line Loop(1) = {2,8,-10};
Line Loop(2) = {10,3,7};
Line Loop(3) = {-8,-9,1};
Line Loop(4) = {-11,-2,5};
Line Loop(5) = {-5,-12,-1};
Line Loop(6) = {-3,11,6};
Line Loop(7) = {-7,4,9};
Line Loop(8) = {-4,12,-6};

Ruled Surface(1) = {1};
Ruled Surface(2) = {2};
Ruled Surface(3) = {3};
Ruled Surface(4) = {4};
Ruled Surface(5) = {5};
Ruled Surface(6) = {6};
Ruled Surface(7) = {7};
Ruled Surface(8) = {8};

// Pointing invard
Surface Loop(1) = {-1,-2,-3,-4,-5,-6,-7,-8};

// ----------------------------------------------------------------------
//                                Outer Cube
// ----------------------------------------------------------------------
d = 50;

Point(8) = {d,-d,-d,lo};
Point(9) = {d,d,-d,lo};
Point(10) = {d,d,d,lo};
Point(11) = {d,-d,d,lo};
Point(12) = {-d,-d,-d,lo};
Point(13) = {-d,d,-d,lo};
Point(14) = {-d,d,d,lo};
Point(15) = {-d,-d,d,lo};

Line(13) = {8,9};
Line(14) = {9,13};
Line(15) = {13,12};
Line(16) = {12,8};

Line(17) = {11,10};
Line(18) = {10,14};
Line(19) = {14,15};
Line(20) = {15,11};

Line(21) = {8,11};
Line(22) = {9,10};
Line(23) = {13,14};
Line(24) = {12,15};

Line Loop(9) =  {13,22,-17,-21};
Line Loop(10) = {14,23,-18,-22};
Line Loop(11) = {15,24,-19,-23};
Line Loop(12) = {16,21,-20,-24};
Line Loop(13) = {17,18,19,20};
Line Loop(14) = {-16,-15,-14,-13};

Plane Surface(9) = {9};
Plane Surface(10) = {10};
Plane Surface(11) = {11};
Plane Surface(12) = {12};
Plane Surface(13) = {13};
Plane Surface(14) = {14};

// ----------------------------------------------------------------------
//                                Inner Sphere 1
// ----------------------------------------------------------------------
b = 2;

p1= 15;
l1= 24;
s1= 14;

Point(p1+2) = {b,0.0,0.0,lc1};
Point(p1+3) = {0,b,0.0,lc1};
Point(p1+4) = {-b,0,0.0,lc1};
Point(p1+5) = {0,-b,0.0,lc1};
Point(p1+6) = {0,0,-b,lc1};
Point(p1+7) = {0,0,b,lc1};

Circle(l1+1) = {p1+2,1,p1+3};
Circle(l1+2) = {p1+3,1,p1+4};
Circle(l1+3) = {p1+4,1,p1+5};
Circle(l1+4) = {p1+5,1,p1+2};
Circle(l1+5) = {p1+3,1,p1+6};
Circle(l1+6) = {p1+6,1,p1+5};
Circle(l1+7) = {p1+5,1,p1+7};
Circle(l1+8) = {p1+7,1,p1+3};
Circle(l1+9) = {p1+2,1,p1+7};
Circle(l1+10) = {p1+7,1,p1+4};
Circle(l1+11) = {p1+4,1,p1+6};
Circle(l1+12) = {p1+6,1,p1+2};

Line Loop(s1+1) = {l1+2,l1+8,-(l1+10)};
Line Loop(s1+2) = {l1+10,l1+3,l1+7};
Line Loop(s1+3) = {-(l1+8),-(l1+9),l1+1};
Line Loop(s1+4) = {-(l1+11),-(l1+2),l1+5};
Line Loop(s1+5) = {-(l1+5),-(l1+12),-(l1+1)};
Line Loop(s1+6) = {-(l1+3),l1+11,l1+6};
Line Loop(s1+7) = {-(l1+7),l1+4,l1+9};
Line Loop(s1+8) = {-(l1+4),l1+12,-(l1+6)};

Ruled Surface(s1+1) = {s1+1};
Ruled Surface(s1+2) = {s1+2};
Ruled Surface(s1+3) = {s1+3};
Ruled Surface(s1+4) = {s1+4};
Ruled Surface(s1+5) = {s1+5};
Ruled Surface(s1+6) = {s1+6};
Ruled Surface(s1+7) = {s1+7};
Ruled Surface(s1+8) = {s1+8};

// ----------------------------------------------------------------------
//                                Outer Sphere 2
// ----------------------------------------------------------------------
b = 5;

p1= 15+p1;
l1= 24+l1;
s1= 14+s1;

Point(p1+2) = {b,0.0,0.0,lc2};
Point(p1+3) = {0,b,0.0,lc2};
Point(p1+4) = {-b,0,0.0,lc2};
Point(p1+5) = {0,-b,0.0,lc2};
Point(p1+6) = {0,0,-b,lc2};
Point(p1+7) = {0,0,b,lc2};

Circle(l1+1) = {p1+2,1,p1+3};
Circle(l1+2) = {p1+3,1,p1+4};
Circle(l1+3) = {p1+4,1,p1+5};
Circle(l1+4) = {p1+5,1,p1+2};
Circle(l1+5) = {p1+3,1,p1+6};
Circle(l1+6) = {p1+6,1,p1+5};
Circle(l1+7) = {p1+5,1,p1+7};
Circle(l1+8) = {p1+7,1,p1+3};
Circle(l1+9) = {p1+2,1,p1+7};
Circle(l1+10) = {p1+7,1,p1+4};
Circle(l1+11) = {p1+4,1,p1+6};
Circle(l1+12) = {p1+6,1,p1+2};

Line Loop(s1+1) = {l1+2,l1+8,-(l1+10)};
Line Loop(s1+2) = {l1+10,l1+3,l1+7};
Line Loop(s1+3) = {-(l1+8),-(l1+9),l1+1};
Line Loop(s1+4) = {-(l1+11),-(l1+2),l1+5};
Line Loop(s1+5) = {-(l1+5),-(l1+12),-(l1+1)};
Line Loop(s1+6) = {-(l1+3),l1+11,l1+6};
Line Loop(s1+7) = {-(l1+7),l1+4,l1+9};
Line Loop(s1+8) = {-(l1+4),l1+12,-(l1+6)};

Ruled Surface(s1+1) = {s1+1};
Ruled Surface(s1+2) = {s1+2};
Ruled Surface(s1+3) = {s1+3};
Ruled Surface(s1+4) = {s1+4};
Ruled Surface(s1+5) = {s1+5};
Ruled Surface(s1+6) = {s1+6};
Ruled Surface(s1+7) = {s1+7};
Ruled Surface(s1+8) = {s1+8};

// ----------------------------------------------------------------------
//                     A Cylinder to capture wake 
// ----------------------------------------------------------------------
p2= 15+p1;
l2= 24+l1;
s2= 14+s1;

Point(p2+2) = {d*3/4 , 0  , b    , lc2};
Point(p2+3) = {d*3/4 , b  , 0    , lc2};
Point(p2+4) = {d*3/4 , 0  , -b    , lc2};
Point(p2+5) = {d*3/4 , -b , 0    , lc2};
Point(p2+6) = {d*3/4 , 0  , 0    , lc2};

Point(p2+7) = {6 , 0  , b    , lc2};
Point(p2+8) = {6 , b  , 0    , lc2};
Point(p2+9) = {6 , 0  , -b    , lc2};
Point(p2+10) = {6 , -b , 0    , lc2};
Point(p2+11) = {6 , 0  , 0    , lc2};

Line(l2+2) = {p2+7, p2+2}; 
Line(l2+3) = {p2+8, p2+3}; 
Line(l2+4) = {p2+9, p2+4}; 
Line(l2+5) = {p2+10, p2+5};

Circle(l2+6) = {p2+2, p2+6, p2+3};
Circle(l2+7) = {p2+3, p2+6, p2+4};
Circle(l2+8) = {p2+4, p2+6, p2+5};
Circle(l2+9) = {p2+5, p2+6, p2+2};

Circle(l2+10) = {p2+7, p2+11, p2+8};
Circle(l2+11) = {p2+8, p2+11, p2+9};
Circle(l2+12) = {p2+9, p2+11, p2+10};
Circle(l2+13) = {p2+10, p2+11, p2+7};

Line Loop(s2+1) = {l2+2, l2+6, -(l2+3), -(l2+10)};
Line Loop(s2+2) = {l2+3, l2+7, -(l2+4), -(l2+11)};
Line Loop(s2+3) = {l2+4, l2+8, -(l2+5), -(l2+12)};
Line Loop(s2+4) = {l2+5, l2+9, -(l2+2), -(l2+13)};

Ruled Surface(s2+1) = {s2+1};
Ruled Surface(s2+2) = {s2+2};
Ruled Surface(s2+3) = {s2+3};
Ruled Surface(s2+4) = {s2+4};

// ----------------------------------------------------------------------
//                                Volume
// ----------------------------------------------------------------------

// Pointing Outward
Surface Loop(2) = {9,10,11,12,13,14};

// The volume
Volume(1) = {2,1};

Surface{+14+1,+14+2,+14+3,+14+4,+14+5,+14+6,+14+7,+14+8} In Volume {1};
Surface{+s1+1,+s1+2,+s1+3,+s1+4,+s1+5,+s1+6,+s1+7,+s1+8} In Volume {1};
Surface {s2+1, s2+2, s2+3, s2+4} In Volume {1};

Physical Volume(1) = {1};
Physical Surface(5) = {9,10,11,12,13,14};
Physical Surface(1) = {1,2,3,4,5,6,7,8};

