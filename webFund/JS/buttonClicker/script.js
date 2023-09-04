function loginLogout(ele)
{
    if(ele.innerText == "Login")
    {
        ele.innerText = "Logout"
    }
    else 
    {
        ele.innerText = "Login"
    }
}

function hideMe(ele)
{
    ele.style.display = "none"
}