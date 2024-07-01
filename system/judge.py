import charator.charator as char

ch = char.Charator 

def makeJudgment(user_charator:ch, cpu_charator:ch):
  user1 = user_charator
  user2 = cpu_charator

  for _ in range(2):
    if (user1.attack_point == user2.attack_point):
      return None
    
    elif (user1.attack_point > user2.attack_point):
      if(user1.attack_point == ch.ENERGY_WAVE):
        if(user2.avoid_status == True): 
          return None
        else :
          return f'\n{user1.name} 승리\n'
      
      if(user1.attack_point == ch.ATTACK):
        if(user2.avoid_status == True or user2.guard_status == True):
          return None
        else :
          return f'\n{user1.name} 승리\n'

    (user1,user2) = (user2,user1)    
    

  
