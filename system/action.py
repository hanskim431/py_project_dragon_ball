import charator.charator as char
import random
from exception.exception import *


def parseAction(action:str):
  ki_list = ['ki', '기', '으', '아', '기모으기', '기 모으기']
  guard_list = ['guard','막기', '가드', '방어']
  teleport_list = ['teleport','텔레포트', '텔포', '텔', '순간이동']
  attack_list = ['attack','공격', '파', '어택']
  energyWage_list = ['energyWave','에너지파', '에너지 파', '에네르기파', '에네르기 파']
  idle_list = ['idle']

  action_list = [ki_list, guard_list, teleport_list,
                 attack_list, energyWage_list, idle_list]

  for list in action_list:
    for item in list:
      if action in (item):
        return list[0]
      
  return False
  

def select_action(charator:char.Charator, action:str):
  parsed_action = parseAction(action)
  print('🚀 ~ parsed_action:', parsed_action)

  match parsed_action:
    case 'ki':
      charator.ki()
    case 'guard':
      charator.guard()
    case 'teleport':
      charator.teleport()
    case 'attack':
      charator.attack()
    case 'energyWave':
      charator.energyWave()
    case 'idle':
      charator.idle()
    case False:
      raise WrongActionError
    
def random_cpu_action(user_charator:char.Charator, cpu_charator:char.Charator):
  probability = random.randint(1,100)
  
  if user_charator.cost == 0 and cpu_charator.cost == 0:
    return 'ki'
  
  elif cpu_charator.cost >= 1 and cpu_charator.cost < 3 :
    if(probability >= 70):
      return 'attack'
    elif(probability >= 20 and probability < 70):
      return 'guard'
    else:
      return 'ki'
    
  elif cpu_charator.cost >= 3 :
    if(probability >= 50):
      return 'energyWave'
    elif(probability >= 30 and probability < 50):
      return 'attack'
    elif(probability >= 10 and probability < 30):
      return 'guard'
    else:
      return 'ki'
    
  else:
    if(probability >= 60):
      return 'guard'
    else:
      return 'ki'
