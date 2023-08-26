function binarySearch(targ, array) {
  let leftIndex = 0;
  let rightIndex = array.length - 1;

  while (leftIndex <= rightIndex) {
    let midIndex = Math.floor((leftIndex + rightIndex)/ 2)
    if (array[midIndex] === targ) {
        return midIndex
    } 
    if (targ < array[midIndex]) {
        rightIndex = midIndex -1
    } else {
        leftIndex = midIndex +1 
    }
  }
}

const array = [10, 20, 7, 12, 30, 40, 50];
const value = 10;

console.log(binarySearch(value, array))
//  BIG O : O(logn)