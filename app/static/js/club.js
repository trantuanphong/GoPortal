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
    club.Name = document.getElementById('clubName').value.trim();
    club.Province = document.getElementById('clubProvince').value.trim();
    club.Address = document.getElementById('clubAddress').value.trim();
    club.Contact = document.getElementById('clubContact').value.trim();
    club.Lat = document.getElementById('clubLat').value.trim();
    club.Lng = document.getElementById('clubLng').value.trim();
    club.OpenDescription = document.getElementById('clubOpenDescription').value.trim();

    var open = '1';
    openWeekDays = document.getElementsByClassName('openWeekDay');
    for (var i = 0; i < openWeekDays.length; i++) {
        if (openWeekDays[i].checked) {
            open += '1';
        }
        else {
            open += '0';
        }
    }
    club.OpenDay = open;

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
                //console.log(json);
                alert('Success!');
                //notify();
            })
    }
}

function addClub() {
    var club = getClubInfo()
    var clubs = [club];
    fetch('/clubs', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clubs),
    })
        .then((json) => {
            //console.log(json);
            alert('Success!');
            //notify();
        })
}