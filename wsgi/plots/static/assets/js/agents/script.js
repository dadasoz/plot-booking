$(document).ready(function() {
    loadData();
    $(document).on('click', '.agent-edit', function() {
        $(".edit-label").show();
        $(".add-label").hide();
        $("#agent-modal").modal("show");
        var id = $(this).attr("data-pk");
        $.get("/api/agents/" + id + "/", function(data, status) {
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
                //$("#photo").val(data.photo);

                $("#update-agent").attr("data-pk", data.id);
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });
    $(document).on('click', '#btn-add-agent', function() {
        $("#agent-form")[0].reset();
        $(".edit-label").hide();
        $(".add-label").show();
        $("#agent-modal").modal("show");

    });


    $(document).on('click', '#update-agent', function() {
        var form_data = $("#agent-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        id = $(this).attr("data-pk");
        $.patch("/api/agents/update/" + id + "/", form_data, function(data, status) {
                loadData();
                $("#agent-modal").modal("hide");
            },
            function(data, status, st) {
                console.log("error");
            }
        );
    });

    $(document).on('click', '#add-agent', function() {
        var form_data = $("#agent-form").serializeArray().reduce(function(a, x) {
            a[x.name] = x.value;
            return a;
        }, {});
        $.post("/api/agents/create/", form_data, function(data, textStatus) {
            if (data.status == 201) {
                loadData();
                $("#agents-modal").modal("hide");
            } else {
                console.log("Error");
            }
        });
    });

    $(document).on('click', '.agent-delete', function() {
        id = $(this).attr("data-pk");
        $("#delete-confirm").modal("show");
        $("#delete-record").attr("data-pk",id);
    });

    $(document).on('click', '#delete-record', function() {
        id = $(this).attr("data-pk");
        $.delete("/api/agents/delete/" + id + "/").done(function(data, textStatus, jqXHR) {
            if (jqXHR.status == 204) {
                loadData();
                $("#delete-confirm").modal("hide");
            } else {
                console.log("Error");
            }
        })
    });


    $(document).on('click', '.agent-view', function() {
        id = $(this).attr("data-pk");
        $("#agent-details-modal").modal("show");
        $.get("/api/agents/" + id + "/", function(data, status) {
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

        });
    });


});

function loadData() {
    $.get("/api/agents/", function(data, status) {
            addData(data);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function addData(data) {

    destroyTable("#agent-data");
    table = $('#agent-data').DataTable({
        responsive: true,
    });
    for (var count = 0; count < data.length; count++) {
        agent = data[count];
        buttons = '<div class="table-buttons">';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm agent-view" data-pk="' + agent.pk + '"><i class="fa fa-eye"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm agent-edit" data-pk="' + agent.pk + '"><i class="fa fa-edit"></i></a>';
        buttons += '<a class="btn btn-info btn-icon btn-circle btn-sm agent-delete" data-pk="' + agent.pk + '"><i class="fa fa-trash"></i></a></div>';
        table.row.add([agent.full_name, agent.email, agent.mobile, agent.alternate_mobile, agent.address1, buttons]).draw(true);
    }
}