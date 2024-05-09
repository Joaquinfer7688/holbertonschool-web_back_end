export default function updateStudentGradeByCity(listofstudents, city, newGrades) {
  const studentsInCity = listofstudents.filter((student) => student.city === city);

  const updatedStudents = studentsInCity.map((student) => {
    const newGrade = newGrades.find((gradeObj) => gradeObj.studentId === student.id);

    return {
      ...student,
      grade: newGrade ? newGrade.grade : 'N/A',
    };
  });
  return updatedStudents;
}
