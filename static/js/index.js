// server-side rendering
const generateBtn = document.getElementById('btn-generate');
generateBtn.onclick = function () {
    window.location = "/show-workouts"
}

// client-side rendering
// function loadWorkouts(data) {
//     for (let workout of data) {
//         let movements = "<ul>"
//         for (let movement of workout.movements) {
//             movements += "<li>" + movement + "</li>"
//         }

//         const div = document.createElement("div")
//         div.innerHTML = `
//         <h5>${workout.label}</h5>
//         ${movements}
//         <br></br>`

//         workoutDiv.appendChild(div)
//     }
// }

// function handleResponse(response) {
//     response.json().then(loadWorkouts)
// }

// const workoutDiv = document.getElementById("client-side-rendered-workouts")
// fetch("/generate-workouts").then(handleResponse)