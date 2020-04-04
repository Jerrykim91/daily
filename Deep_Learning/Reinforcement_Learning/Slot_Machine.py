import numpy as np
import pandas as pd
import random
import math

import matplotlib.pyplot as plt

class Machine():
    # 속성 - 확률
    def __init__(self,p):
        # 확률이라는 속성을 부여 
        self.percentage = p
        # 외부에서 입력된 p로 인해 값이 초기화
        
    # 보상
    def reward(self):
        # 머신 선택시 보상 지급 
        # 세팅된 확률보다 랜덤 값이 적으면 1 아니면 0 
        if self.percentage > random.random():
            return 1.0
        else:
            return 0.0

# 랜덤 값의 범위 확인
# print([ random.random() for n in range(10)])

# Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]
# print(Machines) # 확인용

class Engine():
    # 초기화 함수 -> 알고리즘에 필요한 값을 초기화
    def initialize(self):
        # 값을 초기화
        pass

    def select_machin(self):
        # 기계를 선택
        pass

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self):
        # 파라미터를 핸들링
        pass
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        pass
    

"""
# Engine Class
- 표준 인터페이스
- 알고리즘 2개를 사용 예정 
    - # ε-greedy 알고리즘
        - 확률 ε(0~1)으로 랜덤하게 행동을 선택한다.
        - arm을 선택하는 행위
        - 확률 1-ε는 현재 가치가 가장 높은 팔을 선택한다.
        - 이런 확률값 중 가장 좋은 성능을 내는 값 0.1인 경우가 많다.
    
    - #  UCB1 알고리즘
        - 절차
            - 1. 선택한 팔의 시행 횟수 +1
            - 2. 성공시(보상을 받으면), 선택한 팔의 성공 횟수 +1
            - 3. 시행 횟수가 0인 팔이 존재하는 경우, 가치를 갱신하지 않는다 => 0으로 나눌수가 없어서
            - 4. 시행 횟수가 모두 0이상이면, 팔의 가치에 대해서 탐색과 이용에 대한 균형을 잡는다는 대전에 하에, 모든 팔의 가치를 갱신한다.

            - 모든 팔을 한번 이상 사용할때까지는 가치 갱신을 하지 않는다 => 탐색
            - 모든 팔을 최소 1회 이상 사용해 봤다면, 전체 arm에대 가치 갱신을 시도한다.

"""

# EpsilonGreedy 알고리즘 이용 
class E_Greedy_Engine(Engine):
    def __init__(self, epsilon = 0.1 ):
        # 속성부여 
        self.epsilon = epsilon  # 탐험하는 확률 

    # 초기화 함수 -> 알고리즘에 필요한 값을 초기화
    def initialize(self):
        # 값을 초기화 -> 
        # 각 경험을 보유해야함 -> 시도, 가치(보상)을 배열에 저장 
        
        pass

    def select_machin(self):
        # 기계를 선택
        pass

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self):
        # 파라미터를 핸들링
        pass
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        pass
    

# 시뮬레이터     
# 머신을 준비 -> 각 확률을 부여 
Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]  # 30%, 50%, 90%
print(Machines) 

