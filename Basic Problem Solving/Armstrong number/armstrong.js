/* Armstrong number is a number that is equal to the sum of powers to its length of each digit
=> Let assume num = 153 , here length = 3
=> since product = 1^3 + 5^3 + 3^3 --> digit1^length + digit2^length + ...
=> if product == num then num is armstrong number
*/
const isArmstrong = (num) => {
    let k = String(num).length
    let dup = num
    let res = 0
    while(num > 0){
        let digit = num%10
        res += Math.pow(digit,k)
        num = Math.floor(num/10)
    }

    if(res == dup){
        return true
    }else{
        return false
    }
}

console.log(isArmstrong(153))
console.log(isArmstrong(123))
