import pytest
from main import StudentsInMLOps
def test_enroll_students():
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(5)
    assert mlops_class.getTotalStrength() == 5

def test_drop_students():
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(3)
    assert mlops_class.getTotalStrength() == 7

def test_invalid_drop_students():
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(8)
    mlops_class.dropStudents(10)
    assert mlops_class.getTotalStrength() == 8

def test_get_class_name():
    mlops_class = StudentsInMLOps()
    assert mlops_class.getClassName() == "MLOps"

if __name__ == "__main__":
    pytest.main()

#--