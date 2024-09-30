# 깃허브 연동용 VScode

player_num = int(input())
size_num = list(map(int, input().split()))
Tshirt_Pen_num = list(map(int, input().split()))

if player_num == sum(size_num):
    t_num = Tshirt_Pen_num[0]
    pen_num = Tshirt_Pen_num[1]

    T_buy = 0
    for i in range(len(size_num)):
        if size_num[i] % t_num != 0:
            T_buy = T_buy + (size_num[i] // t_num + 1)
        else:
            T_buy = T_buy + (size_num[i] // t_num)

    pen_bundle = player_num // pen_num
    pen_each = player_num % pen_num

    print(T_buy)
    print(pen_bundle, pen_each)
else:
    print("수를 정확히 기재해주세요.")





