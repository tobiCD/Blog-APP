const audio = document.querySelector("#audio{{ room.songs.id }}");
const progressBar = document.querySelector("#{{ room.songs.id }} .progress-bar");
const playSongBtn = document.querySelector("#{{ room.songs.id }} .play-song");
playSongBtn.addEventListener("click", function () {
    if (audio.paused) {
        // Logic to play the song
        audio.play();
    } else {
        // Logic to pause the song
        audio.pause();
    }
});

audio.addEventListener("timeupdate", function (e) {
    // Logic to update the progress bar and current time
    const { currentTime, duration } = e.srcElement;
    const percentWidth = (currentTime / duration) * 100;
    progressBar.style.width = `${percentWidth}%`;
    const time = formatTime(currentTime);
    // Update the display of current time
});
console.log("Play button clicked");
