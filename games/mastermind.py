import random

secret_number = ""



while len(secret_number) < 4:
    a = random.randint(0, 9)
    change_a_to_text = str(a)
    if change_a_to_text not in secret_number:
        secret_number += change_a_to_text

MAX_TURNS = 10
turn_count = 0

history = []

while True:
    print(f"Bạn có {MAX_TURNS} lượt để đoán số bí mật gồm 4 chữ số!")
    answer = input("Hãy nhập số (4 chữ số, không trùng): ")
    
    count_bulls = 0  # đúng số đúng vị trí
    count_cows = 0   # đúng số sai vị trí
    
    if len(answer) != 4 or not answer.isdigit():
        print("Mời nhập số hợp lệ")    
        continue 
    

    turn_count += 1
    print("... Tiến hành so sánh ...")
    for i in range(4):
        if answer[i] == secret_number[i]:
            count_bulls += 1 
        elif answer[i] in secret_number:
            count_cows += 1 

    print(f"=== Kết quả ===")
    print(f"🐂 Bulls (đúng số đúng vị trí): {count_bulls}")
    print(f"🐄 Cows  (đúng số sai vị trí): {count_cows}")
    history.append((turn_count, answer, count_bulls, count_cows))
    if count_bulls == 2:
        print(f"🔥Bạn đang gần đúng rồi, thử đổi vị trí một vài số")
    elif count_bulls == 3:
        print(f"💡Chỉ còn 1 số nữa là đúng!")
    elif count_bulls == 4:
        print(f"🎉 Chúc mừng! Bạn đã đoán đúng: {secret_number}")
        print(f"Số bạn chọn: {answer}")
        print(f"Secret number: {secret_number}")
        for i in history:
            print(f"Lượt {i[0]}: {i[1]} → {i[2]} Bulls, {i[3]} Cows")
        break
    if turn_count >= MAX_TURNS:
        print(f"GAME OVER! HẾT LƯỢT")
        print(f"Số bạn chọn: {answer}")
        print(f"Secret number: {secret_number}")
        for i in history:
            print(f"Lượt {i[0]}: {i[1]} → {i[2]} Bulls, {i[3]} Cows")
        break
    