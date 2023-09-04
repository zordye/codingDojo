function hideUser(name)
{
    name.style.display = "none"
}

function changeName()
{
    console.log("in")
    let names = ["Bob Ross", "John Smith", "John Doe", "Test Testerson", "Yeiri Desi"]
    var num = Math.floor(Math.random()*(5))
    console.log(num)
    let newName = names[num]
    console.log(newName)
    let currentName = document.getElementById("name")
    console.log(currentName)
    currentName.innerText = newName
}