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

function noti(username, url1, nnid) {
    $.ajax({
        url: url1, // the endpoint
        type: "POST",
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        },
        data: {
            //CSRF: getCSRFTokenValue(),
            'username': username,
            'id': nnid
        },
        success: function(recieved) {
            document.getElementById(data).textContent = recieved;
        },
        error: function(data) {
            alert(data);
        },
    });

}