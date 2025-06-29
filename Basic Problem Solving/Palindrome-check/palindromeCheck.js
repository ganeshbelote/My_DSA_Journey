const palindromeCheck = num => {
  let dup = num
  let rev = 0
  while (num > 0) {
    let ld = num % 10
    rev = rev * 10 + ld
    num = Math.floor(num / 10)
  }
  console.log(rev)
  if (dup == rev) {
    return true
  } else {
    return false
  }
}

console.log(palindromeCheck(3773))
console.log(palindromeCheck(1234))
