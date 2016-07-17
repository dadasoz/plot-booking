$(document).ready(function() {
    getSalesDetails();
    $(document).on('click', '#emi', function() {
        var checkbox = this;
        calculateLoanAmount();
        if($(checkbox).is(':checked')){
            $(".emi-div").show();
            $(".payments-div").show();
        }else{
            $(".emi-div").hide();
            $(".payments-div").hide();
        }
    });
});
function getSalesDetails(){
    sales_id = $("#sales_id").val();
    if(sales_id === ""){
        sales_id = getQuery("pk");
    }
    $.get("/api/accounts/sales/" + sales_id + "/", function(data, status) {
        customer = data.customer;
        booking = data.booking;
        $(".customer-name").text(customer.first_name+" "+customer.middle_name+" "+customer.last_name);
        $(".customer-mobile").text(customer.mobile);
        $(".customer-email").text(customer.email);
        $(".customer-address1").text(customer.address1);
        $(".customer-address2").text(customer.address2);
        $(".customer-pin_code").text(customer.pin_code);
        $(".customer-alternate_mobile").text(customer.alternate_mobile);
        $(".customer-occupation").text(customer.occupation);
        $(".customer-dob").text(customer.dob);
        $(".customer-age").text(customer.age);
        $(".customer-marriage_anniversary").text(customer.marriage_anniversary);
        $(".customer-nominee_name").text(customer.nominee_name);
        $(".customer-relation").text(customer.relation);
        if(customer.photo != null){
            $("#profile-image").attr("src",customer.photo);
        }

        plot = data.plot_no;

        $("#plot_no").val(plot.pk);
        $(".plot-project_name").text(plot.project_name);
        $(".plot-facing").text(plot.facing);
        $(".plot-area").text(plot.area);
        $(".plot-width").text(plot.width);
        $(".plot-breadth").text(plot.breadth);
        $(".plot-rate_per_sqft").text(plot.rate_per_sqft);
        $(".plot-survey_no").text(plot.survey_no);
        $(".plot-plot_no").text(plot.plot_no);

        $(".booking_date").text(booking.booking_date);
        $("#booking_id").val(booking.pk);
        $(".booking_amount").text(booking.booking_amount);

        printTransactions(data.sales_transactions)

        $("#sales_id").val(data.id);
        $(".is_emi_enabled").html(getTrueFalse(data.is_emi_enabled));
        $(".basic_cost").text(parseInt(data.basic_cost));
        $(".sales_cost").text(parseInt(data.sales_cost));
        $(".remaning_cost").text(parseInt(data.remaning_cost));

        $("#total_amount").val(parseInt(data.sales_cost));

        $("#booking_amount").val(booking.booking_amount);
        $("#booking_amount_method").val(booking.booking_amount_method).change();
        $("#booking_date").val(booking.booking_date);
        $("#booking_txn_no").val(booking.booking_txn_no);
        $("#down_payment").val(booking.down_payment);
        $("#down_payment_method").val(booking.down_payment_method).change();
        $("#down_payment_date").val(booking.down_payment_date);
        $("#down_payment_txn_no").val(booking.down_payment_txn_no);
        $("#loan_amount").val(data.loan_amount);
        $("#loan_amount_changed").val(data.loan_amount);


        if(data.is_emi_enabled){
            $(".emi-div").show();
            $(".payments-div").show();
            emi = data.emi_sale[0]
            if(emi != undefined){
                $("#emi_id").val(emi.id);
                $("#emi").prop('checked', true);
                $("#emi_terms").val(emi.duration).change();
                $("#emi_day").val(emi.emi_day);
                $("#emi_intrest").val(emi.intrest_rate);
                $("#loan_amount").val(parseInt(emi.total_amount));

                emi_installments = emi.emi_data;

                destroyTable("#payments-table");
                table = $('#payments-table').DataTable({
                    responsive: true,
                    dom: 'Bfrtip',
                    buttons: [
                        'print'
                    ]
                });

                for(var i=0; i<emi_installments.length; i++){
                    em = emi_installments[i]
                    emi_status = getTrueFalse(em.paid_status)
                    table.row.add([(i+1), em.emi_schedule_date, parseFloat(em.amount).toFixed(2), emi_status]).draw(true);
                }
            }

        }


    });
}

function printTransactions(transactions){
    destroyTable("#transaction-table");
    table = $('#transaction-table').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'print'
        ]
    });

    for(var i=0; i<transactions.length; i++){
        rxn = transactions[i]
        rxn_status = getTrueFalse(rxn.status)
        table.row.add([(i+1), rxn.created_at, parseFloat(rxn.amount).toFixed(2), rxn.source, rxn.trasaction_type, rxn.trasaction_type_no, rxn_status]).draw(true);
    }
}




$(document).on('click', '#update-button', function() {
    sales_id = $("#sales_id").val();
    if(sales_id === ""){
        sales_id = getQuery("pk");
    }
    calculateLoanAmount();
    booking_id = $("#booking_id").val();
    form_data = {
        'pk': booking_id,
        'plot_no': $("#plot_no").val(),
        'booking_date': $("#booking_date").val(),
        'booking_amount': $("#booking_amount").val(),
        'booking_date': $("#booking_date").val(),
        'booking_txn_no': $("#booking_txn_no").val(),
        'booking_amount_method': $("#booking_amount_method option:selected").val(),
        'down_payment': $("#down_payment").val(),
        'down_payment_date': $("#down_payment_date").val(),
        'down_payment_method': $("#down_payment_method option:selected").val(),
        'down_payment_txn_no': $("#down_payment_txn_no").val(),
    }
    $.patch("/api/booking/update/"+booking_id+"/", form_data, function(booking_data, status) {
        if (status === "success") {
            sale_details = {
                "pk": sales_id,
                'plot_no': $("#plot_no").val(), 
                'is_emi_enabled': $("#emi").is(':checked').toString(),
                'basic_cost': $("#total_amount").val(),
                'sales_cost': $("#total_amount").val(),
                'remaning_cost': $("#loan_amount").val(),
            }
            $.patch("/api/accounts/sales/update/"+sales_id+"/", sale_details, function(sales_data, status) {
                if (status === "success") {
                        if(sales_data.is_emi_enabled){
                            emi_id = $("#emi_id").val();
                            if(emi_id === ""){
                                loan_amount = parseInt($("#loan_amount").val());
                                total_amount = parseInt($("#total_amount").val());
                                paid_amount = total_amount - loan_amount;
                                emi_details = {
                                    "sale": sales_data.pk,
                                    'total_amount': $("#loan_amount").val(),
                                    'intrest_rate': $("#emi_intrest").val(),
                                    'paid_amount': paid_amount,
                                    'duration': $("#emi_terms option:selected").val(),
                                    'emi_day': $("#emi_day").val(), 
                                }
                                $.post("/api/accounts/emi/create/", emi_details, function(emi_data, textStatus) {
                                    if (emi_data.status == 201) {
                                        alert("Successfully updated!");
                                    }
                                });
                            }else{
                                loan_amount = parseInt($("#loan_amount").val());
                                total_amount = parseInt($("#total_amount").val());
                                paid_amount = total_amount - loan_amount;
                                emi_details = {
                                    "sale": sales_data.pk,
                                    'total_amount': $("#loan_amount").val(),
                                    'intrest_rate': $("#emi_intrest").val(),
                                    'paid_amount': paid_amount,
                                    'duration': $("#emi_terms option:selected").val(),
                                    'emi_day': $("#emi_day").val(), 
                                }
                                $.patch("/api/accounts/emi/update/"+emi_id+"/", emi_details, function(emi_data, status) {
                                    if (status === "success") {
                                        alert("Successfully updated!");
                                    }
                                });
                            }
                        }        

                    } else {
                        console.log("Error");
                    }
            });
        } else {
            console.log("Error");
        }
    });
});



$(document).on('click', '#calculate-emi', function() {
    calculateEMI();
});


function calculateLoanAmount(){
    booking_amount = getValById("booking_amount");
    down_payment = getValById("down_payment");
    total_amount = getValById("total_amount");

    paid_amount = booking_amount + down_payment;

    loan_amount = total_amount - paid_amount;

    $("#loan_amount").val(loan_amount);

    return loan_amount;

}


function calculateEMI(){

    loan_amount = calculateLoanAmount();  
 
    intrest_rate  = getValById("emi_intrest");

    emi_day  = getValById("emi_day");

    duration = parseInt($("#emi_terms option:selected").val());

    emi_amount =  getMonthlyEMI(loan_amount, intrest_rate, duration);

    printEMI(emi_amount, duration, emi_day);

}

function printEMI(emi, duration, emi_day){
    destroyTable("#payments-table");
    table = $('#payments-table').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'print'
        ]
    });
    var date = new Date();
    for(var i=1; i<=duration; i++){
        date.setDate(emi_day);
        date.setMonth(date.getMonth() + 1);
        table.row.add([i, date.toLocaleFormat('%d-%b-%Y'), emi.toFixed(2)]).draw(true);
    }
}


function getMonthlyEMI(principle_amount, intrest_rate, duration){

    intrest_rate   = intrest_rate / 1200;

    emi_amount = 0;

    if(intrest_rate == 0){
        emi_amount =  principle_amount / duration;
    }else{
        emi_amount =  principle_amount * intrest_rate / (1 - (Math.pow(1/(1 + intrest_rate), duration)));
    }
    return emi_amount
}

function getTrueFalse(status){
    if(status){
        status = '<label class="tbl-icon icon-true"><i class="fa fa-check" aria-hidden="true"></i></label>';
    }else{
        status = '<label class="tbl-icon icon-false"><i class="fa fa-times " aria-hidden="true"></i></label>';
    }
    return status;
}