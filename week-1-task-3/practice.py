import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

conn = psycopg2.connect(
        host="localhost",
        database="task_3",
        user='admin',
        password='root')

while True:
    option = int(input('1.Inner Join, 2.Left Join, 3.Right Join, 4.Full Join'))

    if option ==1:
        try:
            cursor = conn.cursor()
            postgreSQL_select_Query = ("SELECT * FROM Orders INNER JOIN Customers ON Orders.Customer_ID = Customers.Customer_ID;")
            cursor.execute(postgreSQL_select_Query)
            publisher_records = cursor.fetchall()

            print(publisher_records)

            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL"), err

    elif option == 2:
        try:
            cursor = conn.cursor()
            postgreSQL_select_Query = ("SELECT Customers.first_name, Orders.item,orders.amount FROM Customers \
                                        LEFT JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID\
                                        ORDER BY Customers.first_name;")
            cursor.execute(postgreSQL_select_Query)
            publisher_records = cursor.fetchall()
            print(publisher_records)

            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    elif option == 3:
        try:
            cursor = conn.cursor()
            postgreSQL_select_Query = ("SELECT Orders.Order_ID, customers.Last_Name, customers.First_Name FROM Orders\
                                        RIGHT JOIN customers ON Orders.customer_id = customers.customer_id\
                                        ORDER BY Orders.Order_ID;")
            cursor.execute(postgreSQL_select_Query)
            publisher_records = cursor.fetchall()
            print(publisher_records)


            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    elif option == 4:
        try:
            cursor = conn.cursor()
            postgreSQL_select_Query = ("SELECT Customers.first_name, Orders.Order_ID FROM Customers\
                                        FULL OUTER JOIN Orders ON Customers.Customer_ID=Orders.Customer_ID\
                                        ORDER BY Customers.first_name; ")
            cursor.execute(postgreSQL_select_Query)
            publisher_records = cursor.fetchall()
            print(publisher_records)

            conn.commit()
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
