$(document).ready(function() {
    loadData();
    loadAllProjects();
    $(document).on('click', '.plot-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#plot-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/projects/plots/" + id + "/", function(data, status) {
                $("#pk").val(data.pk);
                $("#plot_no").val(data.plot_no);
                $("#basic_cost").val(data.basic_cost);
                $("#project").val(data.project);
                $("#facing").val(data.facing).change();
                $("#width").val(data.width);
                $("#breadth").val(data.breadth);
                $("#area").val(data.area);
                $("#start_date").val(data.start_date);
                $("#update-plot").attr("data-pk", data.pk);
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });
    $(document).on('click', '#btn-add-plot', function() {
        $("#plot-form")[0].reset();
        $(".edit-label").hide();
        $(".add-label").show();
        $("#plot-modal").modal("show");
    });


    $(document).on('click', '#update-plot', function() {
        var form_data = $("#plot-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.put("/api/projects/plots/" + id + "/", form_data, function(data, status) {
                loadData();
                $("#plot-modal").modal("hide");
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#add-plot', function() {
        var form_data = $("#plot-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.post("/api/projects/plots/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#plot-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

    $(document).on('click', '.plot-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk",id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/projects/plots/" + id + "/").done(function(data, textStatus, jqXHR) {
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
    $.get("/api/projects/plots/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}


function loadAllProjects() {
    $.get("/api/projects/for-plots/", function(data, status) {
            for (var count = 0; count < data.length; count++) {
                project = data[count];
                $("#project").append("<option value='"+project.pk+"'>"+project.project_name+"</option>");
            }
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}


function addData(data) {
    destroyTable("#plots-data");
    table = $('#plots-data').DataTable({
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