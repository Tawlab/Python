max_attempts = 3
while True:
    password = input("Enter new password(Max8): ")
    for attempt in range(max_attempts):
        user_Input = input("Enter password(Max8): ")
    # เช็คเงื่อนไขการออก
        if password.lower() == "exit":
            print("ออกจากโปรแกรม")
            break
    # เช็ครหัสผ่านถูกหรือไม่
        if password == user_Input:
            print("Password correct")
            break
        else:
            print("Password incorrect")
    else:
        print("Close program")
    break
