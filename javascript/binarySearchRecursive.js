function binarySearchRecursive(arr, target) {
  return search(arr, target, 0, arr.length - 1);
}

function search(arr, target, leftIndex, rightIndex) {
  if (leftIndex > rightIndex) {
    return -1;
  }
  let midIndex = Math.floor((leftIndex + rightIndex) / 2);
  if (arr[midIndex] === target) {
    return midIndex;
  }
  if (target < arr[midIndex]) {
    return search(arr, target, leftIndex, midIndex - 1);
  } else {
    return search(arr, target, midIndex + 1, rightIndex);
  }
}

const array = [10, 20, 7, 12, 30, 40, 50];
const value = 10;

console.log(binarySearchRecursive(array, value));
