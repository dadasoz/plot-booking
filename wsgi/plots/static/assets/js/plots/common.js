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

$.post = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'POST',
        beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", "Bearer "+JSON.parse($.cookie('login_info')).access_token);
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'complete': callback,
    });
};

$.get = function(url, callback) {
    return jQuery.ajax({
        'type': 'GET',
        beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", "Bearer "+JSON.parse($.cookie('login_info')).access_token);
            },
        'url': url,
        'contentType': 'application/json',
        'dataType': 'json',
        'success': callback,
        'error':callback,
    });
};

$.put = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'PUT',
        beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", "Bearer "+JSON.parse($.cookie('login_info')).access_token);
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'success': callback,
    });
};

$.patch = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'PATCH',
        beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", "Bearer "+JSON.parse($.cookie('login_info')).access_token);
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'success': callback,
    });
};

$.delete = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'DELETE',
        beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", "Bearer "+JSON.parse($.cookie('login_info')).access_token);
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
    });
};

function get_days_from_seconds(seconds){
    seconds = parseInt(seconds);
    return new Date().getTime() + seconds*1000;
}

var table;

var destroyTable = function(id) {
    $(id).DataTable().clear().destroy();
};

function getValById(id){
    data = parseInt($("#"+id).val());
    if(isNaN(data)){
        return 0;
    }else{
        return data;
    }
}

$(document).ready(function(){
    $('.datepicker').datepicker({
        todayHighlight: true,
    });
});
