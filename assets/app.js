//side bar
function openNav() {
    if(document.getElementById("mySidenav").style.width === "250px") {
        document.getElementById("mySidenav").style.width = "0px";
    } else if (document.getElementById("mySidenav").style.width = "0px") {
        document.getElementById("mySidenav").style.width = "250px";
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

console.log("hai")