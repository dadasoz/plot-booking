$(document).ready(function() {
    getBesicSettings();
    getCommissionSettings();
});


function getBesicSettings() {
    $.get("/api/admin/besic/", function(data, status) {
            $("#company_name").val(data.company_name);
            $("#slogan").val(data.slogan);
            $("#founded").val(data.founded);
            $("#email").val(data.email);
            $("#phone").val(data.phone);
            $("#mobile").val(data.mobile);
            $("#website").val(data.website);
            $("#alternate_mobile").val(data.alternate_mobile);

            $("#address").val(data.address);
            $("#pin_code").val(data.pin_code);
            //$("#photo").val(data.photo);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

function getCommissionSettings() {
    $.get("/api/admin/commission/", function(data, status) {
            $("#company").val(data.company);
            $("#employee").val(data.employee);
            $("#agent").val(data.agent);
        },
        function(data, status, st) {
            console.log("error");
        }
    );
}

$(document).on('click', '#save-besic-settings', function() {
    var form_data = $("#basic-form").serializeArray().reduce(function(a, x) {
        a[x.name] = x.value;
        return a;
    }, {});

    $.patch("/api/admin/besic/update/", form_data, function(data, status) {
            alert("Updated successfully!");
        },
        function(data, status, st) {
            console.log("error");
        }
    );
});

$(document).on('click', '#save-commssion-settings', function() {
    var form_data = $("#commission-form").serializeArray().reduce(function(a, x) {
        a[x.name] = x.value;
        return a;
    }, {});

    $.patch("/api/admin/commission/update/", form_data, function(data, status) {
            alert("Updated successfully!");
        },
        function(data, status, st) {
            console.log("error");
        }
    );
});
