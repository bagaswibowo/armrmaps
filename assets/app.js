//side bar
function toggleNav() {
    if(document.getElementById("mySidenav").style.width === "250px") {
        document.getElementById("mySidenav").style.width = "0px";
        document.getElementById("mySidenavSpacer").style.width = "0px";
        document.getElementById("mySidenavSpacer").style.marginRight = "0px";
    } else if (document.getElementById("mySidenav").style.width = "0px") {
        document.getElementById("mySidenav").style.width = "250px";
        document.getElementById("mySidenavSpacer").style.width = "250px";
        document.getElementById("mySidenavSpacer").style.marginRight = "50px";
    }
}

//console.log("hai")

//checkreport



const dbRefObject = firebase.database().ref().child("data");

dbRefObject.on('child_added', snap => {
    console.log(snap.val());

});