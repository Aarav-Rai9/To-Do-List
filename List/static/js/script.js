//tag = document.getElementById("title1-")
//tag.
function getCsrfToken() {
    tag = document.getElementById("csrf")
    token = tag.value
    return token
}

element = document.getElementsByClassName("list_title")
for (let i=0;i<element.length;i++) {
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
    console.log(self)
    })
}