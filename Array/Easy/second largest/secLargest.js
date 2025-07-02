const secLargest = arr => {
  let max = arr[0]
  let secMax = arr[0]
  const len = arr.length
  for (let i = 1; i < len; i++) {
    if (arr[i] > max) {
      secMax = max
      max = arr[i]
    } else if (arr[i] > secMax && arr[i] != max) {
      secMax = arr[i]
    }
  }
  console.log(secMax, max)
  return secMax
}

secLargest([2, -1, 5, 7, 3, 12, 35, -34, 18, -55])
