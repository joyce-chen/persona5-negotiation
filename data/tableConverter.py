import sys
import re

def parse_results(results):
    output = {'gl': '-', 'ir': '-', 'ti': '-', 'up': '-'}
    for r in results:
        parts = r.split(' - ')
        if parts[1] == 'GLOOMY':
            output['gl'] = parts[0]
        elif parts[1] == 'IRRITABLE':
            output['ir'] = parts[0]
        elif parts[1] == 'TIMID':
            output['ti'] = parts[0]
        else:
            output['up'] = parts[0]
    return output

def generate_result(result):
    if result == "GOOD":
        output = "GOOD</div><div class='symbol'>🎶</div>"
    elif result == "OK":
        output = "OK</div><div class='symbol'>💦</div>"
    elif result == "BAD":
        output = "BAD</div><div class='symbol'>💢</div>"
    else:
        output = "-</div><div class='symbol'></div>"
    return "\n\t\t<td class='result'><div class='text'>" + output + '</td>'
        
def create_table(q, flag, top_a, mid_a, bot_a, top_r, mid_r, bot_r):
    question = '\n\t<tr>\n\t\t<th colspan="5">' + q + "</th>\n\t</tr>"
    header = "\n\t<tr>\n\t\t<td></td>" + "\n\t\t<td class='subheader'>gloomy</td>" + "\n\t\t<td class='subheader'>irritable</td>" + "\n\t\t<td class='subheader'>timid</td>" +  "\n\t\t<td class='subheader'>upbeat</td>\n\t</tr>"

    top = "\n\t<tr>\n\t\t<td>" + top_a + "</td>" + generate_result(top_r['gl']) + generate_result(top_r['ir']) + generate_result(top_r['ti']) + generate_result(top_r['up']) + "\n\t</tr>"
    mid = "\n\t<tr>\n\t\t<td>" + mid_a + "</td>" + generate_result(mid_r['gl']) + generate_result(mid_r['ir']) + generate_result(mid_r['ti']) + generate_result(mid_r['up']) + "\n\t</tr>"
    bot = "\n\t<tr>\n\t\t<td>" + bot_a + "</td>" + generate_result(bot_r['gl']) + generate_result(bot_r['ir']) + generate_result(bot_r['ti']) + generate_result(bot_r['up']) + "\n\t</tr>"

    if flag == "":
        return "\n<table>" + question + header + top + mid + bot + "\n</table>"
    else:
        return '\n<table class="' + flag + '">' + question + header + top + mid + bot + "\n</table>"

def convert_file():
    outputfile = open('data/output.html', 'w', encoding="utf8")
    inputfile = open('data/input.html', encoding="utf8")

    indexfile = open('index.md', encoding="utf8")
    indexHTML = indexfile.read().split('<div id="questions">')

    inputHTML = inputfile.read().replace('\n', '').replace('\t', '')
    inputTables = inputHTML.split("</table>")
    del inputTables[-1]

    outputfile.write(indexHTML[0])
    outputfile.write('<div id="questions">')

    for table in inputTables:
        rows = table.split("</tr>")

        question = rows[0]
        top = rows[1]
        mid = rows[2]
        bot = rows[3]

        question_text = re.findall(r'<th colspan="2">(.+?)</th>', question)[0]
        top_text = re.findall(r'<td>(.+?)</td>', top)
        mid_text = re.findall(r'<td>(.+?)</td>', mid)
        bot_text = re.findall(r'<td>(.+?)</td>', bot)

        top_ans = top_text[0]
        mid_ans = mid_text[0]
        bot_ans = bot_text[0]

        if len(top_text) > 1:
            top_res = top_text[1].split("<br>")
        else:
            top_res = []
        
        if len(mid_text) > 1:
            mid_res = mid_text[1].split("<br>")
        else:
            mid_res = []

        if len(bot_text) > 1:
            bot_res = bot_text[1].split("<br>")
        else:
            bot_res = []
        
        if "noAnswer" in question:
            flag = "noAnswer"
        elif "notCertain" in question:
            flag = "notCertain"
        else:
            flag = ""
        
        outputfile.write(create_table(question_text, flag, top_ans, mid_ans, bot_ans, parse_results(top_res), parse_results(mid_res), parse_results(bot_res)))
    
    outputfile.write("\n</div>")
    
    outputfile.close()

convert_file()
