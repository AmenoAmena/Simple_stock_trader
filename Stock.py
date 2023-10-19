import random
import time
from sys import exit

print("You are going to have 2500 money in your account")
print("Every turn represents one week")

things = {
    "apple_up":"Apple lots are rising because new iphone is selling real good",
    "apple_down":"Apple lots are decreasing because new Ipad is selling badly",
    
    "samsung_up":"Samsung lots are rising because new s24 is a banger",
    "samsung_down":"Samsung lots are decreasing because new galaxy book is selling badly",
    
    "xiaomi_up":"Xiaomi lots are rising because new xiaomi curved monitor selling really good",
    "xiaomi_down":"Xiaomi lots are decreasing because new book s12.4 is selling badly",
    
    "huawei_up":"Huawei lots are rising because new p 60 pro is selling good",
    "huawei_down":"Huawei lots are decreasing because new huawei matebook x pro selling poorly",
    
    "nokia_up":"Nokia lot are rising because nokia 3310 refurbished sold well",
    "nokia_down":"Nokia lots are decreasing because nokia new budPhone sell badly",
    
    "apple_big_crash":"Apple lots crashed a lot because of apple privacy policy and refurbished scams",

    "samsung_big_crash":"Samsung lots crashed a lot because samsung new s24 exploded",

    "xiaomi_big_crash":"Xiaomi lots crashed a lot because of working conditions it provides",

    "huawei_big_crash":"Huawei lots are crashed a lot because huawei g box shuts down",

    "nokia_big_crash":"Nokia lots crashed a lot because nokia cant sell phones because they new phones are not good",

    "nokia_big_rise":"Nokia lots rise a lot because nokia made 3310 smartphone and it sold pretty pretty well",

    "huawei_big_rise":"Huawei lots raise really well because google open one of his services to harmony os",

    "nothing":"Nothing happened this week"
}



apple = 180
samsung = 150
xiaomi = 90
huawei = 70
nokia = 100
money = 2500


apple_count = 0
samsung_count = 0
xiaomi_count = 0
huawei_count = 0
nokia_count = 0


print("------------------")
print(f"Apple is {apple}")
print(f"Samsung is {samsung}")
print(f"Xiaomi is {xiaomi}")
print(f"Huawei is {huawei}")
print(f"Nokia is {nokia}")
print("------------------")

turn = int(input("How many turn do you want to simulate stocks: "))


durum = True


while durum:
    
    
    try:
        for _ in range(turn):
            
            account_money = apple*apple_count+samsung*samsung_count+xiaomi*xiaomi_count+huawei*huawei_count+nokia*nokia_count+money

                        
            if account_money  < 500:
                print("Congrats now you are a broke guy")
                exit()
            
            
            
            cikis = input("if you want to quit prees q: ")
            if cikis == "q":
                turn = 0
                durum = False
                exit()


            random_up = random.randint(0,10)
            random_down = random.randint(0,10)
            

            which_one = input("Which stock do you want(Apple,Samsung,Xiaomi,Huawei,Nokia. if you dont want to buy anything just press enter): ")        
            which_one_number = int(input("How many stock you want to purchase : "))
            

            if which_one == "Apple" or which_one == "apple":
                apple_count += 1 * which_one_number
                money -= apple * which_one_number
          
        
        
            elif which_one == "Samsung" or which_one == "samsung":
                samsung_count += 1 * which_one_number
                money -= samsung *which_one_number
            
            

            elif which_one == "Xiaomi" or which_one == "xiaomi":
                xiaomi_count += 1 * which_one_number
                money -= xiaomi * which_one_number
            

            elif which_one == "Huawei" or which_one == "huawei":
                huawei_count += 1 * which_one_number
                money -= huawei * which_one_number
            

            elif which_one == "Nokia" or which_one == "nokia":
                nokia_count += 1 * which_one_number
                money -=nokia * which_one_number
            

            else:
                print("You dont buy anything")
            
            sell = input("Do you want to sell any lots(Yes/No): ")
            
            
            if sell == "Yes" or sell == "yes":
                
                
                sell_lot = input("Which lot do you want to sell(Apple,Samsung,Xiaomi,Huawei,Nokia): ")            
                sell_number = int(input("How many stocks do you want to sell: "))

                
                if sell_lot == "Apple" or sell_lot == "apple" and apple_count >= 1:
                    apple_count -= 1*sell_number
                    print(f"you know have {apple_count} apple lots")
                    money += apple*sell_number

                elif sell_lot == "Samsung" or sell_lot == "samsung" and samsung_count >= 1:
                    samsung_count -= 1*sell_number
                    print(f"you know have {samsung_count} samsung lots")
                    money += samsung * sell_number

                elif sell_lot == "Xiaomi" or sell_lot == "xiaomi" and samsung_count >= 1:
                    xiaomi_count -= 1*sell_number
                    print(f"you know have {xiaomi_count} xiaomi lots")
                    money += xiaomi * sell_number

                elif sell_lot == "Huawei" or sell_lot ==  "huawei" and huawei_count >= 1:
                    huawei_count -= 1*sell_number
                    print(f"you know have {huawei_count} huawei lots")
                    money += huawei*sell_number

                elif sell_lot == "Nokia" or sell_lot == "nokia" and nokia_count >= 1:
                    nokia_count -= 1*sell_number
                    print(f"you know have {nokia_count} nokia lots")
                    money += nokia*sell_number


            elif sell == "No" or sell ==  "no":
                print("You dont sell anything in this turn")            


            else:             
                print("You dont want to sell anything")
            
            
            random_thing_key = random.choice(list(things))
            random_key_happen = things[random_thing_key]
            
            
            if random_thing_key == "apple_up":
                apple += 10
                print(things["apple_up"])
            
            
            elif random_thing_key == "apple_down":
                apple -=10
                print(things["apple_down"])
            
            
            elif random_thing_key == "samsung_up":
                samsung += 10
                print(things["samsung_up"])
            
            
            elif random_thing_key == "samsung_down":
                samsung += 10
                print(things["samsung_down"])
            
            
            elif random_thing_key == "samsung_down":
                samsung -= 10
                print(things["samsung_down"])    
            
            
            elif random_thing_key == "xiaomi_up":
                xiaomi += 10
                print(things["xiaomi_up"])
            
            
            elif random_thing_key == "xiaomi_down":
                xiaomi -= 10
                print(things["xiaomi_down"])
            
            
            elif random_thing_key == "huawei_up":
                huawei += 10
                print(things["huawei_up"])
            
            
            elif random_thing_key == "huawei_down":
                huawei -= 10
                print(things["huawei_down"])
            
            
            elif random_thing_key == "nokia_up":
                nokia += 10
                print(things["nokia_up"])
            
            
            elif random_thing_key == "nokia_down":
                nokia -= 10
                print(things["nokia_down"])
            
            
            elif random_thing_key == "apple_big_crash":
                apple -= 20
                print(things["apple_big_crash"])
            
            
            elif random_thing_key == "samsung_big_crash":
                samsung -= 20
                print(things["samsung_big_crash"])
            
            
            elif random_thing_key == "xiaomi_big_crash":
                xiaomi -= 20
                print(things["xiaomi_big_crash"])
            
            
            elif random_thing_key == "huawei_big_crash":
                huawei -= 20
                print(things["huawei_big_crash"])
            
            
            elif random_thing_key == "nokia_big_crash":
                nokia -= 20
                print(things["nokia_big_crash"])
            
            
            elif random_thing_key == "nokia_big_rise":
                nokia += 30
                print(things["nokia_big_rise"])
            
            
            elif random_thing_key == "huawei_big_rise":
                huawei += 30
                print(things["huawei_big_rise"])
            
            
            elif random_thing_key == "nothing":
                print(things["nothing"])
            
            
            else:
                print("Error")
            
            apple -= random_down
            apple += random_up
            apple += random_up + 2
            apple -= random_down - 1



            samsung -= random_down
            samsung += random_up
            samsung += random_up + 3
            samsung -= 3


            xiaomi -= random_down
            xiaomi += random_up
            xiaomi += random_up + 5
            xiaomi -= random_down - 3


            huawei -= random_down
            huawei += random_up
            huawei += random_up + 4
            huawei -= random_down - 1


            nokia -= random_down
            nokia += random_up
            nokia -= random_down - 4
            nokia += random_up + 3
            

            
            
            account_money = apple*apple_count+samsung*samsung_count+xiaomi*xiaomi_count+huawei*huawei_count+nokia*nokia_count+money


            time.sleep(3)


            print("------------------")
            print(f"Apple is {apple}")
            print(f"Samsung is {samsung}")
            print(f"Xiaomi is {xiaomi}")
            print(f"Huawei is {huawei}")
            print(f"Nokia is {nokia}")
            print("------------------")
            
            
            
            time.sleep(3)
            
            
            
            print("------------------")
            print(f"You have {apple_count} lots of apple")
            print(f"You have {samsung_count} lots of Samsung")
            print(f"You have {xiaomi_count} lots of Xiaomi")
            print(f"You have {huawei_count} lots of Huawei")
            print(f"You have {nokia_count} lots of Nokia")    
            print(f"Your total money in account is {account_money} ")
            print("------------------")
            
            
            durum = False 
    
    except:
        print("use valid numbers and stocks")        
        

