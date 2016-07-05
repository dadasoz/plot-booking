$(document).ready(function() {
    loadData();
    loadAllProjects();

    checkQueryParam();

    calculateLoanAmount();

    $(document).on('click', '.booking-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#booking-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/booking/" + id + "/", function(data, status) {
                $("#pk").val(data.id);
                $("#first_name").val(data.first_name);
                $("#middle_name").val(data.middle_name);
                $("#last_name").val(data.last_name);
                $("#occupation").val(data.occupation);
                $("#dob").val(data.dob);
                $("#age").val(data.age);
                $("#marriage_anniversary").val(data.marriage_anniversary);
                $("#agriculture_status").val(data.agriculture_status);

                $("#update-booking").attr("data-pk", data.id);
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#btn-add-booking', function() {
        $("#booking-form")[0].reset();
        $(".edit-label").hide();
        $(".add-label").show();
        $("#booking-modal").modal("show");
    });


    $(document).on('click', '#update-booking', function() {
        var form_data = $("#booking-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.patch("/api/booking/update/" + id + "/", form_data, function(data, status) {
                loadData();
                $("#booking-modal").modal("hide");
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#add-booking', function() {
        form_data = {
            'plot_no': $("#plot_id").val(),
            'booking_date': $("#booking_date").val(),
            'customer': $("#customer_id").val(),
            'booking_amount': $("#booking_amount").val(),
        }
        $.post("/api/booking/create/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#booking-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

    $(document).on('click', '.booking-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk", id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/booking/delete/" + id + "/").done(function(data, textStatus, jqXHR) {
            if (jqXHR.status == 204) {
                loadData();
                $("#delete-confirm").modal("hide");
            } else {
                console.log("Error");
            }
        })
    });

    $(document).on('click', '#btn-select-customer', function() {
        $("#customer-details").hide();
        $("#customer-list").show();
        loadCustomers();
    });

    $(document).on('click', '.btn-list-select-customer', function() {
        id = $(this).attr("data-pk");
        $("#customer-details").show();
        $("#customer-list").hide();
        loadCustomerDetails(id);
    });



    $(document).on('click', '#select-plot', function() {
        plot_no = $("#plot_no").val();
        project = $("#project option:selected").val();
        loadPlotDetailsByPlotNo(project, plot_no);
    });


    $(document).on('click', '.customer-view', function() {
        id = $(this).attr("data-pk");
        $("#customer-details-modal").modal("show");
        $.get("/api/booking/" + id + "/", function(data, status) {
            $("#lbl-name").text(data.first_name + " " + data.middle_name + " " + data.last_name);
            $("#lbl-occupation").text(data.occupation);
            $("#lbl-dob").text(data.dob);
            $("#lbl-age").text(data.age);
            $("#lbl-marriage_anniversary").text(data.marriage_anniversary);
            $("#lbl-agriculture_status").text(data.agriculture_status);

            $("#lbl-email").text(data.email);
            $("#lbl-mobile").text(data.mobile);
            $("#lbl-alternate_mobile").text(data.alternate_mobile);
            $("#lbl-address1").text(data.address1);
            $("#lbl-address2").text(data.address2);
            $("#lbl-pin_code").text(data.pin_code);
            //$("#photo").text(data.photo);
        });
    });

    $(document).on('click', '#emi', function() {
        var checkbox = this;
        if($(checkbox).is(':checked')){
            $(".emi-div").show();
            $(".payments-div").show();
        }else{
            $(".emi-div").hide();
            $(".payments-div").hide();
        }
    });

});

function loadData() {
    $.get("/api/booking/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function loadCustomers() {
    $.get("/api/customers/", function(data, status) {
            showCustomerList(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}


function loadPlotDetailsByPlotNo(project, plot_no){
    $.get("/api/projects/plots/" + project + "/" + plot_no + "/", function(data, status) {
            if (status === "success") {
                $("#basic_cost").val(data.basic_cost);
                $("#project").val(data.project).change();
                $("#facing").val(data.facing);
                $("#width").val(data.width);
                $("#breadth").val(data.breadth);
                $("#area").val(data.area);
                $("#survey_no").val(data.survey_no);
                $("#rate_per_sqft").val(data.rate_per_sqft);
                $("#total_amount").val(data.basic_cost);
                $("#plot_no").val(plot_no);
                $("#plot_id").val(data.pk);
            } else {
                alert("Not found");
                $("#plot_no").val("");
            }
        })
}

function loadAllProjects() {
    $.get("/api/projects/for-plots/", function(data, status) {
            for (var count = 0; count < data.length; count++) {
                project = data[count];
                $("#project").append("<option value='" + project.pk + "'>" + project.project_name + "</option>");
            }
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {
    destroyTable("#bookings-data");
    table = $('#bookings-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        booking = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-view" data-pk="' + booking.pk + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-edit" data-pk="' + booking.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-delete" data-pk="' + booking.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([booking.customer_name, booking.plot_no, booking.basic_amount, booking.booking_amount, booking.customer_email, booking.customer_email, buttons]).draw(true);
    }
}


function showCustomerList(data) {

    destroyTable("#customer-data");
    table = $('#customer-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        customer = data[count];
        buttons = '<button type="button" class="btn btn-xs btn-inverse btn-list-select-customer" data-pk="' + customer.pk + '">Select</button>';
        table.row.add([customer.full_name, customer.email, customer.mobile, customer.alternate_mobile, customer.address1, buttons]).draw(true);
    }
}

function loadCustomerDetails(id) {
    $.get("/api/customers/" + id + "/", function(data, status) {
        $("#customer_id").val(data.id);
        $("#customer_name").val(data.first_name + " " + data.middle_name + " " + data.last_name);
        $("#occupation").val(data.occupation);
        $("#dob").val(data.dob);
        $("#age").val(data.age);
        $("#marriage_anniversary").val(data.marriage_anniversary);
        $("#agriculture_status").val(data.agriculture_status);

        $("#email").val(data.email);
        $("#mobile").val(data.mobile);
        $("#alternate_mobile").val(data.alternate_mobile);
        $("#address1").val(data.address1);
        $("#address2").val(data.address2);
        $("#pin_code").val(data.pin_code);
    });
}

function checkQueryParam(){
    if(getQuery("plot_no")){
        loadPlotDetailsByPlotNo(getQuery("project"), getQuery("plot_no"));
        $("#booking-modal").modal("show");
        $(".edit-label").hide();
        $(".add-label").show();
    }
    if(getQuery("customer")){
        loadCustomerDetails(getQuery("customer"));
        $("#booking-modal").modal("show");
        $(".edit-label").hide();
        $(".add-label").show();
    }
}

function getQuery(q) {
    return (window.location.search.match(new RegExp('[?&]' + q + '=([^&]+)')) || [, null])[1];
}

$(document).on('click', '#calculate-emi', function() {
    calculateEMI();
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