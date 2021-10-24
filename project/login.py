def login():  # membuka login dengan awal username dan password
    crct_username = "mudhya"  # username yang benar
    crct_password = "mudhya123"  # password yang benar
    while True:  # nilai boolean true untuk username dan password
        username = str(input("username : "))  # input dengan menggunakan string
        password = str(input("password : "))  # input dengan menggunakan string
        # input username dan password masuk kedalam nilai boolean true
        if crct_username == username and crct_password == password:
            # ouput yang keluar setelah username dan password benar
            print("Hey,Welcome to python " + username)
        break  # jika benar maka diakhiri dengan break kaya hubungan
    else:  # seandainya salah ouput teks dibawah yang akan muncul
        print("wrong username or password")


login()
