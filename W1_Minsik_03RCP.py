# 1) 인풋구문을 만들어 대답을 유도합니다.
# 2) 컴퓨터가 대답할 답변의 리스트를 만듭니다.
# 3) IF구문으로 각 승패에 대한 경우의 구문들을 생성합니다.
# 4) 승, 패를 카운팅할 수 있도록 각 결과의 값을 수치로 치환합니다.
# 5) 반복 구문을 활용하여 반복이 될 수 있도록 합니다.
# 5) 승이 3번일 경우, 패가 3번일 경우를 특정의 수치값이 되도록 만들고, 그 결과가 게임의 끝으로 설정합니다.

import random
RCP = input("가위,바위,보 중에 하나를 선택해 주세요. : " )
fightback = ['가위','바위','보']
fightback_r = random.choice(fightback)
result = 0
while result == 3:

if RCP == "가위" and fightback_r =='보':
    result = result + 1
    print ("승리하셨습니다.")
elif RCP == "바위" and fightback_r =='가위':
    result = result + 1
    print ("승리하셨습니다.")
elif RCP == "보" and fightback_r =='바위':
    result = result + 1
    print ("승리하셨습니다.")
elif RCP == "가위" and fightback_r =='바위':
    result = result - 1
    print ("패배하셨습니다.")
elif RCP == "바위" and fightback_r =='보':
    result = result - 1
    print ("패배하셨습니다.")
elif RCP == "보" and fightback_r =='가위':
    result = result - 1
    print ("패배하셨습니다.")
else :
    result = result + 0
    print ('비기셨네요')

# 가위바위보를 게임화하는데는 성공했습니다만, 반복구문으로 만드는 방법을 모르겠습니다.
