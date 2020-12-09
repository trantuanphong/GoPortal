var lng = parseFloat(document.getElementById('clubLng').value);
var lat = parseFloat(document.getElementById('clubLat').value);
map.setCenter([lng,lat]);
map.setZoom(10);
var marker = new mapboxgl.Marker({
    draggable: true
})
    .setLngLat([lng, lat])
    .addTo(map);

function onDragEnd() {
    var lngLat = marker.getLngLat();
    document.getElementById('clubLng').value = lngLat.lng;
    document.getElementById('clubLat').value = lngLat.lat;
}
marker.on('dragend', onDragEnd);

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
    club.lat = document.getElementById('clubLat').value.trim();
    club.lng = document.getElementById('clubLng').value.trim();
    return club;
}

function updateClub(id) {
    if (id === 'None') {
        alert('Invalid id!');
    } else {
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