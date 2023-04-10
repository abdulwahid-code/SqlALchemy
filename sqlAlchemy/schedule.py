
from database import SessionLocal
from database import Data
from datetime import datetime, time
import mysql.connector
import time
from datetime import datetime
from mysql.connector import errorcode
def create_student_table():
    try:
        session=SessionLocal()
        session.execute("""
            CREATE TABLE students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                scheduled_time DATETIME,
                status VARCHAR(255), 
                repeat_interval INT, 
                repeat_type VARCHAR(255) 
                )
            """)
        session.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table created successfully.")    
        
        
def get_data(self):
    session=SessionLocal()
    
    query = "SELECT * FROM students"
    session.execute(query)
    rows =session.fetchall()
    return rows
def get_pending_data(self):
    session=SessionLocal()
    query = "SELECT * FROM students WHERE status IN ('scheduled', 'in progress')"
    session.execute(query)
    rows =session.fetchall()

    return rows

def update_status(self, id, status):
    session=SessionLocal()
    query = "UPDATE students SET status = %s WHERE id = %s"
    values = (status, id)
    session.execute(query, values)
    session.commit()
#interval update
def check_pending(self):
    now = datetime.now() 
    rows = get_pending_data()
    for row in rows:
        scheduled_time = row[3]
        repeat_interval = row[5]
        repeat_type = row[6]
        if repeat_interval is not None and repeat_type is not None:
            if now >= scheduled_time:
                name = row[1]
                age = row[2]
                insert_data(name, age, scheduled_time, repeat_interval, repeat_type)
                update_status(row[0], "scheduled")
                print(f"Task for {name} repeated at {now}")
                continue
        if now >= scheduled_time:
            id = row[0]
            name = row[1]
            update_status(id, "in progress")
            time.sleep(10) # simulate task being performed
            update_status(id, "completed")
            print(f"Status for task with id {id} and name {name} changed to completed at {datetime.now()}")

def insert_data(name, email, scheduled_time=None, repeat=None):
    session = SessionLocal()
    data = Data(name=name, email=email, scheduled_time=scheduled_time, repeat=repeat, status='scheduled')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been scheduled for insertion."

def edit_data(data_id, scheduled_time):
    session = SessionLocal()
    data = session.query(Data).filter_by(id=data_id).first()
    data.scheduled_time = scheduled_time
    session.commit()
    session.close()
    return "Scheduled time has been updated."

def delete_data(data_id):
    session = SessionLocal()
    data = session.query(Data).filter_by(id=data_id).first()
    session.delete(data)
    session.commit()
    session.close()
    return "Data has been deleted."

def insert_data_auto(name, email):
    session = SessionLocal()
    data = Data(name=name, email=email, scheduled_time=datetime.now(), status='completed')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been inserted automatically."

def insert_data_daily(name, email):
    session = SessionLocal()
    data = Data(name=name, email=email, repeat='daily', status='scheduled')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been scheduled for daily insertion."

def insert_data_weekly(name, email):
    session = SessionLocal()
    data = Data(name=name, email=email, repeat='weekly', status='scheduled')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been scheduled for weekly insertion."

def insert_data_monthly(name, email):
    session = SessionLocal()
    data = Data(name=name, email=email, repeat='monthly', status='scheduled')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been scheduled for monthly insertion."

def insert_data_custom(name, email, scheduled_time):
    session = SessionLocal()
    data = Data(name=name, email=email, scheduled_time=scheduled_time, repeat='custom', status='scheduled')
    session.add(data)
    session.commit()
    session.close()
    return "Data has been scheduled for custom insertion."
