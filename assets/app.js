//side bar
function toggleNav() {
    if (document.getElementById("mySidenav").style.width === "250px") {
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



const reportRefObject = firebase.database().ref().child("data");
const archiveRefObject = firebase.database().ref().child("archive");


function archive(report) {

    reportRefObject.child(report).once('value').then(snap => {
        console.log(snap.val());
        archiveRefObject.child(report).set(snap.val());
        reportRefObject.child(report).set(null);
        window.location.reload();
    })
}