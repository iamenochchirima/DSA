function isPrime(n) {
  if (n < 2) {
    return false;
  }

  for (i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}
// BIG 0 = O(n)

// ----------------------------OPTIMIZED-----------------------------------------------------------
function isPrime(n) {
  if (n < 2) {
    return false;
  }

  for (i = 2; i < Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}

console.log(isPrime(41));

// BIG 0 = O(sqrt(n))
