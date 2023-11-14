import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "VR1Fqy5YeOrMnNZd",
                                  host = "db.tscfmjlnezdjlzwsmcmx.supabase.co",
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("\nConexión a supabase exitosa. ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)