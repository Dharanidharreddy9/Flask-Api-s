

# Execute a command: this creates a new table
cursor.execute('CREATE TABLE Company(customer_id int primary key,first_name varchar(100), last_name varchar(100), age int, country varchar(100))')


    # Insert data into the table
    cursor.execute('INSERT INTO Company (customer_id, first_name, last_name, age, country)'
                'VALUES (%s, %s, %s, %s, %s)',
                (1,'John','Doe',31,'USA')
                )

    cursor.execute('INSERT INTO Company (customer_id, first_name, last_name, age, country)'
                'VALUES (%s, %s, %s, %s, %s)',
                (2,'Robert','Luna',22,'USA')
                )

    cursor.execute('INSERT INTO Company (customer_id, first_name, last_name, age, country)'
                'VALUES (%s, %s, %s, %s, %s)',
                (3,'Davis','Robinson',22,'UK')
                )

    cursor.execute('INSERT INTO Company (customer_id, first_name, last_name, age, country)'
                'VALUES (%s, %s, %s, %s, %s)',
                (5,'John','Reinharbit',25,'UK')
                )

    cursor.execute('INSERT INTO Company (customer_id, first_name, last_name, age, country)'
                'VALUES (%s, %s, %s, %s, %s)',
                (6,'Betty','Doe',28,'UAE')
                )
