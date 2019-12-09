const containers = document.getElementsByClassName("tournament-container");
let games = [];
let gamesCurrIndex = [];
let frameCounts = [];

for (container of containers) {
    let frames = container.childNodes;
    for (frame of frames) frame.style.display = "none";
    frames[0].style.display = "block";
    games.push(frames);
    gamesCurrIndex.push(0);
    frameCounts.push(frames.length);
}

function changeFrame() {
    for (let i = 0; i < games.length; i++) {
        let frames = games[i];
        let frameCount = frameCounts[i];
        let currIndex = gamesCurrIndex[i];

        let currFrame = Math.min(currIndex, frameCount - 1);
        frames[currFrame].style.display = "none";
        currIndex = currIndex + 1 > frameCount + 3 ? 0 : currIndex + 1;
        currFrame = Math.min(currIndex, frameCount - 1);
        frames[currFrame].style.display = "block";


        games[i] = frames;
        gamesCurrIndex[i] = currIndex;
    }
}

setInterval(changeFrame, 500);