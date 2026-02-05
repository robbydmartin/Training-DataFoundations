import pandas as pd
from sqlalchemy import create_engine, text # this creates our database engine
from dotenv import load_dotenv # lets you read from our .env file
import psycopg2

engine = create_engine(
    "postgresql+psycopg2://postgres:0523@localhost:5432/postgres"
)

# We can execute raw SQL queries using the execute method using our engine
query = "SELECT student_id, first_name, last_name FROM student;"
student_df = pd.read_sql(query, engine) # need to pass 2 params: the query and the engine
print(student_df)

#create a new student in our database
# new_student = pd.DataFrame(
#     {"first_name" : ["Jayden"],
#      "last_name" : ["Miller"],
#      "email": ["jmill@email.com"],
#      "major" : ["MB"]
# })

# the sql method allows us to write a dataframe to a sql table
# new_student.to_sql(name="student", con=engine, if_exists="append", index=False)

update_student = text("UPDATE student SET phone = '5558990' WHERE student_id = 5;")

# update statements need to be executed using a connections
with engine.connect() as connection:
    connection.execute(update_student)
    connection.commit()


# delete records
delete_sql = text("DELETE FROM student WHERE email = 'jmill@email.com';")
with engine.connect() as connection:
    connection.execute(delete_sql)
    connection.commit()

# Call our stored procedures
# student_major = 'Computer Science'
# result = text(f"CALL selectCSStudents('{student_major}');")
# result_df = pd.read_sql(result, engine)
# print(result_df)
# with engine.begin() as connection:
#     connection.execute(text("CALL selectCSStudents(:major)"), {"major":"Computer Science"})

### Calling a stored procdure that works!
# student_id = 2
# course_count_sql = f"SELECT first_name, last_name, get_course_count({student_id}) AS course_count FROM student;"
# course_count_df = pd.read_sql(course_count_sql, engine)
# print(course_count_df)

## Calling another procedure that works lol
with engine.begin() as connection:
    connection.execute(text("CALL updatemajorstudents(:major, :student_id)"), {"major" : "Computer Science", "student_id" : 2})
    connection.commit()


# We want to make sure we are closing our connection/engine when we are don
connection.close()


