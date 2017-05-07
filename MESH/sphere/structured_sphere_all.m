global g
g.level = 5;
# ---------------------------------------------------------------------------
#                              Functions 
# ---------------------------------------------------------------------------

# Init
function init
  global g

  g.fid = fopen( sprintf("sphere_m%d.geo", g.level) , "w");
  g.ip = 1;

  g.PHI = 2*pi/4;
  g.THETA = 0.937638; #ideal: \pi-2\theta=\sin(\theta)* \pi/2

endfunction

# Finalize
function finish
  global g

  fclose(g.fid);

endfunction

# Write a point with x,y,z
function p=write_point(x,y,z,l)
  global g
  p = g.ip;
  g.ip = g.ip + 1;

  fprintf(g.fid, "Point(%d) = {%.16f, %.16f, %.16f, %e}; \n", p, x, y, z, l);
endfunction

# Write a point with r,phi,theta
function p=write_point_sphere(r,phi,theta,l)
  global g
  p = g.ip; 
  g.ip = g.ip + 1;

  x = r*sin(theta)*cos(phi);
  y = r*sin(theta)*sin(phi);
  z = r*cos(theta);
  fprintf(g.fid, "Point(%d) = {%.16f, %.16f, %.16f, %e}; \n", p, x, y, z, l);
endfunction

# write a line 
function p=write_line(type_in, points)
  global g
  p = g.ip; 
  g.ip = g.ip + 1;

  fprintf(g.fid, "%s(%d) = { ", type_in, p);
  for i = 1:length(points)
	fprintf(g.fid, "%d", points(i));
	if(i < length(points)) 
	  fprintf(g.fid, ", ");
	endif
  endfor
  fprintf(g.fid, "}; \n");	

endfunction

# write a surface 
function p=write_surface(type_in, lines)
  global g
  p = g.ip; 
  g.ip = g.ip + 1;

  fprintf(g.fid, "Line Loop(%d) = { ", p);
  for i = 1:length(lines)
	fprintf(g.fid, "%d", lines(i));
	if(i < length(lines)) 
	  fprintf(g.fid, ", ");
	endif
  endfor
  fprintf(g.fid, "}; \n");	

  fprintf(g.fid, "%s Surface(%d) = {%d}; \n", type_in, p, p);
endfunction

# write a volume
function p=write_volume(surfs)
  global g
  p = g.ip; 
  g.ip = g.ip + 1;

  fprintf(g.fid, "Surface Loop(%d) = { ", p);
  for i = 1:length(surfs)
	fprintf(g.fid, "%d", surfs(i));
	if(i < length(surfs)) 
	  fprintf(g.fid, ", ");
	endif
  endfor
  fprintf(g.fid, "}; \n");	

  fprintf(g.fid, "Volume(%d) = {%d}; \n", p, p);
endfunction

# Write a spherical surface
function s=write_sphere(r,l)
  global g

  phi = g.PHI;
  tet = g.THETA;

  # ------  POINTS -----

  # lower circle
  s.pa= write_point_sphere(r, -phi/2, pi-tet, l);
  s.pb= write_point_sphere(r, phi/2, pi-tet, l);
  s.pc= write_point_sphere(r, 3*phi/2, pi-tet, l);
  s.pd= write_point_sphere(r, -3*phi/2, pi-tet, l);
  s.pp= write_point(0, 0, -r*cos(tet), l);


  # upper circle
  s.pe= write_point_sphere(r,-phi/2, tet, l);
  s.pf= write_point_sphere(r, phi/2, tet, l);
  s.pg= write_point_sphere(r, 3*phi/2, tet, l);
  s.ph= write_point_sphere(r,-3*phi/2, tet, l);
  s.pq= write_point(0, 0, r*cos(tet), l);

# ------  LINES -----

  # lower lines
  s.la = write_line('Circle', [s.pb 1 s.pa]);
  s.lb = write_line('Circle', [s.pa 1 s.pd]);
  s.lc = write_line('Circle', [s.pd 1 s.pc]);
  s.ld = write_line('Circle', [s.pc 1 s.pb]);

  # upper lines
  s.le = write_line('Circle', [s.pe 1 s.pf]);
  s.lf = write_line('Circle', [s.pf 1 s.pg]);
  s.lg = write_line('Circle', [s.pg 1 s.ph]);
  s.lh = write_line('Circle', [s.ph 1 s.pe]);

  # vertical lines
  s.li = write_line('Circle', [s.pa 1 s.pe]);
  s.lj = write_line('Circle', [s.pb 1 s.pf]);
  s.lk = write_line('Circle', [s.pc 1 s.pg]);
  s.ll = write_line('Circle', [s.pd 1 s.ph]);

# ------  Surfaces -----

  s.left   = write_surface('Ruled', [s.li -s.lh -s.ll -s.lb]);
  s.right  = write_surface('Ruled', [s.lk -s.lf -s.lj -s.ld]);
  s.bottom = write_surface('Ruled', [s.la s.lb s.lc s.ld]);
  s.top    = write_surface('Ruled', [s.le s.lf s.lg s.lh]);
  s.front  = write_surface('Ruled', [s.lj -s.le -s.li -s.la]);
  s.back   = write_surface('Ruled', [s.ll -s.lg -s.lk -s.lc]);

endfunction

# Write a volume between two spheres
function v=write_spherical_volume(s1, s2)

# ------- Interim lines, numbered the same 
#         as sphere points

  v.la = write_line('Line', [s1.pa s2.pa]);
  v.lb = write_line('Line', [s1.pb s2.pb]);
  v.lc = write_line('Line', [s1.pc s2.pc]);
  v.ld = write_line('Line', [s1.pd s2.pd]);
  v.le = write_line('Line', [s1.pe s2.pe]);
  v.lf = write_line('Line', [s1.pf s2.pf]);
  v.lg = write_line('Line', [s1.pg s2.pg]);
  v.lh = write_line('Line', [s1.ph s2.ph]);

# ------- Interim surfaces, numbered the same 
#         as sphere lines

  # lower surfaces
  v.sa = write_surface('Plane', [s1.la v.la -s2.la -v.lb]);
  v.sb = write_surface('Plane', [s1.lb v.ld -s2.lb -v.la]);
  v.sc = write_surface('Plane', [s1.lc v.lc -s2.lc -v.ld]);
  v.sd = write_surface('Plane', [s1.ld v.lb -s2.ld -v.lc]);

  # upper surfaces
  v.se = write_surface('Plane', [s1.le v.lf -s2.le -v.le]);
  v.sf = write_surface('Plane', [s1.lf v.lg -s2.lf -v.lf]);
  v.sg = write_surface('Plane', [s1.lg v.lh -s2.lg -v.lg]);
  v.sh = write_surface('Plane', [s1.lh v.le -s2.lh -v.lh]);
	 
  # mid surfaces
  v.si = write_surface('Plane', [s1.li v.le -s2.li -v.la]);
  v.sj = write_surface('Plane', [s1.lj v.lf -s2.lj -v.lb]);
  v.sk = write_surface('Plane', [s1.lk v.lg -s2.lk -v.lc]);
  v.sl = write_surface('Plane', [s1.ll v.lh -s2.ll -v.ld]);

# ------- Volumes, numbered the same as sphere
#         surfaces
  v.left  = write_volume([-s1.left s2.left v.si -v.sl -v.sb -v.sh]);
  v.right = write_volume([-s1.right s2.right v.sk -v.sj -v.sf -v.sd]);

  v.front  = write_volume([-s1.front s2.front v.sj -v.si -v.se -v.sa]);
  v.back  = write_volume([-s1.back s2.back v.sl -v.sk -v.sg -v.sc]);

  v.bottom = write_volume([-s1.bottom s2.bottom v.sa v.sb v.sc v.sd]);
  v.top = write_volume([-s1.top s2.top v.se v.sf v.sg v.sh]);

endfunction

# Make an entitiy transfinite
function trans(type_in, mems, prog)
  global g

  # write the members
  if (prog{1} == 'qt') fprintf(g.fid, "TransfQuadTri { ");
  else fprintf(g.fid, "Transfinite %s { ", type_in);
  endif

  for i = 1:length(mems)
	fprintf(g.fid, "%d", mems(i));
	if(i < length(mems)) 
	  fprintf(g.fid, ", ");
	endif
  endfor
  fprintf(g.fid, '} ');
  
  # write the progression for lines
  if(isnumeric(prog{1}))

	fprintf(g.fid, " = %d ", prog{1}+1);	
	if(length(prog) ==  3)
	  fprintf(g.fid, "Using %s %f ", prog{2}, prog{3});
	endif

  # recombine for surfaces volumes
  elseif(prog{1} == 'rc')

		 fprintf(g.fid, ";\n");		 
		 fprintf(g.fid, "Recombine %s { ", type_in);
		 for i = 1:length(mems)
		   fprintf(g.fid, "%d", mems(i));
		   if(i < length(mems)) 
			 fprintf(g.fid, ", ");
		   endif
		 endfor

		 fprintf(g.fid, "} ");
  elseif(prog{1} == 't')
    fprintf(g.fid, " %s ", prog{2});

  # do nothing for quadtri
  else
	assert(prog{1} == 'qt' || prog{1} == 'n');

  endif


  fprintf(g.fid, ";\n");
endfunction

# ---------------------------------------------------------------------------
#                               Main Code
# ---------------------------------------------------------------------------


# ----------------------- initialize
init();

# ----------------------- Create the geometric entities
# mesh sizing parameters

switch(g.level)
  case 0
    prog_surf = {3, 'Bump', 1};
    prog_r = {2, 'Progression', 1};
    prog_rr = {2, 'Progression', 1};    
  case 1
    prog_surf = {8, 'Bump', 1.2};
    prog_r = { 8, 'Progression', 1.22};
    prog_rr = {12, 'Progression', 1.3};
  case 2
    prog_surf = {14, 'Bump', 1.3};
    prog_r = {12, 'Progression', 1.2};
    prog_rr = {15, 'Progression', 1.21};
  case 3
    prog_surf = {25, 'Bump', 1.3};
    prog_r = {18, 'Progression', 1.12};
    prog_rr = {25, 'Progression', 1.12};
  case 4
    prog_surf = {40, 'Bump', 1.3};
    prog_r = {25, 'Progression', 1.08};
    prog_rr = {28, 'Progression', 1.12};
  case 5
    prog_surf = {70, 'Bump', 1.3};
    prog_r = {35, 'Progression', 1.07};
    prog_rr = {36, 'Progression', 1.10};
  
endswitch

# center
write_point(0,0,0,1);


l = .5;
s1 = write_sphere(1,    l);     
s2 = write_sphere(6,    l);     
s3 = write_sphere(100,    l);      


v = write_spherical_volume(s1,s2);
w = write_spherical_volume(s2,s3);

# --------------------- Transfinite stuff

# Lines
#surface
trans('Line', [s1.la, s1.lb, s1.lc, s1.ld], prog_surf);
trans('Line', [s1.le, s1.lf, s1.lg, s1.lh], prog_surf);
trans('Line', [s1.li, s1.lj, s1.lk, s1.ll], prog_surf);

trans('Line', [s2.la, s2.lb, s2.lc, s2.ld], prog_surf);
trans('Line', [s2.le, s2.lf, s2.lg, s2.lh], prog_surf);
trans('Line', [s2.li, s2.lj, s2.lk, s2.ll], prog_surf);

trans('Line', [s3.la, s3.lb, s3.lc, s3.ld], prog_surf);
trans('Line', [s3.le, s3.lf, s3.lg, s3.lh], prog_surf);
trans('Line', [s3.li, s3.lj, s3.lk, s3.ll], prog_surf);


# radial
trans('Line', [v.la, v.lb, v.lc, v.ld], prog_r);
trans('Line', [v.le, v.lf, v.lg, v.lh], prog_r);

trans('Line', [w.la, w.lb, w.lc, w.ld], prog_rr);
trans('Line', [w.le, w.lf, w.lg, w.lh], prog_rr);

rcmodes = {'n'};
rcmoder = {'rc'};
rcmodev = {'n'};

# Surfaces
# surface of spheres
trans('Surface', [s1.left,s1.right,s1.front,s1.top,s1.bottom,s1.back], rcmodes);
trans('Surface', [s2.left,s2.right,s2.front,s2.top,s2.bottom,s2.back], rcmodes);
trans('Surface', [s3.left,s3.right,s3.front,s3.top,s3.bottom,s3.back], rcmodes);

## radial in vol 1
trans('Surface', [v.sa, v.sb, v.sc, v.sd], rcmoder);
trans('Surface', [v.se, v.sf, v.sg, v.sh], rcmoder);
trans('Surface', [v.si, v.sj, v.sk, v.sl], rcmoder);

## radial in vol 2
[w.sa, w.sb, w.sc, w.sd]
[w.se, w.sf, w.sg, w.sh]
[w.si, w.sj, w.sk, w.sl]
trans('Surface', [w.sa, w.sb, w.sc, w.sd], rcmoder);
trans('Surface', [w.se, w.sf, w.sg, w.sh], rcmoder);
trans('Surface', [w.si, w.sj, w.sk, w.sl], rcmoder);

# volumes
trans('Volume', [v.left, v.right, v.front, v.top, v.bottom, v.back], rcmodev);
trans('Volume', [w.left, w.right, w.front, w.top, w.bottom, w.back], rcmodev);

fprintf(g.fid, "Coherence Mesh; \n");

# --------------------- Physical Stuff

fprintf(g.fid, "Physical Volume(%d) = { ", 1);
fprintf(g.fid, "%d, %d, %d, %d, %d, %d,", v.left, v.right, v.top, v.bottom, v.front, v.back);
fprintf(g.fid, "%d, %d, %d, %d, %d, %d}; \n", w.left, w.right, w.top, w.bottom, w.front, w.back);

fprintf(g.fid, "Physical Surface(%d) = { ", 5); # characteristic
fprintf(g.fid, "%d, %d, %d, %d, %d, %d}; \n", s3.left, s3.right, s3.top, s3.bottom, s3.front, s3.back);


fprintf(g.fid, "Physical Surface(%d) = { ", 1 ); # wall
fprintf(g.fid, "%d, %d, %d, %d, %d, %d}; \n", s1.left, s1.right, s1.top, s1.bottom, s1.front, s1.back);

# ------------------------ Finalize
finish();
