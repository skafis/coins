$(document).ready(function() {
      //alert("aaaa");

 // AJAX POST
    $('.saveentryyear').click(function(){
      //alert('am i called' +$(".entry-year").val()+" : "+$(".current-year").is(":checked"));

        $.ajax({
            type: "POST",
            url: "/sysadmin/entryyear_create/",
            dataType: "json",
            data: { "entryyear": $(".entry-year").val(),"currentyear": $(".current-year").is(":checked"), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("entryyear-ajax-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.entryyear;
            }
        });
    });

	 // AJAX POST
    $('.saveclasses').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/classes_create/",
            dataType: "json",
            data: { "classes": $(".class-name").val(),"entryyear": $("#id_classesentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("classes-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.entryyear;
            }
        });
    });

	 // AJAX POST
    $('.savedormitory').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/dormitory_create/",
            dataType: "json",
            data: { "dormitory": $(".dormitory").val(),"entryyear": $("#id_dormitoryentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("dormitory-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.dormitory;
            }
        });
    });

	 // AJAX POST
    $('.savepaymentmethods').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());
        $.ajax({
            type: "POST",
            url: "/sysadmin/paymentmethods_create/",
            dataType: "json",
            data: { "paymentmethods": $(".paymentmethods").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("paymentmethods-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.paymentmethods;
            }
        });
    });

	 // AJAX POST
    $('.saveterms').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/terms_create/",
            dataType: "json",
            data: { "terms": $(".terms").val(),"entryyear": $("#id_termsentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("terms-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.terms;
            }
        });
    });

	 // AJAX POST
    $('.savestream').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/stream_create/",
            dataType: "json",
            data: { "stream": $(".stream").val(),"entryyear": $("#id_streamentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("stream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savesubject').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/subject_create/",
            dataType: "json",
            data: { "subject": $(".subject").val(),"subject_code": $(".subject_code").val(),"entryyear": $("#id_subjectentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("subject-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.subject;
            }
        });
    });

	 // AJAX POST
    $('.savepaper').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/paper_create/",
            dataType: "json",
            data: { "paper": $(".paper").val(),"paper_code": $(".paper_code").val(),"entryyear": $("#id_paperentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("paper-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.paper;
            }
        });
    });



// AJAX POST
    $('.savegender').click(function(){
      //alert(".............");

        $.ajax({
            type: "POST",
            url: "/sysadmin/gender_create/",
            dataType: "json",
            data: { "gender": $(".gender").val(),"entryyear": $("#id_genderentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("gender-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.gender;
            }
        });
    });

// AJAX POST
    $('.saveschgender').click(function(){
      //alert(".............");

        $.ajax({
            type: "POST",
            url: "/sch_portal/gender_create/",
            dataType: "json",
            data: { "gender": $("#id_gender :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schgender-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.gender;
            }
        });
    });

// AJAX POST
    $('.savecategory').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/category_create/",
            dataType: "json",
            data: { "category": $(".category").val(),"category_code": $(".category_code").val(),"entryyear": $("#id_categoryentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("category-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.category;
            }
        });
    });

// AJAX POST
    $('.savemonth').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/month_create/",
            dataType: "json",
            data: { "month": $(".month").val(),"month_code": $(".month_code").val(),"entryyear": $("#id_monthentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("month-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.month;
            }
        });
    });


// AJAX POST
    $('.savehouse').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/house_create/",
            dataType: "json",
            data: { "house": $(".house").val(),"house_code": $(".house_code").val(),"entryyear": $("#id_houseentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("house-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.house;
            }
        });
    });

// AJAX POST
    $('.saveschooltype').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/schooltype_create/",
            dataType: "json",
            data: { "schooltype": $(".schooltype").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schooltype-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.schooltype;
            }
        });
    });


// AJAX POST
    $('.savecategorytype').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/categorytype_create/",
            dataType: "json",
            data: { "categorytype": $(".categorytype").val(), "entryyear": $("#id_categorytypeentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("categorytype-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.categorytype;
            }
        });
    });

// AJAX POST
    $('.savecountry').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/country_create/",
            dataType: "json",
            data: { "country": $(".country").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("country-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.country;
            }
        });
    });

// AJAX POST
    $('.savecounty').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/county_create/",
            dataType: "json",
            data: { "countyname": $(".countyname").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("county-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.countyname;
            }
        });
    });

// AJAX POST
    $('.savevoteheads').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/voteheads_create/",
            dataType: "json",
            data: { "voteheads": $(".voteheads").val(), "entryyear": $("#id_voteheadsentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("voteheads-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.voteheads;
            }
        });
    });

		// AJAX POST
    $('.savegrades').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sysadmin/grades_create/",
            dataType: "json",
            data: { "grades": $(".grades").val(), "points": $(".points").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("grades-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.grades;
            }
        });
    });


		// AJAX POST
    $('.saveschoolname').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/sysadmin/school_create/",
            dataType: "json",
            data: { "schoolname": $(".school-name").val(), "schoolaccname": $(".school-acc-name").val(), "secschoolaccname": $(".sec-school-acc-name").val(), "schoolphone": $(".school-phone").val(), "schoolemail": $(".school-email").val() , "formone": $("#id_schformone :selected").val(),  "formtwo": $("#id_formtwo :selected").val(),  "formthree": $("#id_formthree :selected").val(),  "formfour": $("#id_formfour :selected").val(), "schoolstream": $("#id_fifthschoolstream :selected").val(), "secschoolstream": $("#id_secschoolstream :selected").val(), "thirdschoolstream": $("#id_thirdschoolstream :selected").val(), "fourthschoolstream": $("#id_fourthschoolstream :selected").val(), "schoolcounty": $("#id_schoolcounty :selected").val(),"schooldivision": $(".school-division").val(), "schoolconstituency": $(".school-constituency").val(), "schoollocation": $(".school-location").val(), "schoolsublocation": $(".school-sublocation").val(), "schooltown": $(".school-town").val() },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schools-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.schname;
            }
        });
    });

		// AJAX POST
    $('.savemerchantname').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/pos_portal/merchant_create/",
            dataType: "json",
            data: { "schoolprofiles": $("#id_schoolprofiles :selected").val(), "firstname": $(".merchant-firstname").val(), "secondname": $(".merchant-secondname").val(), "lastname": $(".merchant-lastname").val(), "phonenumber": $(".merchant-phonenumber").val(), "email": $(".merchant-email").val() , "posnumber": $(".pos-number").val(), "posaccountnumber": $(".pos-accountnumber").val(), "posserialnum": $(".pos-serialnum").val() },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schools-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.schname;
            }
        });
    });


		// AJAX POST
    $('.savepos').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/pos_portal/pos_create/",
            dataType: "json",
            data: { "posnumber": $(".pos-number").val(), "posaccountnumber": $(".pos-accountnumber").val(), "posserialnum": $(".pos-serialnum").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("pos-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.pos;
            }
        });
    });

		// AJAX POST
    $('.savestudentname').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/sch_portal/student_create/",
            dataType: "json",
            data: { "schoolname": $("#id_schoolprofiles :selected").val(),"admno": $(".student-admno").val(), "username": $(".student-username").val(), "firstname": $(".student-firstname").val(), "secondname": $(".student-secondname").val(), "lastname": $(".student-lastname").val() , "gender": $("#id_schgender :selected").val(),"currentclasses": $("#id_formone :selected").val(),"currentstream": $("#id_schoolstream :selected").val(), "dateofbirth": $(".student-dateofbirth").val(), "county": $("#id_studentcounty :selected").val(), "division": $(".student-division").val(), "constituency": $(".student-constituency").val(), "location": $(".student-location").val(), "sublocation": $(".student-sublocation").val(), "town": $(".student-town").val(), "accountnumber": $(".student-accountnumber").val(), "expirerydate": $(".student-expirerydate").val(), "dormitory": $("#id_schdormitory :selected").val() },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("student-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.schname;
            }
        });
    });

		// AJAX POST
    $('.saveschentryyear').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/sch_portal/entryyear_create/",
            dataType: "json",
            data: { "entryyear": $("#id_entryyear :selected").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schentryyear-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.pos;
            }
        });
    });


		// AJAX POST
    $('.saveschstaff').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/sysadmin/schstaff_create/",
            dataType: "json",
            data: { "schoolname": $("#id_schoolprofiles :selected").val(),"userdrpdwn": $("#id_userdrpdwn :selected").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstaff-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.pos;
            }
        });
    });


	 // AJAX POST
    $('.saveschclasses').click(function(){
      //alert('am i called' + $("#id_formone :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/classes_create/",
            dataType: "json",
            data: { "classes": $("#id_formone :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schclasses-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.entryyear;
            }
        });
    });

	 // AJAX POST
    $('.saveschstream').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/stream_create/",
            dataType: "json",
            data: { "stream": $("#id_schoolstream :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

		// AJAX POST
    $('.saveapplicant').click(function(){
      //alert('am i called' );

        $.ajax({
            type: "POST",
            url: "/sch_portal/yellowform_create/",
            dataType: "json",
            data: { "entryyear": $("#id_entryyear :selected").val(),"indexnumber": $(".applicant-indexnumber").val(), "firstname": $(".applicant-firstname").val(), "secondname": $(".applicant-secondname").val(), "lastname": $(".applicant-lastname").val(), "dateofbirth": $(".applicant-dateofbirth").val() , "gender": $("#id_yfgender2 :selected").val(), "birthcert": $(".applicant-birthcert").val(), "pupilsinclasseght": $(".applicant-pupilsinclasseght").val(), "lastposition": $(".applicant-lastposition").val(), "lastmarks": $(".applicant-lastmarks").val(), "cocurricularevents": $(".applicant-cocurricularevents").val(), "headmasterapproval": $(".applicant-headmasterapproval").val(), "dateofapproval": $(".applicant-dateofapproval").val(), "headmasterphone": $(".applicant-headmasterphone").val(), "fax": $(".applicant-fax").val(), "email": $(".applicant-email").val(), "parentfullnames": $(".applicant-parentfullnames").val(), "parentgender": $("#id_yfgender :selected").val(), "maritalstatus": $(".applicant-maritalstatus").val(), "parentdead": $(".applicant-parentdead").val(), "nationality": $(".applicant-nationality").val(), "nationalid": $(".applicant-nationalid").val(), "employment": $(".applicant-employment").val(), "inbusiness": $(".applicant-inbusiness").val(), "hasland": $(".applicant-hasland").val(), "otherincomeoptions": $(".applicant-otherincomeoptions").val(), "physicaladdress": $(".applicant-physicaladdress").val(), "listallsiblings": $(".applicant-listallsiblings").val(), "applicationinfo": $(".applicant-applicationinfo").val(), "cirtifydate": $(".applicant-cirtifydate").val(), "cirtifysigniture": $(".applicant-cirtifysigniture").val(), "cirtifyname": $(".applicant-cirtifyname").val(), "cirtifyoccupation": $(".applicant-cirtifyoccupation").val(), "cirtifyfax": $(".applicant-cirtifyfax").val(), "cirtifyphone": $(".applicant-cirtifyphone").val(), "cirtifyemail": $(".applicant-cirtifyemail").val(), "freefullnames": $(".applicant-freefullnames").val(), "freesignature": $(".applicant-freesignature").val(), "freephoneno": $(".applicant-freephoneno").val(), "recomenderfullnames": $(".applicant-recomenderfullnames").val(), "recomendersignature": $(".applicant-recomendersignature").val(), "recomenderoffice": $(".applicant-recomenderoffice").val(), "recomenderphoneno": $(".applicant-recomenderphoneno").val(), "kcpemath": $(".applicant-kcpemath").val(), "kcpeeng": $(".applicant-kcpeeng").val(), "kcpess": $(".applicant-kcpess").val(), "kcpekisw": $(".applicant-kcpekisw").val() , "kcpesci": $(".applicant-kcpesci").val(), "kcpetotal": $(".applicant-kcpetotal").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("student-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.schname;
            }
        });
    });


	 // AJAX POST
    $('.saveschdormitory').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/dormitory_create/",
            dataType: "json",
            data: { "dormitory": $("#id_dormitory :selected").val(),"entryyear": $("#id_dormitoryentryyear :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("dormitory-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.dormitory;
            }
        });
    });

	 // AJAX POST
    $('.savestudentsports').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/studentsports_create/",
            dataType: "json",
            data: { "sport": $(".student-sport").val(),"studentprofiles": $("#id_studentprofiles :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savestudentclubs').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/studentclubs_create/",
            dataType: "json",
            data: { "club": $(".student-club").val(),"studentprofiles": $("#id_studentprofiles :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savestudentholidayjobs').click(function(){
      //alert('am i called' + $(".class-name").val()+" : "+$("#id_entryyear :selected").val());

        $.ajax({
            type: "POST",
            url: "/sch_portal/holidayjobs_create/",
            dataType: "json",
            data: { "job": $(".student-job").val(),"studentprofiles": $("#id_studentprofiles :selected").val(), },
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savedisciplinecases').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/sch_portal/disciplinecases_create/",
            dataType: "json",
            data: { "blacklist": $(".student-blacklist").val(),"category": $(".student-category").val(),"blacklistdate": $(".student-blacklistdate").val(),"whitelist": $(".student-whitelist").val(),"whitelistdate": $(".student-whitelistdate").val(),"studentprofiles": $("#id_studentprofiles :selected").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });


	 // AJAX POST
    $('.savestudentsupplies').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/sch_portal/studentsupplies_create/",
            dataType: "json",
            data: { "category": $(".student-category").val(),"supply": $(".student-supplies").val(),"studentprofiles": $("#id_studentprofiles :selected").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savebooks').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/sch_portal/book_create/",
            dataType: "json",
            data: { "bookname": $("#id_bookname").val(),"author": $("#id_author").val(),"category": $("#id_category").val(),"boughtsponsored": $("#id_boughtsponsored").val(),"amount": $("#id_amount").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here");
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.getstudentaccno').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/bursar_portal/get_balance/",
            dataType: "json",
            data: { "walletname_name": $("#id_walletname_name :selected").val(),"studentprofiles": $("#id_studentprofiles :selected").val(),},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here "+data.balance);
								$("#display_balance").text(data.balance)
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.savedeposit').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/bursar_portal/do_deposits/",
            dataType: "json",
            data: { "walletname_name": $("#id_walletname_name :selected").val(),"studentprofiles": $("#id_studentprofiles :selected").val(),"amount": $("#id_amount").val()},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here "+data.balance);
								$("#display_balance").text(data.balance)
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });

	 // AJAX POST
    $('.activatedeactivatecard').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/bursar_portal/do_activatecard/",
            dataType: "json",
            data: { "walletname_name": $("#id_walletname_name :selected").val(),"studentprofiles": $("#id_studentprofiles :selected").val(),"is_locked": $(".id_is_locked").is(":checked")},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here "+data.balance);
								$("#display_balance").text(data.balance)
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });
	 // AJAX POST
    $('.savewithdraw').click(function(){
      //alert('am i called');
        $.ajax({
            type: "POST",
            url: "/bursar_portal/do_withdraw/",
            dataType: "json",
            data: { "studentprofiles": $("#id_studentprofiles :selected").val(),"amount": $("#id_amount").val()},
            success: function(data) {
								//toastr.success("here",'SUCCESS');
				        //alert("here "+data.balance);
								$("#display_balance").text(data.balance)
								var table = document.getElementById("schstream-ajax-data-table");
								var count = table.rows.length;
								var row = table.insertRow(parseInt(count)-1);
								var scheckboxes = row.insertCell(0);
								var id = row.insertCell(1);
								var name = row.insertCell(2);
								var checkbox = document.createElement('input');
								checkbox.type = "checkbox";
								checkbox.id = "scsch"+data[d]["id"];
								scheckboxes.appendChild(checkbox);
								var label = document.createElement('label');
								label.htmlFor = "id";
								label.appendChild(document.createTextNode(data[d]["id"]));
								id.appendChild(label);
								name.innerHTML = data.stream;
            }
        });
    });


    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 

});


