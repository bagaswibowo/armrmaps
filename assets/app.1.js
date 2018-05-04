var myTextarea = document.getElementById("myTextarea");
var submitBtn = document.getElementById("submitBtn");
const myList = document.getElementById("list");

const preObject = document.getElementById("object");

const dbRefObject = firebase.database().ref().child("data");
const dbRefList = dbRefObject.child("hobbies");

// dbRefObject.on('value', snap => {
//     preObject.innerText = JSON.stringify(snap.val(), null, 3);
// });

dbRefList.appendChild

dbRefList.on('child_added', snap => {
    const li = document.createElement('li');
    li.innerText = snap.val();
    li.id = snap.key;
    myList.appendChild(li);
});

dbRefList.on('child_changed', snap => {
    const liChanged = document.getElementById(snap.key);
    liChanged.innerText = snap.val();
});

dbRefList.on('child_removed', snap => {
    const liToRemove = document.getElementById(snap.key);
    liToRemove.remove();
});

function submitClick() {
    // window.alert(myTextarea);

    var mainText = myTextarea.value;

    dbRefList.push().set(mainText);
}

//side bar
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

console.log("hai");