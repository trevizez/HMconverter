import re
from datetime import datetime

input_file = '5412341.txt'


def blinds(input_file):
    d = []
    with open(input_file, 'r') as input:
        for line in input:
             if line.startswith("PLO5"):
                sb = line.split(':')[1].split(' ')[0]
                bb = line.split(':', 2)[2].split(' ')[0]
                d.append(sb)
                d.append(bb)
    return d

def players(input_file):
    players_info = []
    with open(input_file, 'r') as input:
        for line in input:
            if line.startswith('Seat') and line.endswith(' chips),\n'):
                player_seat = re.findall(r'Seat \d+', line)[0]
                player_nick = line.split(None, 3)[3].split()[0]
                player_chips = line.split('(')[1].split()[0]
                players_info.append(f"{player_seat}: {player_nick} (${player_chips} in chips)\n")
    return sorted(players_info)

def if_ante(input_file):
    with open(input_file, 'r') as input:
        for line in input:
            if line.__contains__('ante'):
                ante = True
                break
            else:
                ante = False
    return ante



def ante(input_file):
    with open(input_file, 'r') as input:
        for line in input:
            if line.__contains__('ante'):
                ante = line.split('player')[1].split(')')[0]
    return ante

def nick_on_seat(input_file):
    nicks = {}
    for line in players(input_file):
        nicks[(line.split(':')[0])] = line.split(': ')[1].split(' (')[0]
    return nicks

def nick_on_seat_list(input_file):
    nicks = []
    for line in players(input_file):
        nicks.append(line.split(': ')[1].split(' (')[0])
    return nicks

def convert_file(input_file, output_file):
    l = 0
    count_for_dict = 0
    with open(input_file, 'r') as input:
        with open(output_file, 'w') as output:
            for line in input:
                if line.startswith('Round #'):
                    hand_number = re.findall(r'\d+', line)[0]
                    date = re.findall(r'\d{4}-\d{2}-\d{2}', line)[0]
                    time = re.findall(r'\d{2}:\d{2}:\d{2}', line)[0]
                    date_obj = datetime.strptime(date, "%Y-%m-%d")
                    output_date = date_obj.strftime("%Y/%m/%d")
                    gametype = re.findall(r'PLO5|NLH', line)[0]
                    if gametype == 'PLO5':
                        gametype = "Omaha Pot Limit"
                    else:
                        gametype = "Hold'em No Limit"
                    sb = float(blinds(input_file)[0])
                    bb = float(blinds(input_file)[1])
                    output.write(f"Hand #{hand_number}: {gametype} (${sb}/${bb} USD) - {output_date} {time} ET\n")

                elif line.startswith('Table:') and "dealer" in line:
                    table_name = line.split(':')[1].split(',')[0].strip()
                    table_config = line.split(',')[1].split('dealer')[0].strip()
                    output.write(f"Table '{table_name}' {table_config} button\n")

                elif line.startswith('Seat') and line.endswith(' chips),\n'):
                    output.write(players(input_file)[l])
                    l+=1

                elif line.__contains__('posts' and 'blind'):
                    if line.__contains__('small'):
                        nick_sb = nick_on_seat(input_file)[line.split(' posts')[0]]
                        output.write(f'{nick_sb}: posts small blind ${sb}\n')
                    else:
                        nick_bb = nick_on_seat(input_file)[line.split(' posts')[0]]
                        output.write(f'{nick_bb}: posts big blind ${bb}\n')

                elif if_ante(input_file) and output:
                    output.write(nick_on_seat_list(input_file)[count_for_dict]+'\n' )




                # while line != "*** HOLE CARDS ***":
                #     players = []
                #     if



                    #elif 'posts' in line:
                    #     position = re.findall(r'Seat \d+', line)[0]
                    #     amount = re.findall(r'\d+\.\d+', line)[0]
                    #     output.write(f"{position}: PlayerX ($ {amount} in chips)\n")
                    #elif line.startswith('Dealt to'):
                    #     hole_cards = re.findall(r'\[[^\]]+\]', line)
                    #     output.write(f"{line.replace(',', ', ') if ',' in line else line}")
                    #elif line.startswith('Seat') and 'Shows' not in line:
                    #     action = re.findall(r'Seat \d+ [A-Za-z0-9]+', line)[0]
                    #     output.write(f"{action}: {line.replace(action, '').strip()} to {line.split(' ')[-1].strip()}\n")
                    #elif line.startswith('Seat') and 'Shows' in line:
                    #     output.write(f"{line.replace(',', ', ') if ',' in line else line}")
                    #else:
                    #     output.write(line)
                    

convert_file('5412341.txt', 'output.txt')
# a = blinds('5412341.txt')
# print(a)
print(nick_on_seat_list(input_file))