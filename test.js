const container = document.getElementById("tournament-container");
const frames = container.childNodes;

let currFrame = 0;
let totalFrames = frames.length;

console.log(frames);

for (frame of frames) {
    frame.style.display = "none";
}
frames[0].style.display = "block";

function changeFrame() {
    frames[currFrame].style.display = "none";
    currFrame = currFrame + 1 >= totalFrames ? 0 : currFrame + 1;
    frames[currFrame].style.display = "block";
}

setInterval(changeFrame, 500);