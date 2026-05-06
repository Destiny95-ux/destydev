const API_URL = "http://127.0.0.1:8000/api/songs/";

async function loadSongs() {
  const res = await fetch(API_URL);
  const songs = await res.json();

  const grid = document.getElementById("songGrid");
  grid.innerHTML = "";

  songs.forEach(song => {
    grid.innerHTML += `
      <div class="card">
        <img src="${song.cover_image}" />
        <h3>${song.title}</h3>
        <p>${song.artist}</p>

        <div class="actions">
          <button onclick="playSong('${song.id}')">▶ Play</button>
          <button onclick="downloadSong('${song.audio_file}')">⬇ Download</button>
        </div>
      </div>
    `;
  });
}

function playSong(id) {
  fetch(`http://127.0.0.1:8000/api/songs/${id}/play/`, {
    method: "POST"
  });
  alert("Playing song...");
}

function downloadSong(fileUrl) {
  window.open(fileUrl, "_blank");
}

document.getElementById("searchInput").addEventListener("input", async (e) => {
  const query = e.target.value;

  const res = await fetch(`${API_URL}search?q=${query}`);
  const songs = await res.json();

  const grid = document.getElementById("songGrid");
  grid.innerHTML = "";

  songs.forEach(song => {
    grid.innerHTML += `
      <div class="card">
        <img src="${song.cover_image}" />
        <h3>${song.title}</h3>
        <p>${song.artist}</p>
      </div>
    `;
  });
});

loadSongs();
