function linearSearch(n, array) {
    for (i = 0; i < array.length; i++) {
        if (array[i] === n) {
            return i
        }
    }
    return -1
}

const array = [10, 20, 7, 12, 30, 40, 50];
const value = 50;

console.log(linearSearch(value, array))

// BIG O : O(n  )