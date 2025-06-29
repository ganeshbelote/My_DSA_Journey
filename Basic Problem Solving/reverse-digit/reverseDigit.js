function reverseDigit(num){
    let res = 0
    while(num > 0){
        let ld = (num % 10)
        res = (res * 10) + ld
        num = Math.floor(num/10)
    }
    return res
}

console.log(reverseDigit(5267))