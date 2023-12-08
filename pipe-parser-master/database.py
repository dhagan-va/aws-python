import pyodbc

from env import envdef, envreq


def save(data):
    hostname = envreq("RDS_HOSTNAME")
    port = envdef("RDS_PORT", 1433)
    db_name = envreq("RDS_DB_NAME")
    username = envreq("RDS_USERNAME")
    password = envreq("RDS_PASSWORD")

    cs = f'DRIVER=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1;SERVER={hostname}:{port};DATABASE={db_name};UID={username};PWD={password};'
    conn = pyodbc.connect(cs, timeout=5)

    columns = []
    values = []
    for key in data.keys():
        columns.push(key)
        values.push(data[key])

    print(",".join(columns))
    print(",".join(values))

    # cursor = conn.cursor()

    # cursor.execute('''
    #                 INSERT INTO Report (product_id, product_name, price)
    #                 VALUES
    #                 (5,'Chair',120),
    #                 (6,'Tablet',300)
    #                 ''')
    # conn.commit()
