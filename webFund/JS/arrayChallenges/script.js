function alwaysHungry(arr)
{
    var hungry = true
    for(x = 0; x < arr.length; x++)
    {
        if(arr[x] == "food")
        {
            console.log("yummy")
            hungry = false
        }
    }
    if(hungry)
    {
        console.log("I'm hungry")
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"])

alwaysHungry([4, 1, 5, 7, 2])

function highPass(arr, cutoff) {
    var filteredArr = [];
    for(x = 0; x < arr.length; x++)
    {
        if(arr[x] > cutoff)
        {
            filteredArr.push(arr[x])
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);


function betterThanAverage(arr) {
    var sum = 0;
    for(x = 0; x <arr.length; x++)
    {
        sum = sum + arr[x]
    }
    var count = 0
    for(y = 0; y <arr.length; y++)
    {
        if(arr[y] > sum / arr.length)
        {
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);

function reverse(arr) {
    var tempArr = []
    for(x = 0; x < arr.length; x++)
    {
        tempArr.unshift(arr[x])
    }
    arr = tempArr
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);

function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    var x = 0
    while(x < n - 2)
    {
        var y = fibArr[fibArr.length-1]
        var z = fibArr[fibArr.length-2]
        fibArr.push(y + z)
        x++
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]