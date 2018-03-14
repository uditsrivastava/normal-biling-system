
def bill(grand_total,grand_sqft,rate,raw_input):
    sr_no = input("enter serial number")
    desc = raw_input("enter description")
    height = input("enter height")
    width = input("enter width")
    pcs = input("enter pcs")
    sq_ft = height * width * pcs
    print ("square feet:",sq_ft)
    current_amount = sq_ft * rate
    print ("current amount:",current_amount)
    grand_total = grand_total + current_amount
    grand_sqft = grand_sqft + sq_ft
    answer =raw_input("do you want to enter the second record? y/n")
    if answer.lower() == 'y':
             bill(grand_total,grand_sqft,rate)
    elif answer == 'n':
             print ("grand square feet:",grand_sqft)
             print ("grand total:",grand_total)
    else:
             print ("invalid input")
             
print ("udit creation and software")
grand_total = 0
grand_sqft = 0
rate = 0.79
choice = raw_input("enter into biling system? y/n")
if choice == 'y':
     password = input("enter correct password")
     if password == 2477:
              bill(grand_total,grand_sqft,rate)
     else:
              print ("error ...wrong password!")
else:
    exit




    
 

    
