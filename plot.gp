reset
set terminal pdfcairo font "Times"
set output "graph.pdf"


#set yrange [40000:70000]
p 'export.csv' u 1:6 w lines,\
  ''  u 1:10 w lines,\
  ''  u 1:11 w lines

#unset xrange
p 'export.csv'   u 1:15 w lines,\
   ''  u 1:14 w lines,\