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

function cart(Bid, url1) {
    var a = parseInt(Bid);
    var b = document.getElementById("quantity").value;
    $.ajax({
        url: url1, // the endpoint
        type: "POST",
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        },
        data: {
            'Bid': a,
            'quantity': b
        },
        success: function(recieved) {

            document.getElementById('cart_count').innerHTML = recieved;
        },
        error: function(data) {
            alert('Failure');
        },
    });
}