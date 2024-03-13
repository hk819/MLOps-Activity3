class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        """
        Enroll students in the MLOps class.

        Parameters:
        - count (int): Number of students to enroll.
        """
        if count > 0:
            self.total_strength += count
            print(f"{count} students enrolled in {self.class_name}.")

    def dropStudents(self, count):
        """
        Drop students from the MLOps class.

        Parameters:
        - count (int): Number of students to drop.
        """
        if count > 0 and count <= self.total_strength:
            self.total_strength -= count
            print(f"{count} students dropped from {self.class_name}.")
        else:
            print("Invalid number of students to drop.")

    def getTotalStrength(self):
        """
        Get the total strength of students in the MLOps class.

        Returns:
        - int: Total number of students.
        """
        return self.total_strength

    def getClassName(self):
        """
        Get the name of the class.

        Returns:
        - str: Class name.
        """
        return self.class_name

# Example usage:
if __name__ == "__main__":
    mlops_class = StudentsInMLOps()

    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(2)

    total_strength = mlops_class.getTotalStrength()
    class_name = mlops_class.getClassName()

    print(f"{class_name} has a total strength of {total_strength} students.")
