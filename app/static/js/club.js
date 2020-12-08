function deleteMember(id) {
    var a = confirm("Are you sure to delete?");
    if (a) {
        fetch('/player/' + id, {
            method: 'DELETE',
        })
        .then((json) => {
            console.log(json);
            location.reload();
        })
    }
}

function getClubInfo() {
    var club = {};
    club.name = document.getElementById('clubName').value.trim();
    club.province = document.getElementById('clubProvince').value.trim();
    club.address = document.getElementById('clubAddress').value.trim();
    club.contact = document.getElementById('clubContact').value.trim();
    return club;
}

function updateClub(id) {
    var club = getClubInfo()
    fetch('/club/' + id, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(club),
    })
        .then((json) => {
            console.log(json);
            alert('Success!')
            //notify();
        })
}

function addClub() {
    var club = getClubInfo()
    var clubs = [club];
    fetch('/club', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clubs),
    })
        .then((json) => {
            console.log(json);
            //notify();
        })
}