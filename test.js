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
        let currIndex = gamesCurrIndex[i];
        let frameCount = frameCounts[i];

        frames[currIndex].style.display = "none";
        currIndex = currIndex + 1 >= frameCount ? 0 : currIndex + 1;
        frames[currIndex].style.display = "block";

        games[i] = frames;
        gamesCurrIndex[i] = currIndex;
    }
}

setInterval(changeFrame, 500);