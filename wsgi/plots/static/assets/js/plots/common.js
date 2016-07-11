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

function calculateLoanAmount(){
    booking_amount = getValById("booking_amount");
    down_payment = getValById("down_payment");
    total_amount = getValById("total_amount");

    paid_amount = booking_amount + down_payment;

    loan_amount = total_amount - paid_amount;

    $("#loan_amount").val(loan_amount);

    return loan_amount;

}


function calculateEMI(){

    loan_amount = calculateLoanAmount();  
 
    intrest_rate  = getValById("emi_intrest");

    emi_day  = getValById("emi_day");

    duration = parseInt($("#emi_terms option:selected").val());

    emi_amount =  getMonthlyEMI(loan_amount, intrest_rate, duration);

    printEMI(emi_amount, duration, emi_day);

}

function printEMI(emi, duration, emi_day){
    destroyTable("#payments-table");
    table = $('#payments-table').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'print'
        ]
    });
    var date = new Date();
    for(var i=1; i<=duration; i++){
        date.setDate(emi_day);
        date.setMonth(date.getMonth() + 1);
        table.row.add([i, date.toLocaleFormat('%d-%b-%Y'), emi.toFixed(2)]).draw(true);
    }
}


function getMonthlyEMI(principle_amount, intrest_rate, duration){

    intrest_rate   = intrest_rate / 1200;

    emi_amount = 0;

    if(intrest_rate == 0){
        emi_amount =  principle_amount / duration;
    }else{
        emi_amount =  principle_amount * intrest_rate / (1 - (Math.pow(1/(1 + intrest_rate), duration)));
    }
    return emi_amount
}

function getTrueFalse(status){
    if(status){
        status = '<label class="tbl-icon icon-true"><i class="fa fa-check" aria-hidden="true"></i></label>';
    }else{
        status = '<label class="tbl-icon icon-false"><i class="fa fa-times " aria-hidden="true"></i></label>';
    }
    return status;
}