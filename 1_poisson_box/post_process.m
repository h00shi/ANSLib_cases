## ----------------------------------------------------------------------------
##
## find_norms.m 
## 
## Find the norms and plot them for a sequence of meshes.
## ---------------------------------------------------------------------------
#mode = 'sep';
mod = 'tog';

switch mod

case 'sep'

  raw_name = ['a4'];
  file_name = [raw_name, '.dat'];

  c = { 'b', 'r', 'g' };
  LW = 'linewidth';
  C = 'color';

  sol = load('-ascii', file_name);
  l1 = sol(:,1);
  l2 = sol(:,2);
  l3 = sol(:,3);
  N = [cbrt(232); cbrt(999); cbrt(4670); cbrt(30475)];

  p1 = polyfit (log10(N(end-1:end)),  log10(l1(end-1:end)),1);
  p2 = polyfit (log10(N(end-1:end)),  log10(l2(end-1:end)),1);
  p3 = polyfit (log10(N(end-1:end)), log10(l3(end-1:end)),1);

  clf, hold on;
  hold on;
  loglog(N, l1, ["-s;L1, slope =" sprintf("%.2f", -p1(1)) ";"], LW, 2, C, c{1});
  loglog(N, l2, ["-s;L2, slope =" sprintf("%.2f", -p2(1)) ";"], LW, 2, C, c{2});
  loglog(N, l3, ["-s;Linf, slope =" sprintf("%.2f", -p3(1)) ";"], LW, 2, C, c{3});


  ## style
  copied_legend = findobj(gcf(),"type","axes","Tag","legend");
  set(copied_legend, "FontSize", 20 , "location" , "southwest", "linewidth",2);

  hx=xlabel("N");
  hy=ylabel("Error");
  set(hx, "fontsize", 15, "linewidth", 2);
  set(hy, "fontsize", 15, "linewidth", 2);
  set(gca,  "fontsize", 15);

  print(['plots/', raw_name, '.png'] ,"-dpng","-FArial", "-color");

case 'tog'

  raw_name = ['a4'];
  file_name = [raw_name, '.dat'];

  c = { 'b', 'r', 'g' };
  LW = 'linewidth';
  C = 'color';

  # --------------------
  sol = load('-ascii', 'norms-a2.dat');
  a2 = sol(:,2);

  sol = load('-ascii', 'norms-a3.dat'); 
  a3 = sol(:,2);

  sol = load('-ascii', 'norms-a4.dat'); 
  a4 = sol(:,2);

  #sol = load('-ascii', 'a2_nt.dat');
  #a2n = sol(:,2);

  #sol = load('-ascii', 'a4_nt.dat'); 
  #a4n = sol(:,2);


  N = [sqrt(566); sqrt(3180); sqrt(13157)];

  p2 = polyfit (log10(N(end-2:end)),  log10(a2(end-2:end)),1);
  p3 = polyfit (log10(N(end-2:end)),  log10(a3(end-2:end)),1);
  p4 = polyfit (log10(N(end-2:end)),  log10(a4(end-2:end)),1);
  #p2n = polyfit (log10(N(end-2:end)),  log10(a2n(end-2:end)),1);
  #p4n = polyfit (log10(N(end-2:end)),  log10(a4n(end-2:end)),1);

  # --------------------
  clf, hold on;
  hold on;
  loglog(N, a2, ["-o;a2, slope =" sprintf("%.2f", -p2(1)) ";"], LW, 2, C, c{1});
  #loglog(N, a2n, ["--o;a2n, slope =" sprintf("%.2f", -p4(1)) ";"], LW, 2, C, c{1});  
  loglog(N, a3, ["-^;a3, slope =" sprintf("%.2f", -p3(1)) ";"], LW, 2, C, c{2});
  loglog(N, a4, ["-s;a4, slope =" sprintf("%.2f", -p4(1)) ";"], LW, 2, C, c{3});
  #loglog(N, a4n, ["--s;a4n, slope =" sprintf("%.2f", -p4(1)) ";"], LW, 2, C, c{3});


  ## style
  copied_legend = findobj(gcf(),"type","axes","Tag","legend");
  set(copied_legend, "FontSize", 20 , "location" , "southwest", "linewidth",2);

  hx=xlabel("N");
  hy=ylabel("||Error||_2");
  set(hx, "fontsize", 15, "linewidth", 2);
  set(hy, "fontsize", 15, "linewidth", 2);
  set(gca,  "fontsize", 15);

  print(['plots/', 'all', '.png'] ,"-dpng","-FArial", "-color");

endswitch
