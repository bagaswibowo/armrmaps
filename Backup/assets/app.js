//side bar
function openNav() {
    if (document.getElementById("mySidenav").style.width === "250px") {
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



        const dbRefObject = firebase.database().ref("data").orderByChild("lng");

        const myList = document.getElementById("list");

        dbRefObject.on('value', snap => {
            const li = document.createElement('li');
            li.innerHTML =
                myList.appendChild(li);
        });

        // function addLi() {
        //     var node = document.createElement("li");
        //     var textnode = document.createTextNode("Water");
        //     node.appendChild(textnode);
        //     document.getElementById("list").appendChild(node);
        // }