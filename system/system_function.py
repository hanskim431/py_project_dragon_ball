import charator.charator as char
import time
import os

def initial():
  os.system('cls')
  cpu_name = '손오공' + '(CPU)'
  cpu_charator = char.Charator(cpu_name)

  user_name = input('당신의 이름을 입력하세요: ') + '(나)'
  user_charator = char.Charator(user_name)

  return (user_charator, cpu_charator)

def start_yelling():
  sleep_time = 0.3
  print('드', end='\r')
  time.sleep(sleep_time)
  print('드 래', end='\r')
  time.sleep(sleep_time)
  print('드 래 곤', end='\r')
  time.sleep(sleep_time)
  print('드 래 곤 볼')
  time.sleep(sleep_time)

def info(user_charator:char.Charator, cpu_charator:char.Charator):
    print()
    print(f'{user_charator.name} [HP: {user_charator.hp}] [기: {user_charator.cost}]')
    print(f'{cpu_charator.name} [HP: {cpu_charator.hp}] [기: {cpu_charator.cost}]')
  
def yellSpell(user_charator:char.Charator, cpu_charator:char.Charator):
  print(f'{user_charator.name}: {user_charator.status_list[-1]}!! vs {cpu_charator.name}: {cpu_charator.status_list[-1]}!! ')