from system.system_function import *
from system.action import *
from system.judge import *
from exception.exception import *

user_charator, cpu_charator = initial()

start_yelling()

while True:
  info(user_charator, cpu_charator)

  select_action(cpu_charator, random_cpu_action(user_charator, cpu_charator))
  

  while True :
    try:
      select_action(user_charator, input('\n당신이 취할 행동은? '))
      break
    except WrongActionError as err:
      print('잘못된 입력값 입니다.')
      continue

  yellSpell(user_charator, cpu_charator)

  judgment = makeJudgment(user_charator, cpu_charator)

  if(judgment != None):
    print(judgment)
    print(user_charator.name,':  ',user_charator.status_list)
    print(cpu_charator.name,':  ',cpu_charator.status_list)
    break