$(document).ready(function() {
    loadData();
    $(document).on('click', '.customer-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#customer-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/customers/" + id + "/", function(data, status) {
                $("#pk").val(data.id);
                $("#first_name").val(data.first_name);
                $("#middle_name").val(data.middle_name);
                $("#last_name").val(data.last_name);
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
                $("#photo").val(data.photo);

                $("#nominee_name").val(data.nominee_name);
                $("#nominee_address").val(data.nominee_address);
                $("#nominee_email").val(data.nominee_email);
                $("#nominee_mobile").val(data.nominee_mobile);
                $("#nominee_alternate_mobile").val(data.nominee_alternate_mobile);
                $("#nominee_photo").val(data.nominee_photo);
                $("#nominee_dob").val(data.nominee_dob);
                $("#nominee_age").val(data.nominee_age);
                $("#nominee_occupation").val(data.nominee_occupation);
                $("#relation").val(data.relation);

                $("#update-customer").attr("data-pk", data.id);
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });
    $(document).on('click', '#btn-add-customer', function() {
        $("#customer-form")[0].reset();
        $(".edit-label").hide();
        $(".add-label").show();
        $("#customer-modal").modal("show");
    });


    $(document).on('click', '#update-customer', function() {
        var form_data = $("#customer-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.patch("/api/customers/update/" + id + "/", form_data, function(data, status) {
                loadData();
                $("#customer-modal").modal("hide");
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#add-customer', function() {
        var form_data = $("#customer-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.post("/api/customers/create/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#customer-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

    $(document).on('click', '.customer-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk",id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/customers/delete/" + id + "/").done(function(data, textStatus, jqXHR) {
            if (jqXHR.status == 204) {
                loadData();
                $("#delete-confirm").modal("hide");
            } else {
                console.log("Error");
            }
        })
    });


    $(document).on('click', '.customer-view', function() {
        id = $(this).attr("data-pk");
        $("#customer-details-modal").modal("show");
        $.get("/api/customers/" + id + "/", function(data, status) {
                $("#lbl-name").text(data.first_name+" "+data.middle_name+" "+data.last_name);
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

                $("#lbl-nominee_name").text(data.nominee_name);
                $("#lbl-nominee_address").text(data.nominee_address);
                $("#lbl-nominee_email").text(data.nominee_email);
                $("#lbl-nominee_mobile").text(data.nominee_mobile);
                $("#lbl-nominee_alternate_mobile").text(data.nominee_alternate_mobile);
                //$("#lbl-nominee_photo").val(data.nominee_photo);
                $("#lbl-nominee_dob").text(data.nominee_dob);
                $("#lbl-nominee_age").text(data.nominee_age);
                $("#lbl-nominee_occupation").text(data.nominee_occupation);
                $("#lbl-relation").text(data.relation);
        });
    });


});

function loadData() {
    $.get("/api/customers/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {

    destroyTable("#customer-data");
    table = $('#customer-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        customer = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-view" data-pk="' + customer.pk + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-edit" data-pk="' + customer.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm customer-delete" data-pk="' + customer.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([customer.full_name, customer.email, customer.mobile, customer.alternate_mobile, customer.address1, buttons]).draw(true);
    }
}