


import pymysql.cursors
connection = pymysql.connect(
host='147.46.15.66',
user='qmopla',
password='bde1234',
db='qmopla',
charset='utf8',
cursorclass=pymysql.cursors.DictCursor)


def func_1():
    
    try:
        with connection.cursor()as cursor:
            sql='select* from hall'
            cursor.execute(sql)
            result=cursor.fetchall()
            #print(result)
            print('-'*80)
            print('id' + '\t' + 'name' + ('%18s'%' ') + 'location' +('%5s'%' ') +'capacity')
            print('-'*80)
            for row in result:
                print(str(row['h_id']) + '\t' + row['h_name'] + '\t' + row['location'] + '\t'+ '\t' + str(row['capacity']))  
            print('-'*80)    
            
    finally:
        pass

def func_2():
    try:
        with connection.cursor()as cursor:
            sql='select* from performance'
            cursor.execute(sql)
            result=cursor.fetchall()
            #print(result)
            print('-'*80)
            print('id' + '\t' + 'name' + ('%20s'%' ')  +'type' +  ('%5s'%' ') +  'price' +('%5s'%' ')  +'booked')
            print('-'*80)
            for row in result:
                print(str(row['p_id']) + ('%4s'%' ')  + row['p_name'] + ('%10s'%' ')  + row['p_type'] + '\t'+  row['price']+('%7s'%' ') +  str(row['booked']))  
            print('-'*80)    
            
    finally:
        pass    


def func_3():
    try:
        with connection.cursor()as cursor:
            sql='select* from audience'
            cursor.execute(sql)
            result=cursor.fetchall()
            #print(result)
            print('-'*80)
            print('id' + '\t' + 'name' + '\t' +'gender' +  '\t'+  'age')
            print('-'*80)
            for row in result:
                print(str(row['a_id']) + '\t' + row['a_name'] + '\t'  + row['gender'] + '\t'+  row['age'])  
            print('-'*80)    
            
    finally:
        pass


def func_4():
    hall_name=input('please input Hall name : ')
    location_name=input('please input location name : ')
    capacity_input=input('please input capacity : ')
    try:
        with connection.cursor()as cursor:
            sql="insert into hall(h_name,location,capacity) values (%s,%s,%s) "
            
            cursor.execute(sql, (hall_name, location_name,capacity_input))
            connection.commit()
            result=cursor.fetchall()
            print('A hall is successfully inserted')

           
    finally:
        pass


def func_5():
    hall_id=eval(input('please input hall_id want to delete : '))
    
    try:
        with connection.cursor()as cursor:
            #sql="delete from hall where (h_id=%s) "
            sql2='select h_id from hall'
            #cursor.execute(sql, (hall_id))
            cursor.execute(sql2)
            #connection.commit()
            result=cursor.fetchall()

            
            ids = [row["h_id"] for row in result]
            if hall_id in ids:
                sql="delete from hall where (h_id=%s) "
                cursor.execute(sql, (hall_id))
                connection.commit()
                #print(result)
            else:
                print('no result')
    finally: pass
  

def func_6():
    performance_name=input('please input performance name : ')
    performance_type=input('please input performance type : ')
    performance_price=input('please input performance price : ')
    seat_input=eval(input('please input capacity : '))
    
    try:
        with connection.cursor()as cursor:
            sql="insert into performance(p_name,p_type,price,seat) values (%s,%s,%s,%s) "
            
            cursor.execute(sql, (performance_name, performance_type,performance_price,seat_input))
            connection.commit()
            result=cursor.fetchall()
            print('A performance is successfully inserted')

           
    finally:
        pass


def func_7():
    performance_id=eval(input('please input performance_id want to delete : '))
    
    try:
        with connection.cursor()as cursor:
            #sql="delete from hall where (h_id=%s) "
            sql2='select p_id from performance'
            #cursor.execute(sql, (hall_id))
            cursor.execute(sql2)
            #connection.commit()
            result=cursor.fetchall()

            
            ids = [row["p_id"] for row in result]
            if performance_id in ids:
                sql="delete from performance where (p_id=%s) "
                cursor.execute(sql, (performance_id))
                connection.commit()
                #print(result)
            else:
                print('no result')
    finally: pass


def func_8():
    Audience_name=input('please input Audience name : ')
    Audience_gender=input('please input Audience gender : ')
    Audience_age=input('please input Audience age : ')
    try:
        with connection.cursor()as cursor:
            sql="insert into audience(a_name,gender,age) values (%s,%s,%s) "
            
            cursor.execute(sql, (Audience_name, Audience_gender,Audience_age))
            connection.commit()
            result=cursor.fetchall()
        print('An audience is successfully inserted')

         
    finally:
        pass    


def func_9():
    audience_id=eval(input('please input audience_id want to delete : '))
    
    try:
        with connection.cursor()as cursor:
            #sql="delete from hall where (h_id=%s) "
            sql2='select a_id from audience'
            #cursor.execute(sql, (hall_id))
            cursor.execute(sql2)
            #connection.commit()
            result=cursor.fetchall()

            
            ids = [row["a_id"] for row in result]
            if audience_id in ids:
                sql="delete from audience where (a_id=%s) "
                cursor.execute(sql, (audience_id))
                connection.commit()
                #print(result)
            else:
                print('no result')
    finally: pass


def func_10():
    Hall_id=eval(input('please input Hall_id want to locate : '))
    performance_id=eval(input('please input performance_id want to locate : '))

    try:
        with connection.cursor()as cursor:
            sql2='select p_id from locate'
            cursor.execute(sql2)
            result=cursor.fetchall()

            ids = [row["p_id"] for row in result]
            #print(ids)
            if (performance_id not in ids):
                sql="insert into locate(h_id,p_id) values (%s,%s) "
            
                cursor.execute(sql, (Hall_id,performance_id))
                connection.commit()
                result=cursor.fetchall()
                print('Successfully assign a performance')
            else : print('There is performance find other hall')
    finally: pass


def func_11():
    performance_id=int(input('please input performance_id : '))
    Audience_id=input('please input Audience_id : ')
    seat_number=input('please input seat_number : ')
    seat_number_list=seat_number.split(',')
    Hall_id = input('please input Hall_id : ')
    p_id_list=[]
    seat_list=[]
    seat_also_reservation=[] #예약되어있는 좌석 번호
    performance_price=0
    locate_p_id=[]
    seat_capacity=0 #공연의 좌석 수
    try: 
        with connection.cursor()as cursor: #배정되지 않은 경우 에러 출력
            sql="select l.p_id from locate l"
            cursor.execute(sql)
            result=cursor.fetchall()
            for row in result:
                locate_p_id.append(row['p_id'])
            if performance_id not in locate_p_id :
                print('that performance is not existed')
                raise SyntaxError

    finally : pass


    try: # 이미 예약된 좌석일 경우 에러 출력
        with connection.cursor()as cursor:
            sql="select r.seat from reservation r where r.p_id=(%s)  "
            cursor.execute(sql,(performance_id))
            result=cursor.fetchall()
            #print(result)
            for row in result:
                #print(row)
                #p_id_list.append(row['p_id'])
                seat_also_reservation.append(row['seat'])
            #print(p_id_list)
            #print(seat_also_reservation)

            for number in seat_number_list:
                if int(number) in seat_also_reservation:
                    print('That seat already booked')
                    raise SyntaxError     
    finally: pass



    try: #좌석번호가 최대좌석번호수를 넘어설때 에러출력 
        with connection.cursor()as cursor:
            sql="select p.seat,p.price from performance p where p.p_id=(%s)"
            cursor.execute(sql,(performance_id))
            result=cursor.fetchall()
            for row in result :
                #print(row['seat'])
                seat_capacity=row['seat']
                performance_price = row['price']
            #print(seat_capacity)
            #print(performance_price)

                for number in seat_number_list:
                    if int(number) > seat_capacity:
                        print('That seat is not avaliable')
                        raise SyntaxError                   
    finally: pass


    try:
        with connection.cursor()as cursor:
            for i in range(len(seat_number_list)):
                sql="insert into reservation(p_id,a_id,h_id,seat) values (%s,%s,%s,%s) "
        
                cursor.execute(sql, (performance_id,Audience_id,Hall_id,seat_number_list[i]))
                connection.commit()
                result=cursor.fetchall()
            print('Total ticket price is :',len(seat_number_list)*performance_price)
    

    finally: pass


def func_12():
    Hall_id = eval(input('please input Hall_id : '))
    try:
        with connection.cursor()as cursor:
            sql="select p.p_id,p.p_name,p.p_type,p.price from performance p,locate l,hall h where p.p_id=l.p_id and l.h_id=h.h_id and l.h_id=(%s) "
            
            cursor.execute(sql,(Hall_id))
            connection.commit()
            result=cursor.fetchall()
            #print(result)
            print('p_id' + '\t' + 'p_name' +('%10s'%' ') + 'p_type' + '\t' + 'price')
            print('-'*80)
            for row in result:
                print(str(row['p_id'])+ '\t' + row['p_name'] + '\t' + row['p_type'] +'\t' + row['price'])
           
    finally:
        pass



def func_13():
    Performance_id = eval(input('please input Performance_id : '))
    try:
        with connection.cursor()as cursor:
            sql="select distinct a.a_id,a.a_name,a.gender,a.age,r.p_id from audience a, reservation r where a.a_id=r.a_id "
            
            cursor.execute(sql)
            connection.commit()
            result=cursor.fetchall()
            
            li_p_id=[]
            for row in result:
                li_p_id.append(row['p_id'])
            #print(li_p_id)

            if Performance_id not in li_p_id:
                print('There is no performance')
                raise SyntaxError

            sql2="select distinct a.a_id,a.a_name,a.gender,a.age,r.p_id from audience a, reservation r where a.a_id=r.a_id and r.p_id=(%s) "
            
            cursor.execute(sql2,(Performance_id))
            connection.commit()
            result2=cursor.fetchall()
            #print(result2)       
            print('a_id' + '\t' + 'a_name' + '\t' + 'gender' + '\t' + 'age')
            print('-'*80)
            for row in result2:
                print(str(row['a_id']) + '\t' + row['a_name'] + '\t' + row['gender'] + '\t' + row['age'])
            #for i in li_p_id:
             #   if Performance_id == i:
              #      print('a_id' + '\t' + 'a_name' + '\t' + 'gender' + '\t' + 'age')
               #     print('-'*80)
                #    print(str(row['a_id']) + '\t' + row['a_name'] + '\t' + row['gender'] + '\t' + row['age'])
                #else : print('Not in Performan')
           
    finally:
        pass


def func_14():
    Performance_id = eval(input('please input Performance_id : '))
    seat_performance=0 
    reservation_seat_list=[]
    reservation_present={}
    audience_id_list=[]
    locate_identy=[]
    try:
        with connection.cursor()as cursor:
            sql="select distinct p.seat,r.seat,r.a_id from performance p,reservation r where p.p_id=r.p_id and p.p_id=(%s) "
            
            cursor.execute(sql,(Performance_id))
            connection.commit()
            result=cursor.fetchall()
            #print(result)
            for row in result:
                seat_performance=row['seat']
                reservation_seat_list.append(row['r.seat'])
                audience_id_list.append(row['a_id'])
            #print(seat_performance)
            #print(reservation_seat_list)
            #print(audience_id_list)

    finally:
        pass


    try:
        with connection.cursor()as cursor:
            sql="select p.p_id from performance p "
            
            cursor.execute(sql)
            connection.commit()
            result=cursor.fetchall()
            
            li_p_id=[]
            for row in result:
                li_p_id.append(row['p_id'])
            #print(li_p_id)

            if Performance_id not in li_p_id:
                print('There is no performance')
                raise SyntaxError
            else:pass
    finally:
        pass


    try:
        with connection.cursor()as cursor:
            sql="select l.p_id from locate l "
            
            cursor.execute(sql)
            connection.commit()
            result=cursor.fetchall()
            for row in result:
                locate_identy.append(row['p_id'])
            #print(li_p_id)

            if Performance_id not in locate_identy:
                print('There is no performance')
                raise SyntaxError
            else:pass
    finally:
        pass


    for i in range(1,seat_performance+1):
        reservation_present[i]=''
    #print(reservation_present)

    for i in range(len(reservation_seat_list)):
        reservation_present[reservation_seat_list[i]]=audience_id_list[i]
    #print(reservation_present)


    keys=list(reservation_present.keys())
    values=list(reservation_present.values())
    #print(keys)
    #print(values)
    print('seat_number'+'\t'+'audience_id')
    print('-'*80)
    for i in range(len(keys)):
        print(keys[i],'\t','\t',values[i])


def func_15():
    print('Bye!')
    try: pass
    
    finally:
        #print('Bye!')
        connection.close()


def main():


    print("=================================================================")
    print("1. print all buildings")
    print("2. print all performances")
    print("3. print all audiences")
    print("4. insert a new building")
    print("5. remove a building")
    print("6. insert a new performance")
    print("7. remove a performance")
    print("8. insert a new audience")
    print("9. remove an audience")
    print("10. assign a performance to a building")
    print("11. book a performance")
    print("12. print all performances assigned at a building")
    print("13. print all audiences booked for a performance")
    print("14. print ticket booking status of a performance")
    print("15. exit")
    print("=================================================================")

    
    a=eval(input('please input action :'))
    while a<15:
       if a==1: func_1()
       elif a==2 : func_2()
       elif a==3 : func_3()
       elif a==4 : func_4()
       elif a==5 : func_5()
       elif a==6 : func_6()
       elif a==7 : func_7()
       elif a==8 : func_8()
       elif a==9 : func_9()
       elif a==10 : func_10()
       elif a==11 : func_11()
       elif a==12 : func_12()
       elif a==13 : func_13()
       elif a==14 : func_14()
       elif a==15 : func_15()

       a=eval(input('please input action :'))


       
       
