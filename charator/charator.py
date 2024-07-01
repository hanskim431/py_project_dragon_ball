import sys

class Charator() :
  IDLE = 0
  ATTACK = 1
  ENERGY_WAVE = 2

  def __init__(self, name):
    self.name = name
    self.hp = 1 # 체력
    self.cost = 0 # 기
    self.attack_point = self.IDLE # 무슨 공격 [ 공격(파), 에네르기파(에너지파), ... ]  
    self.guard_status = False # 가드 한다 / 가드 안한다 
    self.avoid_status = False  # 회피 한다 / 회피 안한다
    self.status_list = []

  def statusChange(self, attack_point=IDLE, guard_status=False, avoid_status=False ):
    self.attack_point = attack_point # 무슨 공격 [ 공격(파), 에네르기파(에너지파), ... ]  
    self.guard_status = guard_status # 가드 한다 / 가드 안한다 
    self.avoid_status = avoid_status  # 회피 한다 / 회피 안한다
    status=f'{sys._getframe(1).f_code.co_name}'
    self.status_list.append(status)
  
  def idle(self):
    self.statusChange()

  def ki(self):
    self.cost += 1
    self.statusChange()

  def guard(self):
    self.statusChange(guard_status=True)

  def teleport(self):
    self.cost -= 1
    self.statusChange(avoid_status=True)

  def attack(self):
    if self.cost >= 1:
      self.cost -= 1
      self.statusChange(Charator.ATTACK)
    else :
      self.idle()

  def energyWave(self):
    if self.cost >= 3:
      self.cost -= 3
      self.statusChange(Charator.ENERGY_WAVE)
    else :
      self.idle()

  def damaged(self, damage):
    if self.hp > 0:
      self.hp -= damage
