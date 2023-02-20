import argparse
import csv
import math
import yaml


def load_enemy_data(enemy_file):
  with open(enemy_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    l = []
    for row in reader:
      l.append([int(r) for r in row])
    return l

def load_own_data_yaml(own_file):
  with open(own_file, 'r') as yml:
    l = yaml.safe_load(yml)
  return l

def calc_own_rps(own_data, c_list):
  own_rps = [0, 0, 0]
  count = 0
  for c in c_list:
    own_rps[c] = own_rps[c] + own_data[count]
    count += 1
  return own_rps

def check_win_or_lose(enemy_rps, own_data):
  # explore if there is a winning combination for the enemy
  #   - https://hiraocafe.com/note/kumiwake.html
  #     (7) How to divide 6 different balls into 3 people.
  #         However, there is no one who does not receive
  for c1 in (0, 1, 2):
    for c2 in (0, 1, 2):
      for c3 in (0, 1, 2):
        for c4 in (0, 1, 2):
          for c5 in (0, 1, 2):
            for c6 in (0, 1, 2):
              own_rps = calc_own_rps(own_data, [c1, c2, c3, c4, c5, c6])
              if own_rps[0] > enemy_rps[0] and own_rps[1] > enemy_rps[1] and own_rps[2] > enemy_rps[2]:
                return own_rps

def main():
  parser = argparse.ArgumentParser(
            prog='battle_simulator.py',
            usage='python3 battle_simulator.py',
            description='battle simulator of TsubasaRivals',
            epilog='end',
            add_help=True,
            )
  parser.add_argument('-s', '--special',
                      help='all command parameters 150%% up',
                      action='store_true')
  parser.add_argument('-e', '--enemy',
                      help='enemy data csv',
                      default='./data/3_Dias.csv')
  args = parser.parse_args()

  if args.special:
    ratio = 1.5
  else:
    ratio = 1.0

  own_file = './data/own.yaml'
  own_data_yaml = load_own_data_yaml(own_file)
  own_data = []
  for own in own_data_yaml:
    for i in range(own["commands"]):
      if own.get("main") and i==0:
        own_data.append(int(own["val"] * ratio * 2))
      else:
        own_data.append(int(own["val"] * ratio))
  print("------------------------")
  print("|     YOUR COMMANDS     |")
  print("------------------------")
  print(own_data)
  print("")

  enemy_data = load_enemy_data(args.enemy)

  pattern = 1
  win_flag = True
  for enemy_rps in enemy_data:
    print("===== Pattern", pattern , "=====")
    own_rps = check_win_or_lose(enemy_rps, own_data)
    if own_rps:
      print("You win!")
    else:
      print("You lose...")
      win_flag = False
    print("- You  :", own_rps)
    print("- Enemy:", enemy_rps)
    print("")
    pattern +=1
  
  print("------------------------")
  print("|     TOTAL RESULT     |")
  print("------------------------")
  if win_flag:
    print("YOU WIN ALL PATTERN!!!")
  else:
    print("You lose...Continue?")


if __name__ == "__main__":
  main()
