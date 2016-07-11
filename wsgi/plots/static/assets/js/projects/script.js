$(document).ready(function() {
    loadData();
    $(document).on('click', '.project-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#project-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/projects/" + id + "/", function(data, status) {
                $("#pk").val(data.pk);
                $("#name").val(data.name);
                $("#description").val(data.description);
                $("#village").val(data.village);
                $("#taluka").val(data.taluka);
                $("#district").val(data.district);
                $("#state").val(data.state);
                $("#address").val(data.address);
                $("#area").val(data.area);
                $("#plot_no").val(data.plot_no);
                $("#gat_no").val(data.gat_no);
                $("#survey_no").val(data.survey_no);
                $("#rate_per_sqft").val(data.rate_per_sqft);
                $("#start_date").val(data.start_date);
                $("#update-project").attr("data-pk", data.pk);
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });
    $(document).on('click', '#btn-add-project', function() {
        $("#project-form")[0].reset();
        $(".edit-label").hide();
        $(".add-label").show();
        $("#project-modal").modal("show");
    });


    $(document).on('click', '#update-project', function() {
        var form_data = $("#project-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.put("/api/projects/" + id + "/", form_data, function(data, status) {
                loadData();
                $("#project-modal").modal("hide");
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#add-project', function() {
        var form_data = $("#project-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.post("/api/projects/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#project-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

    $(document).on('click', '.project-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk",id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/projects/" + id + "/").done(function(data, textStatus, jqXHR) {
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
    $.get("/api/projects/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}


function addData(data) {
    destroyTable("#example");
    table = $('#example').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        project = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm project-edit" data-pk="' + project.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm project-delete" data-pk="' + project.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([project.name, project.description, project.area, project.address, project.plot_no, project.gat_no, buttons]).draw(true);
    }
}