const printDivisors = (num) => {
    let res = [1]
    for(let i = 2; i <= num;i++){
        if(num%i==0){
            res.push(i)
        }
    }
    return res
}

const optimalSol = (num) => {
    let res = []
    let sqrt = Math.floor(Math.sqrt(num))

    for(let i = 1; i <= sqrt; i++){
        if(num%i==0){
            res.push(i)
            if(i != Math.floor(num/i)){
                res.push(Math.floor(num/i))
            }
        }
    }
    return res.sort((a,b)=> a - b)
}


console.log(printDivisors(36))
console.log(printDivisors(17))
console.log(optimalSol(36))
console.log(optimalSol(17))
