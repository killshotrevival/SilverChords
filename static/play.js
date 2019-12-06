function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function play(beatl, Bid, url1) {
    var audio = document.getElementById("cntl");
    audio.src = beatl;
    audio.load();
    audio.play();
    //var url1 = $("#Play_Button").attr("data-url");
    var a = parseInt(Bid);
    $.ajax({
        url: url1, // the endpoint
        type: "POST",
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        },
        data: {
            //CSRF: getCSRFTokenValue(),
            'Bid': a
        },
    });
}