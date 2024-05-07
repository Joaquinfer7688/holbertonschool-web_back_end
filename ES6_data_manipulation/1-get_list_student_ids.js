export default function getListStudentIds(studentarray) {
  if (!Array.isArray(studentarray)) {
    return [];
  }
  return studentarray.map((student) => student.id);
}
