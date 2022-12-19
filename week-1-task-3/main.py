import psycopg2

# Connecting the database using psycopg2
conn = psycopg2.connect(
            host="localhost",
            database="task_3",
            user='admin',
            password='root',
            port='5432')

# While loop until user wants to exit from this loop it will continued
while True:
    Topic = int(input('1.DDL, 2.DML,3.DCL,4.joins, 5.Direct Query from the Database, 6.Exit \n Select anyone Topic:' ))

    #If user select 1 then it will redirect to the DDL Queries
    if Topic == 1:

        while True:
            option = int(input('1.CREATE, 2.Drop, 3.Alter ,4.Truncate'))

            #If user select 1 then it will redirect to the CREATE method
            if option ==1:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                # Droping EMPLOYEE table if already exists.
                cursor.execute("DROP TABLE IF EXISTS publisher")

                # Creating table as per requirement
                sql = '''CREATE TABLE PUBLISHER(
                                publisher_id SERIAL PRIMARY KEY,
                                publisher_name VARCHAR(255) NOT NULL,
                                publisher_estd INT,
                                publsiher_location VARCHAR(255),
                                publsiher_type VARCHAR(255)
                )'''
                cursor.execute(sql)
                print("Table created successfully")
                conn.commit()
                cursor.close()

            #If user select 2 then it will redirect to the Drop method
            elif option == 2:
                try:
                    cursor = connection.cursor()
                    postgreSQL_select_Query = ("Drop table PUBLISHER;")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)

            #If user select 3 then it will redirect to the Alter method
            elif option == 3:
                try:
                    cursor = conn.cursor()
                    postgreSQL_select_Query = ("ALTER TABLE PUBLISHER rename COLUMN publisher_estd to publisher_year;")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)

            #If user select 4 then it will redirect to the Delete the only data then this will be used method
            elif option == 4:
                try:
                    cursor = connection.cursor()
                    postgreSQL_select_Query = (" TRUNCATE TABLE publisher; ")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)


    #If user select 1 then it will redirect to the DDL Queries
    elif Topic == 2:
                option = int(input('1.Insert, 2.Update, 3.Delete \n Enter one option:' ))

                #If user select 1 then it will redirect to the CREATE method
                if option ==1:
                    print("Data will be inserted")

                #If user select 2 then it will redirect to the update method
                elif option == 2:
                    print("D`ata will be Updated")

                #If user select 3 then it will redirect to the Delete method
                elif option == 3:
                    print("Data will be deleted")

    #If user select 3 then it will redirect to the DCL Queries
    elif Topic == 3:
                option = int(input('1.Grant, 2.Revoke' ))
                if option ==1:
                    print("grant the data")

                elif option == 2:
                    print("revoke the data")

    #If user select 4 then it will redirect to the Joins methods
    elif Topic == 4:

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

    #If user select 5 then it will redirect to whatever user wants to print, they can easily provide their own Queries
    elif Topic == 5:

        try:
            # creating a cursor object using he cursor() method
            cursor = conn.cursor()
            postgreSQL_select_Query = input("Enter your query:")
            cursor.execute(postgreSQL_select_Query)

            publisher_records = cursor.fetchall()
            print(publisher_records)
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    #If user select 6 then whole process is closed.
    elif option == 6:
        # cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")
        print("you are exited form the database")
        break;
