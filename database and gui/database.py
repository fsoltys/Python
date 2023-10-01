#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect('test.db')

con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Employee;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        idEmployee varchar(3) PRIMARY KEY ASC,
        Surname varchar(250) NOT NULL,
        Position varchar(250) DEFAULT ''
    )""")
cur.executescript("""
    DROP TABLE IF EXISTS Attendance;
    CREATE TABLE IF NOT EXISTS Attendance (
        Workday varchar(2) PRIMARY KEY ASC,
        Place varchar(250) NOT NULL,
        idEmployee varchar(2) NOT NULL,
        Worktime varchar(3) NOT NULL,
        FOREIGN KEY(idEmployee) REFERENCES Employee(idEmployee)
    )""")

Employees = [
    ('1', 'Soltysiak', 'Barista'),
    ('2', 'Losowy', 'Barista'),
    ('3', 'Kowalski', 'Lider zmiany'),
    ('4', 'Pawelczak', 'Kierownik')
]
Attendance = (
    ('12', 'Nadodrze', '1', '8'),
    ('13', 'Rynek', '3', '5'),
    ('14', 'Rynek', '3', '7'),
    ('15', 'Nadodrze', '4', '8'),
    ('16', 'Nadodrze', '2', '7')
)

cur.executemany('INSERT INTO Employee VALUES(?,?,?)', Employees)
cur.executemany('INSERT INTO Attendance VALUES(?,?,?,?)', Attendance)
con.commit()


def nadodrzeemployees(): #a table showing all the employees in a specified place
    cur.execute(
        """
        SELECT Employee.idEmployee, Employee.Surname, Attendance.Place, Attendance.Worktime FROM Employee, Attendance
        WHERE Employee.idEmployee=Attendance.idEmployee
            AND Attendance.Place == 'Nadodrze'
        """)
    sqlresult = cur.fetchall()
    for entry in sqlresult:
        print(entry['idEmployee'], entry['Surname'])
    print('\n')


def worktimeatrynek(): #creates a table of total hours spent by the employees at a specified place
    cur.execute(
        """
        SELECT Employee.idEmployee, Employee.Surname, Attendance.Place, Attendance.Worktime FROM Employee, Attendance
        WHERE Employee.idEmployee=Attendance.idEmployee
            AND Attendance.Place == 'Rynek'
        """)
    sqlresult = cur.fetchall()
    for entry in sqlresult:
        print(entry['idEmployee'], entry['Surname'], entry['Worktime'])
    print('\n')


def baristas(): #showing all the emplyees with specified position
    cur.execute(
        """
        SELECT Employee.idEmployee, Employee.Surname, Employee.Position FROM Employee
        WHERE Employee.Position == 'Barista'
        """)
    sqlresult = cur.fetchall()
    for entry in sqlresult:
        print(entry['idEmployee'], entry['Surname'], entry['Position'])
    print('\n')


worktimeatrynek()
nadodrzeemployees()
baristas()

cur.execute('DELETE FROM Employee WHERE Position=?', ['Lider zmiany'])
worktimeatrynek()
nadodrzeemployees()
baristas()
