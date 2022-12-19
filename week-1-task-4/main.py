import psycopg2

# Connecting the database using psycopg2
Conn = psycopg2.connect(
        host="localhost",
        database="task_4",
        user='admin',
        password='root')

# While loop until user wants to exit from this loop it will continued
while True:
    option =int(input('\n 1.Insert, 2.Read, 3.Update, 4.Delete, 5. Exit \n Enter any one option:'))


    #If user select 1 then it will redirect to the Insert method
    if option == 1:
        try:
            cursor = Conn.cursor()
            postgres_insert_query = """ INSERT INTO publisher(publisher_id,
            publisher_name, publisher_estd, publisher_location, publisher_type)
            VALUES (%s,%s,%s,%s,%s)"""

            user_input = input('Enter space-separated integers: ').split()

            record_to_insert = [(user_input)]

            for i in record_to_insert:
                cursor.execute(postgres_insert_query, i)

                Conn.commit()
                count = cursor.rowcount
            print(count, "Record inserted successfully into publisher table")

            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into publisher table", error)


    #If user select 2 then it will redirect to the Get method
    elif option == 2:
        try:
            # creating a cursor object using he cursor() method
            cursor = Conn.cursor()
            postgreSQL_select_Query = "select * from publisher"
            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from publisher table using cursor.fetchall")
            publisher_records = cursor.fetchall()

            print("Print each row and it's columns values")
            for row in publisher_records:
                print("publisher_Id = ", row[0], )
                print("publisher_name = ", row[1])
                print("publisher_estd  = ", row[2])
                print("publisher_location  = ", row[3])
                print("publisher_type  = ", row[4], "\n")

            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)


    #If user select 3 then it will redirect to the Update method
    elif option == 3:
        def updateTable(publisherId, establishedYear):
            try:
                cursor = Conn.cursor()
                # Update single record now
                sql_update_query = """Update publisher set publisher_estd = %s where publisher_id = %s"""
                cursor.execute(sql_update_query,(establishedYear, publisherId))
                Conn.commit()
                count = cursor.rowcount
                print(count, "Record Updated successfully ")

                cursor.close()

            except (Exception, psycopg2.Error) as error:
                print("Error in update operation", error)


        # call the update function
        publisherId = input("Enter any value:")
        establishedYear = 2000
        updateTable(publisherId, establishedYear)

    #If user select 4 then it will redirect to the Delete method
    elif option == 4:
        def deleteData(publisherId):
            try:
                cursor = Conn.cursor()
                # Update single record now
                sql_delete_query = """Delete from publisher where publisher_id = %s"""
                cursor.execute(sql_delete_query, (publisherId,))
                Conn.commit()
                count = cursor.rowcount
                print(count, "Record deleted successfully ")

                cursor.close()

            except (Exception, psycopg2.Error) as error:
                print("Error in Delete operation", error)

        publisherId = input("enter any value:")
        deleteData(publisherId)


    #If user select 5 then user will be get out from this loop(function)
    elif option == 5:
        # cursor.close()
        Conn.close()
        print("PostgreSQL connection is closed")
        print("you are exited form the database")
        break;
