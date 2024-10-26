//tag = document.getElementById("title1-")
//tag.
function getCsrfToken() {
    tag = document.getElementById("csrf")
    token = tag.value
    return token
}

console.log(getCsrfToken())

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

/*
function notification() {
    fetch("http://127.0.0.1:8000/notification/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCsrfToken()
        },
        credentials: "same-origin"
    }).then(response => response.json()).then(data => {
        let count = data["count"]
        let element = document.getElementById("notification")
        element.innerHTML = count
    }).catch(error => console.log("Error:", error))

}

notification()
*/

function get_user_details() {
    tag = document.getElementById("user_id")
    user_id = parseInt(tag.value)
    let user_details = fetch("http://127.0.0.1:8000/user_details", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCsrfToken()
        },
        body: JSON.stringify({"id": user_id})
    })
}

get_user_details()