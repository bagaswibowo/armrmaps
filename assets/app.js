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

//console.log("hai")

//checkreport



const dbRefObject = firebase.database().ref().child("data");

dbRefObject.on('child_added', snap => {
    console.log(snap.val());

});