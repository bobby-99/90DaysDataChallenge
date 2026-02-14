function getIndexToIns(array, num) {
  array.sort((a, b) => a - b)
  const index = array.findIndex(element => element >= num)
  return index === -1 ? array.length : index;
}
console.log(getIndexToIns([20, 3, 9], 4))