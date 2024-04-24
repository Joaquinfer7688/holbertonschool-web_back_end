export default function appendToEachArrayValue(array, appendString) {
  const val = [];
  for (const value of array) {
    val.push(appendString + value);
  }

  return val;
}
