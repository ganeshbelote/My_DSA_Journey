const frequency = arr => {
  let len = arr.length
  let hash = {}
  for (let i = 0; i < len; i++) {
    if (!hash[arr[i]]) {
      hash[arr[i]] = 1
    } else {
      hash[arr[i]] += 1
    }
  }
  console.log(hash)
  return hash
}

frequency([1, 1, 2, 2, 3, 4, 3, 4, 3])
