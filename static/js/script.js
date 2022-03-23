function send_request() {
    $.ajax({
        type: "POST",
        url: 'api/v1/create_url/',
        data: {
            'full_url': document.getElementById("full_url").value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            document.getElementById("short_url").value = document.location.origin + '/' + response['short_url']
        },
        error: function (response) {
            document.getElementById("short_url").value = response['responseJSON']['full_url']
        },
    });
}


window.onload = function () {
    create_url.onclick = function () {
        send_request();
    };
}