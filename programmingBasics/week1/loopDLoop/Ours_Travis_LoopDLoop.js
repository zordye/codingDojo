// We need a loop in oder to cycle through the different miles
// The starting point of the loop is 0
// The loop will stop when the variable reaches 6
// The loop will be set to end if the variable is greater than 5
// the variable representing the mile number is incrementing
// the only variable we need is mile

for(var mile = 0; mile < 6; mile++)
{
    if(mile == 2 || mile == 4)
    {
        console.log("Have a piece of candy.")
    }
}

var milesPerHour;

for(var mile = 0; mile < 6; mile++)
{
    if(mile == 2 && milesPerHour > 5.5 || mile == 4 && milesPerHour > 5.5)
    {
        console.log("Have a piece of candy.")
    }
}