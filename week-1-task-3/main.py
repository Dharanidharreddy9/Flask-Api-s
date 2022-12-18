import psycopg2

conn = psycopg2.connect(
            host="localhost",
            database="task_3",
            user='admin',
            password='root',
            port='5432')

while True:
    Topic = int(input('1.DDL, 2.DML,3.DCL,4.joins, 5.Direct Query from the Database, 6.Exit \n Select anyone Topic:' ))

# DDL Queries
    if Topic == 1:

        while True:
            option = int(input('1.CREATE, 2.Drop, 3.Alter ,4.Truncate'))

            if option ==1:
                # Creating a cursor object using the
                # cursor() method
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

            elif option == 2:
                try:
                    cursor = connection.cursor()
                    postgreSQL_select_Query = ("Drop table PUBLISHER;")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)

            elif option == 3:
                try:
                    cursor = conn.cursor()
                    postgreSQL_select_Query = ("ALTER TABLE PUBLISHER rename COLUMN publisher_estd to publisher_year;")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)

            elif option == 4:
                try:
                    cursor = connection.cursor()
                    postgreSQL_select_Query = (" TRUNCATE TABLE publisher; ")
                    cursor.execute(postgreSQL_select_Query)

                    conn.commit()
                    cursor.close()

                except (Exception, psycopg2.Error) as error:
                    print("Error while fetching data from PostgreSQL", error)

    # DML Queries
    elif Topic == 2:
                option = int(input('1.Insert, 2.Update, 3.Delete ' ))
                if option ==1:
                    try:
                        cursor = conn.cursor()
                        postgres_insert_query = """ INSERT INTO publisher(publisher_id,
                        publisher_name, publisher_estd, publisher_location, publisher_type)
                        VALUES (%s,%s,%s,%s,%s)"""

                        user_input = input('Enter space-separated integers: ').split()

                        record_to_insert = [(user_input)]

                        for i in record_to_insert:
                            cursor.execute(postgres_insert_query, i)

                            conn.commit()
                            count = cursor.rowcount
                        print(count, "Record inserted successfully into publisher table")

                        cursor.close()

                    except (Exception, psycopg2.Error) as error:
                        print("Failed to insert record into publisher table", error)

                elif option == 2:
                    def updateTable(publisherId, establishedYear):
                        try:
                            cursor = conn.cursor()
                            # Update single record now
                            sql_update_query = """Update publisher set publisher_estd = %s where publisher_id = %s"""
                            cursor.execute(sql_update_query,(establishedYear, publisherId))
                            conn.commit()
                            count = cursor.rowcount
                            print(count, "Record Updated successfully ")

                            cursor.close()

                        except (Exception, psycopg2.Error) as error:
                            print("Error in update operation", error)


                    # call the update function
                    publisherId = input("Enter any value:")
                    establishedYear = 2000
                    updateTable(publisherId, establishedYear)


                elif option == 3:
                    def deleteData(publisherId):
                        try:
                            cursor = conn.cursor()
                            # Update single record now
                            sql_delete_query = """Delete from publisher where publisher_id = %s"""
                            cursor.execute(sql_delete_query, (publisherId,))
                            conn.commit()
                            count = cursor.rowcount
                            print(count, "Record deleted successfully ")

                            cursor.close()

                        except (Exception, psycopg2.Error) as error:
                            print("Error in Delete operation", error)


                    publisherId = input("enter any value:")
                    deleteData(publisherId)

                elif option == 4:
                    print("hello world")

    # DCL Queries
    elif Topic == 3:
                option = int(input('1.Grant, 2.Revoke' ))
                if option ==1:
                    print("grant the data")

                elif option == 2:
                    print("revoke the data")

    # Join methods
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


    elif option == 6:
        # cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")
        print("you are exited form the database")
        break;
