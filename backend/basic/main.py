class Student:
    def __init__(self, id, name, age, major, hackjum):
        self.id = id
        self.__name = name
        self.__age = age
        self.__major = major
        self.__hackjum = hackjum

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def major(self):
        return self.__major
    
    @property
    def hackjum(self):
        return self.__hackjum
    
    def __str__(self):
        return self.__name

from abc import *

class StduentManagerRepo:
    @abstractmethod
    def add_student(self, student): # 학생 추가
        pass

    @abstractmethod
    def recieve_student(self): # 학생 출력
        pass

    @abstractmethod
    def list_student(self): # 전체 학생 조회
        pass

    @abstractmethod
    def search_student(self, name): # 학생 조회
        pass

    @abstractmethod
    def delete_student(self, name): # 학생 제거
        pass

    @abstractmethod
    def update_student(self, name, student): # 학생 수정
        pass


class StudentMangerImpl(StduentManagerRepo):
    def __init__(self):
        self.__student_list = []
    
    def add_student(self, student): # 학생 추가
        self.__student_list.append(student)
        print(f"{student.name} 학생이 추가되었습니다.")

    def recieve_student(self): # 학생 출력
        for student in self.__student_list:
            print(student)

    def list_student(self): # 전체 학생 조회
        return self.__student_list
    
    def search_student(self, name): # 학생 조회
        for student in self.__student_list:
            if student.name == name:
                return student
        return None
    
    def delete_student(self, name): # 학생 제거
        for student in self.__student_list:
            if student.name == name:
                self.__student_list.remove(student)
                print(f"{name} 학생이 삭제되었습니다.")
                return
        print(f"{name} 학생이 존재하지 않습니다.")

    def update_student(self, name, student): # 학생 수정
        for i in range(len(self.__student_list)):
            if self.__student_list[i].name == name:
                self.__student_list[i] = student
                print(f"{name} 학생이 수정되었습니다.")
                return
        print(f"{name} 학생이 존재하지 않습니다.")

class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentMangerImpl()

    def add_student(self, student): # 학생 추가
        self.__student_repo.add_student(student)

    def recieve_student(self): # 학생 출력
        self.__student_repo.recieve_student()

    def list_student(self): # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        self.__student_repo.delete_student(name)

    def update_student(self, name, student): # 학생 수정
        self.__student_repo.update_student(name, student)

def main(manager):
    while True:
        menu = input("===============\n1. 학생 추가\n2. 학생 출력\n3. 전체 학생 조회\n4. 학생 조회\n5. 학생 제거\n6. 학생 수정\n7. 종료\n===============\n")
        if menu == "1":
            id = input("학번: ")
            name = input("이름: ")
            age = input("나이: ")
            major = input("전공: ")
            hackjum = input("학점: ")
            manager.add_student(Student(id, name, age, major, hackjum))
        elif menu == "2":
            manager.recieve_student()
        elif menu == "3":
            for student in manager.list_student():
                print(student)
        elif menu == "4":
            name = input("이름: ")
            student = manager.search_student(name)
            if student != None:
                print(student)
            else:
                print(f"{name} 학생이 존재하지 않습니다.")
        elif menu == "5":
            name = input("이름: ")
            manager.delete_student(name)
        elif menu == "6":
            name = input("이름: ")
            id = input("학번: ")
            age = input("나이: ")
            major = input("전공: ")
            hackjum = input("학점: ")
            manager.update_student(name, Student(id, name, age, major, hackjum))
        elif menu == "7":
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)
