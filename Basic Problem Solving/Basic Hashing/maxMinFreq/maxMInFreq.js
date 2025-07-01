const maxMinFeq = arr => {
    let len = arr.length
    let hash = {}
    for(let i = 0; i < len; i++){
        if(!hash[arr[i]]){
            hash[arr[i]] = 1
        }else{
            hash[arr[i]] += 1
        }
    }
    let maxFreq = -Infinity
    let minFreq = Infinity
    let max = null
    let min = null

    for(let key in hash){ 
        let freq = hash[key] 
        if(freq > maxFreq){
            maxFreq = freq
            max = parseInt(key)
        }
        if(freq < minFreq){
            minFreq = freq
            min = parseInt(key)
        }
    }
    return { "Hash":hash,"max":max,"min":min}
}


console.log(maxMinFeq([1,1,2,3,3,4,4,4]))