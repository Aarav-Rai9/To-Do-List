//tag = document.getElementById("title1-")
//tag.
function getCsrfToken() {
    tag = document.getElementById("csrf")
    token = tag.value
    return token
}

element = document.getElementsByClassName("list_title")
for (let i = 0; i < element.length; i++) {
    element[i].addEventListener("change", function (self) {
        id = self.target.id
        id_num = id.slice(7)
        tag = document.getElementById(id)
        content = tag.value
        let api = fetch("http://127.0.0.1:8000/edit-list-item/" + id_num, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken()
            },
            body: JSON.stringify({"description": content})
        })
        element = document.getElementById("notification")

    })
}

async function notification() {
    try {
        let id = sessionStorage.getItem("user_id")
        //let id = idObj.id
        let notification = await fetch("http://127.0.0.1:8000/notification/" + id, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken()
            }
        })

        if (notification.ok) {
            //let response = await notification.json()
            //element = document.getElementById("notification")
            //element.innerHTML = response.count
        }
    } catch (e) {
        console.error("ERROR", e)
    }
}


async function get_user_details() {
    tag = document.getElementById("user_id")
    user_id = parseInt(tag.value)
    try {
        let user_details = await fetch("http://localhost:8000/user_details/" + user_id, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken()
            }
        })

        if (user_details.ok) {
            let response = await user_details.json()
            sessionStorage.setItem("user_id", response.id)
            sessionStorage.setItem("full_name", response.first_name + " " + response.last_name)
            sessionStorage.setItem("email_address", response.email_address)
        }
    } catch (e) {
        console.error("ERROR:", e)
    }


}

function log() {
    console.log("hello world")
}


get_user_details()

setInterval(notification, 2000)


