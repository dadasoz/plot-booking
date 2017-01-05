$(document).ready(function() {
    loadData();

    $(document).on('click', '.sales-edit', function() {
        var id = $(this).attr("data-pk");
        document.location = "/frontend/accounts/sales/edit/"+id+"/";
    });

    $(document).on('click', '.sales-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk", id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/accounts/sales/delete/" + id + "/").done(function(data, textStatus, jqXHR) {
            if (jqXHR.status == 204) {
                loadData();
                $("#delete-confirm").modal("hide");
            } else {
                console.log("Error");
            }
        })
    });
});

function loadData() {
    $.get("/api/accounts/sales/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}


function addData(data) {
    destroyTable("#sales-data");
    table = $('#sales-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        booking = data[count];
        paid_amount = parseInt(booking.basic_cost)- parseInt(booking.remaning_cost);
        customer = booking.customer;
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm sales-edit" data-pk="' + booking.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm sales-delete" data-pk="' + booking.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([customer.full_name, parseInt(booking.plot_no), parseInt(booking.basic_cost), parseInt(booking.remaning_cost), parseInt(paid_amount), customer.email, customer.mobile, buttons]).draw(true);
    }
}