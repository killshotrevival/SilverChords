function noticomment(url1, user_id) {
    hae = document.getElementById('hae').value;
    data = document.getElementById('data').value;
    alert(hae);
    $.ajax({
        url: url1,
        type: "POST",
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        },
        data: {

            'hae': hae,
            'data': data,
            'id': user_id
        },
        success: function(data) {
            document.getElementById('rtn').innerHTML = data
        }

    });

}