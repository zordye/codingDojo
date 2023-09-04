function loops()
{
    console.log("odd numbers")
    for(x = 1; x <= 20; x++)
    {
        if(x%2 != 0)
        {
            console.log(x)
        }
    }

    console.log("decreasing multiples of 3")
    for(y = 100; y >= 0; y--)
    {
        if(y%3 == 0)
        {
            console.log(y)
        }
    }

    console.log("sequence")
    for(z = 4; z >= -3.5; z = z - 1.5)
    {
        console.log(z)
    }

    console.log("sigma")
    var sum = 0
    for(a = 1; a <= 100; a++)
    {
        sum = sum + a
    }
    console.log(sum)

    console.log("factorial")
    var product = 1
    for(b = 1; b <= 12; b++)
    {
        product = product * b
    }
    console.log(product)
}

loops()