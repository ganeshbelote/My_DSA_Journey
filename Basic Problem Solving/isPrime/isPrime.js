const isPrime = (num) => {
    if (num == 2) return "2 is niether be prime nor be composite"
    let sqrt = Math.floor(Math.sqrt(num))
    for(let i = 2 ; i <= sqrt; i++){
        if(num%i==0){
            return false
        }
    }
    return true
}

console.log(isPrime(36))
console.log(isPrime(17))
console.log(isPrime(3))
console.log(isPrime(1483))


