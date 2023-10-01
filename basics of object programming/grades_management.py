class Student:
    def __init__(self, name, surname, index_nr):
        if len(index_nr) != 6:
            print("Podano niepoprawny indeks")

        else:
            self.name = name.title()
            self.surname = surname.title()
            self.index_nr = index_nr
            self.grades = {"analiza": [], "algebra": [], "programowanie": []}


class JSOS(Student):
    def addgrade(self, course, grade):
        if isinstance(grade, tuple):
            for x in grade:
                self.grades[course].append(x)
        else:
            self.grades[course].append(grade)

    def showgrades(self, course):
        print(f"Oceny studenta {self.name} {self.surname} nr indeksu {self.index_nr} z {course} to : "
              f"{self.grades[course]}")

    def changegrade(self, course):
        self.showgrades(course)
        gradenr = int(input("Ktora ocene chcesz edytowac?")) - 1
        newgrade = int(input("Podaj nowa ocene"))
        self.grades[course][gradenr] = newgrade
        print(f"Oceny z podanego kursu po zmianie: {self.grades[course]}")


student1 = JSOS('imietest', 'nazwiskotest', '123456')
student2 = JSOS('Filip', 'Soltysiak', '266835')
student3 = JSOS('aaaaa', 'bbbbbbbbbb', '987654')

student1.addgrade("analiza", (3, 2, 4))
student1.addgrade("algebra", (3, 3, 3))
student1.addgrade("programowanie", (2, 3, 5))
student1.changegrade("analiza")

student2.addgrade("analiza", (4, 5, 4))
student2.addgrade("algebra", (3, 3, 3))
student2.addgrade("programowanie", (4, 5, 3))
student2.showgrades("analiza")

student3.addgrade("analiza", (3, 5, 4))
student3.addgrade("algebra", (3, 4, 3))
student3.addgrade("programowanie", (3, 3, 5))
