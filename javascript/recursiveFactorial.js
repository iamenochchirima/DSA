function recursiveFactorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * recursiveFactorial(n - 1);
    }
}
 
console.log(recursiveFactorial(0));

// BIG O = O(n)