# class res:
#     res_1 = list["용수산", "가회정", "좋구먼", "가온"]
#     res_2 = list["황금성", "딘타이펑", "리틀타이완", "하하"]
#     res_3 = list["우마쿠라", "이나니와요스케", "토끼정", "하스"]
#
import random
res_1 = ["용수산","가회정"]
res_2 = ["황금성", "하하"]
res_3 = ["우마쿠라","이나니와요스케"]
select = input("한식, 중식, 일식 중 한 가지를 고르세요. : ",)
if select == "한식":
    print("찾으시는 식당은 ", random.choice(res_1))
elif select == "중식":
    print("찾으시는 식당은 ", random.choice(res_2))
elif select == "일식":
    print("찾으시는 식당은 ", random.choice(res_3))
