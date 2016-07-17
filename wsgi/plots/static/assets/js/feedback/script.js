$(document).ready(function() {
    loadData();
    loadAllProjects();

    $(document).on('click', '.agent-delete', function() {
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
                $("#lbl-name").text(data.first_name+" "+data.middle_name+" "+data.last_name);
                $("#lbl-occupation").text(data.occupation);
                $("#lbl-dob").text(data.dob);
                $("#lbl-age").text(data.age);
                $("#lbl-marriage_anniversary").text(data.marriage_anniversary);
                $("#lbl-agriculture_status").text(data.agriculture_status);
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
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm agent-view" data-pk="' + feedback.id + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm agent-delete" data-pk="' + feedback.id + '"><i class="fa fa-trash"></i></a></div>';
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