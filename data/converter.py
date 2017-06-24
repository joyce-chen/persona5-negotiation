import sys
import csv


reader = csv.reader(open('p5.csv', 'rU'), delimiter=',', dialect=csv.excel_tab)

htmlfile = open('p5.html', 'w')

for i, row in enumerate(reader):
    if i%4 == 0:
        htmlfile.write('<table>\n\t<tr>\n\t\t<th colspan="2">' + row[0] + '</th>\n\t</tr>\n')
    else:
        htmlfile.write('\t<tr>\n')
        for column in row:
            htmlfile.write('\t\t<td>' + column + '</td>\n')
        htmlfile.write('\t</tr>\n')
        if i%4 == 3:
            htmlfile.write('</table>\n')

htmlfile.close()
