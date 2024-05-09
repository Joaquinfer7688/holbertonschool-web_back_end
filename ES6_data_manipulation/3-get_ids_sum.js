export default function getStudentIdsSum(listofstudents) {
  const sum = listofstudents.reduce((total, student) => total + student.id, 0);

  return sum;
}
