class Kassa(object):
    count=1000

    def __init__(self,count):
        self.count=count

    def top_up(self,x):
        self.count+=x

    def count_1000(self):
        print("В кассе",self.count//1000," тыс.руб.")

    def take_away(self,x):
        if x>self.count:
            print("В кассе недостаточно средств")
        else:
            self.count-=x
            print("Пройдите в закрома")

command=""

print("Введите начальный остаток в кассе")
My_Kassa=Kassa(int(input()))

while command!="stop":
    print("Введите команду (add,take, ost, stop для выхода)")
    command=input()

    if command=="ost":
        My_Kassa.count_1000()

    elif command=="add":
        print("Какую сумму Вы хотите положить в кассу?")
        My_Kassa.top_up(int(input()))
        
    elif command=="take":
        print("Какую сумму Вы хотите взять из кассы?")
        My_Kassa.take_away(int(input()))
        
 
