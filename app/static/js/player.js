function notify() {
    document.getElementById('notify').style.visibility = "visible";
}

function getPlayerInfo() {
    var player = {};
    player.id = document.getElementById('playerId').value;
    player.name = document.getElementById('playerName').value;
    player.rank = document.getElementById('playerRank').value;
    player.hometown = document.getElementById('playerHometown').value;
    player.birthYear = parseInt(document.getElementById('playerBirthYear').value);
    player.clubId = document.getElementById('playerClub').value;
    return player;
}

function savePlayer() {
    var player = getPlayerInfo();
    if (player.id === '') {
        var players = [player];
        fetch('/players', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(players),
        })
            .then((json) => {
                console.log(json);
                notify();
            })
    } else {
        fetch('/player/' + player.id, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(player),
        })
            .then((json) => {
                console.log(json);
                notify();
            })
    }
}