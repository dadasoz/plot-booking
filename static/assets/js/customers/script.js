$(document).ready(function() {
    loadData();
    $(document).on('click', '.customer-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#customer-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/customers/" + id + "/", function(data, status) {
                $("#pk").val(data.pk);
                $("#plot_no").val(data.plot_no);
                $("#basic_cost").val(data.basic_cost);
                $("#project").val(data.project);
                $("#facing").val(data.facing).change();
                $("#width").val(data.width);
                $("#breadth").val(data.breadth);
                $("#area").val(data.area);
                $("#start_date").val(data.start_date);
                $("#update-customer").attr("data-pk", data.pk);
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


    $(document).on('click', '#customer-plot', function() {
        var form_data = $("#plot-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.put("/api/customers/" + id + "/", form_data, function(data, status) {
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
        $.post("/api/projects/plots/", form_data, function(data, textStatus) {
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
        $.delete("/api/customers/" + id + "/").done(function(data, textStatus, jqXHR) {
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
    $.get("/api/customers/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {
    destroyTable("#customers-data");
    table = $('#customers-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        plot = data[count];
        booking = plot.is_booked;
        sale = plot.is_saled;
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm plot-edit" data-pk="' + plot.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm plot-delete" data-pk="' + plot.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([plot.plot_no, plot.area, plot.basic_cost, plot.facing, plot.width, plot.breadth, plot.project_name, booking, sale, buttons]).draw(true);
    }
}