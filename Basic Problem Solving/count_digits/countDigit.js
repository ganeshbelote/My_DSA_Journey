const countDigit = num => {
  return Math.floor(Math.log10(num) + 1)
}

const bruteForceCountDigit = num => {
  let count = 0
  while (num > 0) {
    num = Math.floor(num / 10)
    count++
  }
  return count
}

console.log(countDigit(4356), bruteForceCountDigit(4356))
