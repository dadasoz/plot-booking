
$.loginPost = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'POST',
        beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
        'url': url,
        'data': data,
        'dataType': 'text/html',
        'success': callback,
        'error':callback,
    });
};

$.postJSON = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'POST',
        beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'success': callback
    });
};

$.getJSON = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'POST',
        beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
        'url': url,
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'success': callback
    });
};


function get_days_from_seconds(seconds){
    seconds = parseInt(seconds);
    return new Date().getTime() + seconds*1000;
}