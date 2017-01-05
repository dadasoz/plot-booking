$(document).ready(function() {
    loadData();
    loadAllProjects();

    $(document).on('click', '.feedback-delete', function() {
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


    $(document).on('click', '.feedback-view', function() {
        id = $(this).attr("data-pk");
        $("#feedback-details-modal").modal("show");
        $.get("/api/feedback/" + id + "/", function(data, status) {
                $("#lbl-name").text(data.name);
                $("#lbl-email").text(data.email);
                $("#lbl-mobile").text(data.mobile);
                $("#lbl-message").text(data.message);
                $("#lbl-created_at").text(data.created_at);
                $("#lbl-project").text(data.project);
        });
    });

    $(document).on('click', '#btn-add-feedback', function() {
        $("#feedback-form")[0].reset();
        $("#feedback-modal").modal("show");
    });

    $(document).on('click', '#add-feedback', function() {
        var form_data = $("#feedback-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.post("/api/feedback/create/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#feedback-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

});

function loadData() {
    $.get("/api/feedback/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {

    destroyTable("#feedback-data");
    table = $('#feedback-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        feedback = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm feedback-view" data-pk="' + feedback.id + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm feedback-delete" data-pk="' + feedback.id + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([feedback.project, feedback.name, feedback.email, feedback.mobile, feedback.message, buttons]).draw(true);
    }
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