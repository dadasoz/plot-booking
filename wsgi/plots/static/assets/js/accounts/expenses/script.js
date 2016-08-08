$(document).ready(function() {
    loadData();

    $(document).on('click', '.exp-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk",id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/feedback/delete/" + id + "/").done(function(data, textStatus, jqXHR) {
            if (jqXHR.status == 204) {
                loadData();
                $("#delete-confirm").modal("hide");
            } else {
                console.log("Error");
            }
        })
    });


    $(document).on('click', '.exp-view', function() {
        id = $(this).attr("data-pk");
        $("#feedback-details-modal").modal("show");
        $.get("/api/accounts/expenses/" + id + "/", function(data, status) {
                $("#lbl-name").text(data.name);
                $("#lbl-email").text(data.email);
                $("#lbl-mobile").text(data.mobile);
                $("#lbl-message").text(data.message);
                $("#lbl-created_at").text(data.created_at);
                $("#lbl-project").text(data.project);
        });
    });

    $(document).on('click', '#btn-add-exp', function() {
        $("#exp-form")[0].reset();
        $("#exp-modal").modal("show");
    });

    $(document).on('click', '#add-exp', function() {
        var form_data = $("#exp-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.post("/api/feedback/create/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#exp-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

});

function loadData() {
    $.get("/api/accounts/expenses/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {

    destroyTable("#exp-data");
    table = $('#exp-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        exp = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm exp-view" data-pk="' + exp.id + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm exp-delete" data-pk="' + exp.id + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([exp.project, exp.name, exp.email, exp.mobile, exp.message, buttons]).draw(true);
    }
}
