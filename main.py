import requests
import json
from flask import Flask, render_template
import jinja2

from student import Student

add_student_link = 'http://staging.bldt.ca/api/method/build_it.test.register_student'
edit_student_link = 'http://staging.bldt.ca/api/method/build_it.test.edit_student'
get_student_details_link = 'http://staging.bldt.ca/api/method/build_it.test.get_student_details'
delete_student_link = 'http://staging.bldt.ca/api/method/build_it.test.delete_student'
get_students_link = 'http://staging.bldt.ca/api/method/build_it.test.get_students'
students = []


def read_students():
    students.clear()
    response = requests.get(get_students_link)
    json_response = json.loads(response.text)
    for entry in json_response['data']:
        students.append(
            Student(full_name=entry['full_name'], s_id=entry['id'], level=entry['level'], mobile=entry['mobile_number'],
                    age=entry['age']))


def read_student():
    sid = input('please enter student id:  ')
    response = requests.get(get_student_details_link,
                            params={'id': sid})
    json_response = json.loads(response.text)
    entry = json_response['data']

    return Student(full_name=entry['full_name'], s_id=entry['id'], level=entry['level'], mobile=entry['mobile_number'],
                   age=entry['age'])


def save_students():
    read_students()
    file = open('students.txt', 'w', encoding="utf-8")

    for student in students:
        file.write(student.to_string(), )
    file.close()


def save_student():
    student = read_student()
    print(student.full_name)
    file = open(student.full_name + ' student_details.txt', 'w', encoding="utf-8")
    file.write(student.to_string(),)
    file.close()


def main_menu():
    print('--------------------------------------------------------------------------------')
    print('1.  Register new Student  ')
    print('2.  Edit Student Details')
    print('3.  Delete Student')
    print('4.  Export Student to text file')
    print('5.  Export Student Details to text file')
    print('6.  to exit :)')
    return input('please enter your choice:  ')


def add_student():
    print('--------------------------------------------------------------------------------')
    name = input('please enter student name:  ')
    age = input('please enter student age:  ')
    leve = input('please enter student level (A,B or C):  ')
    mobile = input('please enter student mobile number:  ')
    result = requests.get(add_student_link,
                          params={'full_name': name, 'age': age, 'level': leve, 'mobile_number': mobile})
    if result.status_code == 200:
        print('student has been added successfully')


def edit_student():
    sid = input('please enter student id:  ')
    result = requests.get(get_student_details_link,
                          params={'id': sid})
    if result.status_code == 200:
        name = input('please enter student name:  ')
        age = input('please enter student age:  ')
        leve = input('please enter student level (A,B or C):  ')
        mobile = input('please enter student mobile number:  ')
        result_edit = requests.post(edit_student_link,
                                    params={'id': sid, 'full_name': name, 'age': age, 'level': leve,
                                            'mobile_number': mobile})
        if result_edit.status_code == 200:
            print('student has been Edited successfully')
        else:
            print('Student does not exists')


def delete_student():
    sid = input('please enter student id:  ')
    result = requests.get(get_student_details_link,
                          params={'id': sid})
    if result.status_code == 200:
        delete_result = requests.get(delete_student_link,
                                     params={'id': sid})
        if delete_result.status_code == 200:
            print('student has been Deleted successfully')

    else:
        print('Student does not exists')


def handle_choice(user_choice):
    if user_choice == '6':
        exit()
    elif user_choice == '1':
        add_student()
    elif user_choice == '2':
        edit_student()
    elif user_choice == '3':
        delete_student()
    elif user_choice == '4':
        save_students()
    elif user_choice == '5':
        save_student()
    else:
        print('wrong choice please try again: ')


while True:
    choice = main_menu()
    handle_choice(choice)
