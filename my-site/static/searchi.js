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


function searching(url1) {
    var content = document.getElementById(searchform.data.value);
    if (content.length === 0 || !content.trim()) {
        document.getElementById('error').innerHTML = 'Please try a valid data...'
    } else {

        $.ajax({
            url: url1, // the endpoint
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            },
            data: {
                //CSRF: getCSRFTokenValue(),
                'search': content
            },
        });

    }
}