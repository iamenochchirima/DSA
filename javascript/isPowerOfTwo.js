const isPowerOfTwo = (n) => {
  if (n < 1) {
    return false;
  }

  while (n > 1) {
    if (n % 2 !== 0) {
      return false;
    }
    n = n / 2;
  }
  return true;
};

console.log(isPowerOfTwo(10));
console.log(isPowerOfTwo(3));
console.log(isPowerOfTwo(4));

// BIG 0 = O(log(n))

// ----------------------------OPTIMIZED-----------------------------------------------------------

const isPowerOfTwoBitWise = (n) => {
  if (n < 1) {
    return false;
  }
  return (n & (n-1)) === 0
};

// BIG 0 = O(1)

console.log(isPowerOfTwoBitWise(10));
console.log(isPowerOfTwoBitWise(3));
console.log(isPowerOfTwoBitWise(4));
