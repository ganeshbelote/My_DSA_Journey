function palindrome(str){
    let start = 0
    let end = str.length - 1

    while(start < end){
        if(str[start] != str[end]) return false
        start++
        end--
    }

    return true
}

console.log(palindrome("madam"))
console.log(palindrome("ganesh"))
