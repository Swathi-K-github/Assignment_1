#Registration and Login system using Python, file handling

# Function to validate username

def emailid_register(userName):
  index1 = userName.find("@")
  index2 = userName.find(".")
  alphaCheck = userName[0].isalpha() 
  if index1<index2 and index2-index1>1 and alphaCheck == 1 :
     temp = 1
  else :
       print("Username is not in correct format, Try again")
       choices()


# Function to validate the password
def password_check(passwd):
      
    SpecialSym =['!', '"', '#', '$', '%', '&', '~', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) >16:
        print('length should be not be greater than 16')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

#Storing data in a file
def store(userName, passwd) :
  f = open("User_Data.txt", "r")
  ss = f.read()
  f.close()
  f = open("User_Data.txt", "a")
  ss =  "\n" + userName + " " + passwd
  f.write(ss)

#function to login
def login():
    print("Welcome to Login Page")
    userName = str(input("Login Name: "))
    #emailid_register(userName)
    passwd = str(input("Password: "))
    #if (password_check(passwd)) :
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if userName in info:
        index = info.index(userName) + 1
        usr_password = info[index]
        if usr_password == passwd:
            print("Welcome, " + userName)
        else:
          print("Invalid Credentials /n Have you forgotten the password? Give YES to retrieve it, else give NO to change password.")
          forgot_password = input()
          if  forgot_password == "YES" :
            userName = input("Enter the userID: ")
            flag = True
            f = open('User_Data.txt','r')
            info = f.read()
            info = info.split()
            for line in info:
                if userName in info:
                  index = info.index(userName) + 1
                  usr_password = info[index]
                  print("The Password is", usr_password)
                  flag = False
                break
            
            if flag:
                print("User ID not found /n Please SignUp")
                choices()
                
          elif forgot_password == "NO" : 
                passwd2 = input("Type your new password")
                PassWord3 = password_check(passwd2)
                lines=[]
                if PassWord3 :
                  with open("User_Data.txt", "r") as f:
                      lines = list(f.readlines())
                      f.close()

                  with open("User_Data.txt", "w") as f:
                      for line in (lines):
                        if(line.find(userName) == -1) :
                          f.write(line) 
                  f.close() 
                  f = open("User_Data.txt", "a")
                  f.writelines("\n" +userName + " " +passwd2 +"\n")
                  f.close()
                  print("Password Changed Successfully")

          else:
            "Invalid input"  
                
    else:
      print("Username does not exists. Please register.")
      choices()
      

def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
      print("Registration Form")
      userName = input("Enter the username:")
      emailid_register(userName)
      passwd = input("Enter the Password:")
      if (password_check(passwd)):
        store(userName, passwd)
        print("Registration successful")

    elif choice == 2:
      login()

  
choices()
