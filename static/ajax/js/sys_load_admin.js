$( window ).load(function() {
							//alert("yeeeh");
    		// AJAX GET for loading students list
        $.ajax({
            type: "GET",
						cache: false,
            url: "/sysadmin/syssettings/",
            success: function(data) {

								//alert("data.schools "+data.schools);
								/*ENTRY YEAR*/
								var table = document.getElementById("entryyear-ajax-table");
								for(d in data.entryyear){

										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										//var id = row.insertCell(1);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.entryyear[d]["id"];
										tdzero.appendChild(checkbox);
										//var label = document.createElement('label');`
										//label.htmlFor = "id";
										//label.appendChild(document.createTextNode(data.entryyear[d]["id"]));
										//id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/sysadmin/entryyear/"+data.entryyear[d]["id"]);
										link.text = data.entryyear[d]["entryyear"];
										tdone.innerHTML=data.entryyear[d]["entryyear"];
										var edit = document.createElement("a");
										edit.setAttribute("href", "/sysadmin/entryyear/"+data.entryyear[d]["id"]);
										edit.text = "Edit";
										edit.className += 'btn btn-action'; 
										tdtwo.appendChild(edit);
										var view = document.createElement("a");
										view.setAttribute("href", "/sysadmin/entryyear/"+data.entryyear[d]["id"]);
										view.text = "View";
										//view.addClass("btn btn-action"); 
										view.className += 'btn btn-action'; //note the space
										tdtwo.appendChild(view);
										var deletes = document.createElement("a");
										deletes.setAttribute("href", "/sysadmin/entryyear/"+data.entryyear[d]["id"]);
										deletes.text = "Delete";
										deletes.className += 'btn btn-action'; //note the space
										tdtwo.appendChild(deletes);
										//alert("data.entryyear ....."+data.entryyear[d]["entryyear"]);
								}

								/*CLASSES*/
								var table = document.getElementById("classes-ajax-data-table");
								for(d in data.classes){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.classes[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.classes[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.classes[d]["id"]);
										link.text = data.classes[d]["classes"];
										tdone.appendChild(link);
								}

								/*dormitory*/
								var table = document.getElementById("dormitory-ajax-data-table");
								for(d in data.dormitory){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.dormitory[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.dormitory[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.dormitory[d]["id"]);
										link.text = data.dormitory[d]["dormitory"];
										tdone.appendChild(link);
								}

								/*paymentmethods*/
								var table = document.getElementById("paymentmethods-ajax-data-table");
								for(d in data.paymentmethods){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.paymentmethods[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.paymentmethods[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.paymentmethods[d]["id"]);
										link.text = data.paymentmethods[d]["paymentmethods"];
										tdone.appendChild(link);
								}

								/*terms*/
								var table = document.getElementById("terms-ajax-data-table");
								for(d in data.terms){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.terms[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.terms[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.terms[d]["id"]);
										link.text = data.terms[d]["term"];
										tdone.appendChild(link);
								}

								/*stream*/
								var table = document.getElementById("stream-ajax-data-table");
								for(d in data.stream){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.stream[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.stream[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.stream[d]["id"]);
										link.text = data.stream[d]["stream"];
										tdone.appendChild(link);
								}

								/*subject*/
								var table = document.getElementById("subject-ajax-data-table");
								for(d in data.subject){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.subject[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.subject[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.subject[d]["id"]);
										link.text = data.subject[d]["subject"];
										tdone.appendChild(link);
								}

								/*paper*/
								var table = document.getElementById("paper-ajax-data-table");
								for(d in data.paper){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.paper[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.paper[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.paper[d]["id"]);
										link.text = data.paper[d]["paper"];
										tdone.appendChild(link);
								}

								/*gender*/
								var table = document.getElementById("gender-ajax-data-table");
								for(d in data.gender){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.gender[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.gender[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.gender[d]["id"]);
										link.text = data.gender[d]["gender"];
										tdone.appendChild(link);
								}

								/*category*/
								var table = document.getElementById("category-ajax-data-table");
								for(d in data.category){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.category[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.category[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.category[d]["id"]);
										link.text = data.category[d]["category"];
										tdone.appendChild(link);
								}

								/*month*/
								var table = document.getElementById("month-ajax-data-table");
								for(d in data.month){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.month[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.month[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.month[d]["id"]);
										link.text = data.month[d]["month"];
										tdone.appendChild(link);
								}

								/*house*/
								var table = document.getElementById("house-ajax-data-table");
								for(d in data.house){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.house[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.house[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.house[d]["id"]);
										link.text = data.house[d]["house"];
										tdone.appendChild(link);
								}

								/*schooltype*/
								var table = document.getElementById("schooltype-ajax-data-table");
								for(d in data.schooltype){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schooltype[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.schooltype[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.schooltype[d]["id"]);
										link.text = data.schooltype[d]["schooltype"];
										tdone.appendChild(link);
								}

								/*categorytype*/
								var table = document.getElementById("categorytype-ajax-data-table");
								for(d in data.categorytype){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.categorytype[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.categorytype[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.categorytype[d]["id"]);
										link.text = data.categorytype[d]["categorytype"];
										tdone.appendChild(link);
								}

								/*country*/
								var table = document.getElementById("country-ajax-data-table");
								for(d in data.country){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.country[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.country[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.country[d]["id"]);
										link.text = data.country[d]["country"];
										tdone.appendChild(link);
								}

								/*county*/
								var table = document.getElementById("county-ajax-data-table");
								for(d in data.county){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.county[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.county[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.county[d]["id"]);
										link.text = data.county[d]["countyname"];
										tdone.appendChild(link);
								}


								/*voteheads*/
								var table = document.getElementById("voteheads-ajax-data-table");
								for(d in data.voteheads){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.voteheads[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.voteheads[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.voteheads[d]["id"]);
										link.text = data.voteheads[d]["voteheads"];
										tdone.appendChild(link);
								}

								/*grades*/
								var table = document.getElementById("grades-ajax-data-table");
								for(d in data.grades){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.grades[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.grades[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.grades[d]["id"]);
										link.text = data.grades[d]["grades"];
										tdone.appendChild(link);
								}

								/*schools*/
								var table = document.getElementById("schools-ajax-data-table");
								for(d in data.schools){
										alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schools[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.schools[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.schools[d]["id"]);
										link.text = data.schools[d]["schname"];
										tdone.appendChild(link);
								}


								/*schoolstaff*/
								var table = document.getElementById("schstaff-ajax-data-table");

								for(d in data.schoolstaff){
										//alert("data.entryyear "+data.schoolstaff);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var tdtwo = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schoolstaff[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.schoolstaff[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.schoolstaff[d]["id"]);
										link.text = data.schoolstaff[d]["name__schname"];
										tdone.appendChild(link);
										tdtwo.innerHTML=data.schoolstaff[d]["owner__username"];
								}
        		}
			});

//alert("123.");
        $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/register/",
            success: function(data) {

								//alert("data.merchant ...."+data.schools);
								/*merchant*/
								var table = document.getElementById("sch_portal-ajax-data-table");
								for(d in data.schools){//'id','pos','name','firstname','firstname','lastname','phonenumber','email','username'
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schools[d]["id"];
										tdzero.appendChild(checkbox);
										tdone.innerHTML=data.schools[d]["schname"];
										var edit = document.createElement("a");
										edit.setAttribute("href", "/sysadmin/merchant/"+data.schools[d]["id"]);
										edit.text = "Edit";
										edit.className += 'btn btn-action'; 
										tdtwo.appendChild(edit);
										var view = document.createElement("a");
										view.setAttribute("href", "/sysadmin/merchant/"+data.schools[d]["id"]);
										view.text = "View";
										view.className += 'btn btn-action'; //note the space
										tdtwo.appendChild(view);
										var deletes = document.createElement("a");
										deletes.setAttribute("href", "/sysadmin/merchant/"+data.schools[d]["id"]);
										deletes.text = "Delete";
										deletes.className += 'btn btn-action';//note the space
										tdtwo.appendChild(deletes);
								}

								/*studentprofiles*/
								var table = document.getElementById("schstudent-ajax-data-table");
								for( d in  data.studentprofiles){
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studentprofiles[d]["admno"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studentprofiles[d]["name__schname"]));
										tdtwo.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studentprofiles[d]["admno"]);
										link.text = data.studentprofiles[d]["firstname"];
										tdone.appendChild(link);
										tdthree.innerHTML=data.studentprofiles[d]["username__username"];
										tdfour.innerHTML=data.studentprofiles[d]["firstname"];
										tdfive.innerHTML=data.studentprofiles[d]["secondname"];
										tdsix.innerHTML=data.studentprofiles[d]["lastname"];
										tdseven.innerHTML=data.studentprofiles[d]["gender__gender__gender"];
										tdeight.innerHTML=data.studentprofiles[d]["current_classes__classes__classes"];
										tdnine.innerHTML=data.studentprofiles[d]["current_stream__streams__stream"];
										tdten.innerHTML=data.studentprofiles[d]["accountnumber"];
										tdeleven.innerHTML=data.studentprofiles[d]["encryped_acc_no"];
								}

								/*studentprofiles*/
								var table = document.getElementById("yellowform-ajax-data-table");
								for( d in  data.yellowform){
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.yellowform[d]["admno"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.yellowform[d]["entryyear__entryyear"]));
										tdtwo.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.yellowform[d]["admno"]);
										link.text = data.yellowform[d]["firstname"];
										tdone.appendChild(link);
										tdthree.innerHTML=data.yellowform[d]["entryyear__entryyear"];
										tdfour.innerHTML=data.yellowform[d]["firstname"];
										tdfive.innerHTML=data.yellowform[d]["secondname"];
										tdsix.innerHTML=data.yellowform[d]["lastname"];
										tdseven.innerHTML=data.yellowform[d]["gender__gender__gender"];
								}

            }
			});

//alert("wewe");

        $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/merchant/",
            success: function(data) {

								//alert("data.merchant ...."+data.merchant);
								/*merchant*/
								var table = document.getElementById("posmerchant-ajax-data-table");
								for(d in data.merchants){//'id','pos','name','firstname','firstname','lastname','phonenumber','email','username'
										//alert("data.merchant ...."+data.merchant[d]["id"]);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.merchants[d]["merchant_id__id"];
										tdzero.appendChild(checkbox);
										tdone.innerHTML=data.merchants[d]["merchant_id__name__schname"];
										tdtwo.innerHTML=data.merchants[d]["merchant_id__firstname"]+" "+data.merchants[d]["merchant_id__secondname"]+" "+data.merchants[d]["merchant_id__lastname"];
										//tdthree.innerHTML=;
										//tdfour.innerHTML=;
										tdthree.innerHTML=data.merchants[d]["merchant_id__phonenumber"];
										tdfive.innerHTML=data.merchants[d]["merchant_id__email"];
										tdsix.innerHTML=data.merchants[d]["merchant_id__balance"];
										tdseven.innerHTML=data.merchants[d]["accountnumber"];
										var edit = document.createElement("a");
										edit.setAttribute("href", "/sysadmin/merchant/"+data.merchants[d]["id"]);
										edit.text = "Edit";
										edit.className += 'btn btn-action'; 
										tdeight.appendChild(edit);
										var view = document.createElement("a");
										view.setAttribute("href", "/sysadmin/merchant/"+data.merchants[d]["id"]);
										view.text = "View";
										view.className += 'btn btn-action'; //note the space
										tdeight.appendChild(view);
										var deletes = document.createElement("a");
										deletes.setAttribute("href", "#"+data.merchants[d]["id"]);
										deletes.text = "Delete";
										deletes.className += 'btn btn-action'; //note the space
										tdeight.appendChild(deletes);
								}

        		}
			});

        $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/pos/",
            success: function(data) {

								//alert("data.merchant ...."+data.pos);
								/*pos*/
								/*var table = document.getElementById("pos-ajax-data-table");
								for(d in data.pos){
										//alert("data.entryyear "+data.pos);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.pos[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										tdone.innerHTML=data.pos[d]["posnumber"];
										tdtwo.innerHTML=data.pos[d]["accountnumber"];
										tdthree.innerHTML=data.pos[d]["serialnum"];
										tdfour.innerHTML=data.pos[d]["merchant_id__name__schname"];
										tdfive.innerHTML=data.pos[d]["merchant_id__firstname"];
										tdsix.innerHTML=data.pos[d]["balance"];
										tdsix.innerHTML=data.pos[d]["reverse"];
										tdsix.innerHTML="Stats";
								}*/


								var table = document.getElementById("pos-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										//var tdthirteen = row.insertCell(13);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.transactions[d]["id"];
										tdzero.innerHTML = data.transactions[d]["id"];//.appendChild(checkbox);
										tdone.innerHTML=data.transactions[d]["terminal__posnumber"];
										tdtwo.innerHTML=data.transactions[d]["terminal__accountnumber"];
										tdthree.innerHTML=data.transactions[d]["terminal__serialnum"];
										tdfour.innerHTML=data.transactions[d]["location_id__schname"];
										tdfive.innerHTML=data.transactions[d]["terminal_id__merchant_id__firstname"];
										tdsix.innerHTML=data.transactions[d]["balance"];
										tdseven.innerHTML=data.transactions[d]["reverse"];
										tdeight.innerHTML="Stats";
										if(data.transactions[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactions[d]["amount"])
										}else if(data.transactions[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactions[d]["amount"])
										}
								}
								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(0);

								// Add some bold text in the new cell:
								cell.innerHTML = "<strong>Total</strong>";
								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(1);

								// Add some bold text in the new cell:
								cell.innerHTML = total;
        		}
			});

        $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/pos_by_schools/",
            success: function(data) {

								var table = document.getElementById("posbyschools-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var a = document.createElement('a');
										var linkText = document.createTextNode(data.transactions[d]["location_id__schname"]);
										a.appendChild(linkText);
										a.title = data.transactions[d]["location_id__schname"];
										a.href = "/pos_portal/pos_by_posname/"+data.transactions[d]["location"];
										tdzero.appendChild(a);
										tdone.innerHTML=data.transactions[d]["wallet_id__studentprofiles_id__accountnumber"];
										tdtwo.innerHTML=data.transactions[d]["amount"];
										tdthree.innerHTML=data.transactions[d]["trace_no"];
										tdfour.innerHTML=data.transactions[d]["ref_no"];
										tdfive.innerHTML=data.transactions[d]["location"];
										tdsix.innerHTML=data.transactions[d]["terminal_id__posnumber"];
										tdseven.innerHTML=data.transactions[d]["terminal_id__accountnumber"];
										tdeight.innerHTML=data.transactions[d]["terminal_id__merchant_id__firstname"];
										tdnine.innerHTML=data.transactions[d]["transaction_type"];
										tdten.innerHTML=data.transactions[d]["reverse"];
										if(data.transactions[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactions[d]["amount"])
										}else if(data.transactions[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactions[d]["amount"])
										}
								}
								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(0);

								// Add some bold text in the new cell:
								cell.innerHTML = "<strong>Total</strong>";
								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(1);

								// Add some bold text in the new cell:
								cell.innerHTML = total;
        		}
			});

				var currurl = window.location.href;
				var temp = currurl.substring(0,currurl.lastIndexOf("/"));
				var pk = temp.substring(temp.lastIndexOf("/")+1, temp.length);

				//alert("res");

        $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/pos_by_posname/"+pk,
            success: function(data) {

								var table = document.getElementById("posbyposname-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
								//alert("nnnn");
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										//var tdthirteen = row.insertCell(13);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.transactions[d]["id"];
										tdzero.innerHTML = data.transactions[d]["id"];//.appendChild(checkbox);
										tdone.innerHTML=data.transactions[d]["wallet_id__studentprofiles_id__accountnumber"];
										tdtwo.innerHTML=data.transactions[d]["amount"];
										tdthree.innerHTML=data.transactions[d]["trace_no"];
										tdfour.innerHTML=data.transactions[d]["ref_no"];
										tdfive.innerHTML=data.transactions[d]["location"];
										tdsix.innerHTML=data.transactions[d]["terminal_id__posnumber"];
										tdseven.innerHTML=data.transactions[d]["terminal_id__accountnumber"];
										tdeight.innerHTML=data.transactions[d]["terminal_id__merchant_id__firstname"];
										tdnine.innerHTML=data.transactions[d]["location_id__schname"];
										tdten.innerHTML=data.transactions[d]["transaction_type"];
										tdeleven.innerHTML=data.transactions[d]["reverse"];
										if(data.transactions[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactions[d]["amount"])
										}else if(data.transactions[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactions[d]["amount"])
										}
								}
								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(0);

								// Add some bold text in the new cell:
								cell.innerHTML = "<strong>Total</strong>";
								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(1);

								// Add some bold text in the new cell:
								cell.innerHTML = total;
								//alert("mmmm");
        		}
			});


        /*$.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/pos_by_schools/",
            success: function(data) {

								var table = document.getElementById("posbyschools-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										tdzero.innerHTML = data.transactions[d]["id"];
										tdone.innerHTML=data.transactions[d]["wallet_id__studentprofiles_id__accountnumber"];
										tdtwo.innerHTML=data.transactions[d]["amount"];
										tdthree.innerHTML=data.transactions[d]["trace_no"];
										tdfour.innerHTML=data.transactions[d]["ref_no"];
										tdfive.innerHTML=data.transactions[d]["location"];
										tdsix.innerHTML=data.transactions[d]["terminal_id__posnumber"];
										tdseven.innerHTML=data.transactions[d]["terminal_id__accountnumber"];
										tdeight.innerHTML=data.transactions[d]["terminal_id__merchant_id__firstname"];
										tdnine.innerHTML=data.transactions[d]["location_id__schname"];
										tdten.innerHTML=data.transactions[d]["transaction_type"];
										tdeleven.innerHTML=data.transactions[d]["reverse"];
										if(data.transactions[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactions[d]["amount"])
										}else if(data.transactions[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactions[d]["amount"])
										}
								}
								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(0);

								// Add some bold text in the new cell:
								cell.innerHTML = "<strong>Total</strong>";
								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(1);

								// Add some bold text in the new cell:
								cell.innerHTML = total;
        		}
			});*/

    		// AJAX GET for loading school systemsettings
        $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/syssettings/",
            success: function(data) {
								//alert(",,,");
								/*gender*/
								var table = document.getElementById("schgender-ajax-data-table");
								for(d in data.gender){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.gender[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.gender[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.gender[d]["id"]);
										link.text = data.gender[d]["gender__gender"];
										tdone.appendChild(link);
								}

							
								/*schstream*/
								var table = document.getElementById("schstream-ajax-data-table");
								for(d in data.schstream){
										//alert("data.entryyear ");
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schstream[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.schstream[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.schstream[d]["id"]);
										link.text = data.schstream[d]["streams__stream"];
										tdone.appendChild(link);
								}

								//alert("data.schclasses "+data.schclasses);

								/*schclasses*/
								var table = document.getElementById("schclasses-ajax-data-table");
								for( d in  data.schclasses){
										//alert("data.schclasses "+data.schclasses[d]["classes__classes"]);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schclasses[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.schclasses[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.schclasses[d]["id"]);
										link.text = data.schclasses[d]["classes__classes"];
										tdone.appendChild(link);
								}

								//alert("data.schools "+data.schools);
								/*ENTRY YEAR*/
								var table = document.getElementById("schentryyear-ajax-table");
								for(d in data.schentryyear){

										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										//var id = row.insertCell(1);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.schentryyear[d]["id"];
										tdzero.appendChild(checkbox);
										//var label = document.createElement('label');`
										//label.htmlFor = "id";
										//label.appendChild(document.createTextNode(data.entryyear[d]["id"]));
										//id.appendChild(label);
										//var link = document.createElement("a");
										//link.setAttribute("href", "/sysadmin/entryyear/"+data.schentryyear[d]["id"]);
										//link.text = data.schentryyear[d]["entryyear"];
										tdone.innerHTML=data.schentryyear[d]["entryyear__entryyear"];
										var edit = document.createElement("a");
										edit.setAttribute("href", "/sysadmin/entryyear/"+data.schentryyear[d]["id"]);
										edit.text = "Edit";
										edit.className += 'btn btn-action'; 
										tdtwo.appendChild(edit);
										var view = document.createElement("a");
										view.setAttribute("href", "/sysadmin/entryyear/"+data.schentryyear[d]["id"]);
										view.text = "View";
										//view.addClass("btn btn-action"); 
										view.className += 'btn btn-action'; //note the space
										tdtwo.appendChild(view);
										var deletes = document.createElement("a");
										deletes.setAttribute("href", "/sysadmin/entryyear/"+data.schentryyear[d]["id"]);
										deletes.text = "Delete";
										deletes.className += 'btn btn-action'; //note the space
										tdtwo.appendChild(deletes);
										//alert("data.entryyear ....."+data.entryyear[d]["entryyear"]);
								}

								/*dormitory*/
								var table = document.getElementById("schdormitory-ajax-data-table");
								for(d in data.dormitory){
										//alert("data.entryyear "+data.entryyear.d);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.dormitory[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.dormitory[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.dormitory[d]["id"]);
										link.text = data.dormitory[d]["dormitory__dormitory"];
										tdone.appendChild(link);
								}

        		}
			});


        $.ajax({
            type: "GET",
						cache: false,
            url: "/sysadmin/student/",
            success: function(data) {
								//alert('here');
								/*studentprofiles*/
								var table = document.getElementById("sysadminstudent-ajax-data-table");
								for( d in  data.studentprofiles){
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studentprofiles[d]["admno"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studentprofiles[d]["name__schname"]));
										tdtwo.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studentprofiles[d]["admno"]);
										link.text = data.studentprofiles[d]["firstname"];
										tdone.appendChild(link);
										tdthree.innerHTML=data.studentprofiles[d]["username__username"];
										tdfour.innerHTML=data.studentprofiles[d]["firstname"];
										tdfive.innerHTML=data.studentprofiles[d]["secondname"];
										tdsix.innerHTML=data.studentprofiles[d]["lastname"];
										tdseven.innerHTML=data.studentprofiles[d]["gender__gender__gender"];
										tdeight.innerHTML=data.studentprofiles[d]["current_classes__classes__classes"];
										tdnine.innerHTML=data.studentprofiles[d]["current_stream__streams__stream"];
										tdten.innerHTML=data.studentprofiles[d]["accountnumber"];
										tdeleven.innerHTML=data.studentprofiles[d]["encryped_acc_no"];
								}

        		}
			});
										//alert("wallan");
        $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/pos_transactions/",
            success: function(data) {

							//alert("data.transactions ....");
								/*transactions*/
								var table = document.getElementById("postransactions-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.transactions[d]["id"];
										tdzero.innerHTML = data.transactions[d]["id"];//.appendChild(checkbox);
										tdone.innerHTML=data.transactions[d]["transaction_type"];
										tdtwo.innerHTML=data.transactions[d]["amount"];
										tdthree.innerHTML=data.transactions[d]["trace_no"];
										tdfour.innerHTML=data.transactions[d]["ref_no"];
										tdfive.innerHTML=data.transactions[d]["currency"];
										tdsix.innerHTML=data.transactions[d]["location"];
										tdseven.innerHTML=data.transactions[d]["terminal_id__posnumber"];
										tdeight.innerHTML=data.transactions[d]["studentaccounts_id__studentprofiles_id__admno"];
										tdnine.innerHTML=data.transactions[d]["wallet_id__walletname_name"];
										;
								}

        		}
			});

        $.ajax({
            type: "GET",
						cache: false,
            url: "/ecoins_portal/",
            success: function(data) {

								var table = document.getElementById("ecoins_portalposbyschools-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactions){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										//var tdnine = row.insertCell(9);
										//var tdten = row.insertCell(10);
										var a = document.createElement('a');
										var linkText = document.createTextNode(data.transactions[d]["location_id__schname"]);
										a.appendChild(linkText);
										a.title = data.transactions[d]["location_id__schname"];
										a.href = "/ecoins_portal/pos_by_posname/"+data.transactions[d]["location"];
										tdzero.appendChild(a);
										tdone.innerHTML=data.transactions[d]["wallet_id__studentprofiles_id__accountnumber"];
										tdtwo.innerHTML=data.transactions[d]["amount"];
										tdthree.innerHTML=data.transactions[d]["trace_no"];
										tdfour.innerHTML=data.transactions[d]["location"];
										tdfive.innerHTML=data.transactions[d]["terminal_id__posnumber"];
										tdsix.innerHTML=data.transactions[d]["terminal_id__accountnumber"];
										tdseven.innerHTML=data.transactions[d]["transaction_type"];
										tdeight.innerHTML=data.transactions[d]["reverse"];
										//tdnine.innerHTML=data.transactions[d]["reverse"];
										//tdten.innerHTML=data.transactions[d]["reverse"];
										if(data.transactions[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactions[d]["amount"])
										}else if(data.transactions[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactions[d]["amount"])
										}
								}
								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(0);

								// Add some bold text in the new cell:
								cell.innerHTML = "<strong>Total</strong>";
								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var cell = row.insertCell(1);

								// Add some bold text in the new cell:
								cell.innerHTML = total;

								/*POS LIST DISPLAY*/
								var table = document.getElementById("transactionspos-ajax-data-table");
								var tbody = table.appendChild(document.createElement('tbody'))
								var total=0;
								for(d in data.transactionspos){//'transaction_type','amount','trace_no','ref_no','currency','location','terminal_id','studentaccounts_id','wallet_id
										var count = tbody.rows.length;
										var row = tbody.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										//var tdthirteen = row.insertCell(13);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.transactionspos[d]["id"];
										tdzero.innerHTML = data.transactionspos[d]["id"];//.appendChild(checkbox);
										tdone.innerHTML=data.transactionspos[d]["terminal__posnumber"];
										tdtwo.innerHTML=data.transactionspos[d]["terminal__accountnumber"];
										tdthree.innerHTML=data.transactionspos[d]["terminal__serialnum"];
										tdfour.innerHTML=data.transactionspos[d]["location_id__schname"];
										tdfive.innerHTML=data.transactionspos[d]["terminal_id__merchant_id__firstname"];
										tdsix.innerHTML=data.transactionspos[d]["balance"];
										tdseven.innerHTML=data.transactionspos[d]["reverse"];
										tdeight.innerHTML="Stats";
										if(data.transactionspos[d]["transaction_type"]=="Withdraw"){
												total=total-parseInt(data.transactionspos[d]["amount"])
										}else if(data.transactionspos[d]["transaction_type"]=="Deposit"){
												total=total+parseInt(data.transactionspos[d]["amount"])
										}
								}

								/*MERCHANT LIST DISPLAY*/
								var table = document.getElementById("posmerchantecoinsportal-ajax-data-table");
								for(d in data.posmerchantecoinsportal){//'id','pos','name','firstname','firstname','lastname','phonenumber','email','username'
										//alert("data.merchant ...."+data.merchant[d]["id"]);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										//var tdeight = row.insertCell(8);
										//var tdnine = row.insertCell(9);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.posmerchantecoinsportal[d]["id"];
										tdzero.appendChild(checkbox);
										tdone.innerHTML=data.posmerchantecoinsportal[d]["name__schname"];
										tdtwo.innerHTML=data.posmerchantecoinsportal[d]["firstname"];
										tdthree.innerHTML=data.posmerchantecoinsportal[d]["secondname"];
										tdfour.innerHTML=data.posmerchantecoinsportal[d]["lastname"];
										tdfive.innerHTML=data.posmerchantecoinsportal[d]["phonenumber"];
										tdsix.innerHTML=data.posmerchantecoinsportal[d]["email"];
										tdseven.innerHTML=data.posmerchantecoinsportal[d]["username__username"];
										//tdeight.innerHTML=data.posmerchantecoinsportal[d]["username__username"];
										var edit = document.createElement("a");
										edit.setAttribute("href", "/sysadmin/merchant/"+data.posmerchantecoinsportal[d]["id"]);
										edit.text = "Edit";
										edit.className += 'btn btn-action'; 
										//tdnine.appendChild(edit);
										var view = document.createElement("a");
										view.setAttribute("href", "/sysadmin/merchant/"+data.posmerchantecoinsportal[d]["id"]);
										view.text = "View";
										view.className += 'btn btn-action'; //note the space
										//tdnine.appendChild(view);
										var deletes = document.createElement("a");
										deletes.setAttribute("href", "#"+data.posmerchantecoinsportal[d]["id"]);
										deletes.text = "Delete";
										deletes.className += 'btn btn-action'; //note the space
										//tdnine.appendChild(deletes);
								}

								/*schools*/
								var table = document.getElementById("ecoins_portalschools-ajax-data-table");
								for(d in data.ecoins_portalschools){
										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.ecoins_portalschools[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.ecoins_portalschools[d]["id"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.ecoins_portalschools[d]["id"]);
										link.text = data.ecoins_portalschools[d]["schname"];
										tdone.appendChild(link);

								}

								//alert("yeh");
								var table = document.getElementById("ecoins_portalstudentprofiles-ajax-data-table");
								for( d in  data.ecoins_portalstudentprofiles){
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.ecoins_portalstudentprofiles[d]["admno"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.ecoins_portalstudentprofiles[d]["admno"]));
										tdtwo.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.ecoins_portalstudentprofiles[d]["admno"]);
										link.text = data.ecoins_portalstudentprofiles[d]["name__schname"];
										tdone.appendChild(link);
										tdthree.innerHTML=data.ecoins_portalstudentprofiles[d]["username__username"];
										tdfour.innerHTML=data.ecoins_portalstudentprofiles[d]["firstname"];
										tdfive.innerHTML=data.ecoins_portalstudentprofiles[d]["secondname"];
										tdsix.innerHTML=data.ecoins_portalstudentprofiles[d]["lastname"];
										tdseven.innerHTML=data.ecoins_portalstudentprofiles[d]["gender__gender__gender"];
										tdeight.innerHTML=data.ecoins_portalstudentprofiles[d]["current_classes__classes__classes"];
										tdnine.innerHTML=data.ecoins_portalstudentprofiles[d]["current_stream__streams__stream"];
										tdten.innerHTML=data.ecoins_portalstudentprofiles[d]["accountnumber"];
										tdeleven.innerHTML=data.ecoins_portalstudentprofiles[d]["encryped_acc_no"];
								}

        		}
			});


       $.ajax({
            type: "GET",
						cache: false,
            url: "/pos_portal/student/",
            success: function(data) {
								//alert('data '+data[0][0]);//[0]['fields'][0]);
								tdfourtotal=0;tdfivetotal=0;tdsixtotal=0;tdseventotal=0;tdeighttotal=0;tdninetotal=0;tdtentotal=0;tdeleventotal=0;
								var table = document.getElementById("studs-ajax-data-table");
								for( d in  data.studenttransactions){
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var tdone = row.insertCell(1);
										var tdtwo = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var tdnine = row.insertCell(9);
										var tdten = row.insertCell(10);
										var tdeleven = row.insertCell(11);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studenttransactions[d]["admno"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studenttransactions[d]["wallet_id__studentprofiles_id__firstname"]+" "+data.studenttransactions[d]["wallet_id__studentprofiles_id__secondname"]+" "+data.studenttransactions[d]["wallet_id__studentprofiles_id__lastname"]));
										tdtwo.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studenttransactions[d]["admno"]);
										link.text = data.studenttransactions[d]["wallet_id__studentprofiles_id__name__schname"];
										tdone.appendChild(link);
										tdthree.innerHTML=data.studenttransactions[d]["wallet_id__studentprofiles_id__encryped_acc_no"];
										if(data.studenttransactions[d]["wallet_id__walletname_name"]=="Pocket Money"){
											if(data.studenttransactions[d]["transaction_type"]=="Deposit"){
												tdfour.innerHTML=data.studenttransactions[d]["amount"];
												tdfourtotal=tdfourtotal+parseInt(data.studenttransactions[d]["amount"])
												tdfive.innerHTML=0;
												tdsix.innerHTML=0;
												tdseven.innerHTML=0;
												tdeight.innerHTML=0;
												tdnine.innerHTML=0;
												tdten.innerHTML=0;
												tdeleven.innerHTML=0;
											}else if(data.studenttransactions[d]["transaction_type"]=="Withdraw"){
												tdfive.innerHTML=data.studenttransactions[d]["amount"];
												tdfivetotal=tdfivetotal+parseInt(data.studenttransactions[d]["amount"])
												tdfour.innerHTML=0;
												tdsix.innerHTML=0;
												tdseven.innerHTML=0;
												tdeight.innerHTML=0;
												tdnine.innerHTML=0;
												tdten.innerHTML=0;
												tdeleven.innerHTML=0;
											}
												tdsix.innerHTML=data.studenttransactions[d]["balance"];
												tdsixtotal=tdsixtotal+parseInt(data.studenttransactions[d]["balance"])
										}else if(data.studenttransactions[d]["wallet_id__walletname_name"]=="School Fees"){
											if(data.studenttransactions[d]["transaction_type"]=="Deposit"){
												tdseven.innerHTML=data.studenttransactions[d]["amount"];
												tdseventotal=tdseventotal+parseInt(data.studenttransactions[d]["amount"])
												tdfour.innerHTML=0;
												tdsix.innerHTML=0;
												tdfive.innerHTML=0;
												tdeight.innerHTML=0;
												tdnine.innerHTML=0;
												tdten.innerHTML=0;
												tdeleven.innerHTML=0;
											}else if(data.studenttransactions[d]["transaction_type"]=="Withdraw"){
												tdeight.innerHTML=data.studenttransactions[d]["amount"];
												tdeighttotal=tdeighttotal+parseInt(data.studenttransactions[d]["amount"])
												tdfour.innerHTML=0;
												tdsix.innerHTML=0;
												tdfive.innerHTML=0;
												tdseven.innerHTML=0;
												tdnine.innerHTML=0;
												tdten.innerHTML=0;
												tdeleven.innerHTML=0;
											}
											tdnine.innerHTML=data.studenttransactions[d]["balance"];
											tdninetotal=tdninetotal+parseInt(data.studenttransactions[d]["balance"])
										}else if(data.studenttransactions[d]["wallet_id__walletname_name"]=="Savings"){
											if(data.studenttransactions[d]["transaction_type"]=="Deposit"){
												tdten.innerHTML=data.studenttransactions[d]["amount"];
												tdtentotal=tdtentotal+parseInt(data.studenttransactions[d]["amount"])
												tdfour.innerHTML=0;
												tdsix.innerHTML=0;
												tdfive.innerHTML=0;
												tdseven.innerHTML=0;
												tdeight.innerHTML=0;
												tdnine.innerHTML=0;
												tdeleven.innerHTML=0;
											}else if(data.studenttransactions[d]["transaction_type"]=="Withdraw"){
												tdeleven.innerHTML=data.studenttransactions[d]["amount"];
												tdeleventotal=tdeleventotal+parseInt(data.studenttransactions[d]["amount"])
												tdfour.innerHTML=0;
												tdsix.innerHTML=0;
												tdfive.innerHTML=0;
												tdseven.innerHTML=0;
												tdeight.innerHTML=0;
												tdnine.innerHTML=0;
												tdten.innerHTML=0;
											}
											tdeleven.innerHTML=data.studenttransactions[d]["balance"];
											tdeleventotal=tdeleventotal+parseInt(data.studenttransactions[d]["balance"])
										}
								}

								// Create an empty <tfoot> element and add it to the table:
								var footer = table.createTFoot();

								// Create an empty <tr> element and add it to the first position of <tfoot>:
								var row = footer.insertRow(0);     

								// Insert a new cell (<td>) at the first position of the "new" <tr> element:
								var tdzero = row.insertCell(0);
								var tdone = row.insertCell(1);
								var tdtwo = row.insertCell(2);
								var tdthree = row.insertCell(3);
								var tdfour = row.insertCell(4);
								var tdfive = row.insertCell(5);
								var tdsix = row.insertCell(6);
								var tdseven = row.insertCell(7);
								var tdeight = row.insertCell(8);
								var tdnine = row.insertCell(9);
								var tdten = row.insertCell(10);
								var tdeleven = row.insertCell(11);

								// Add some bold text in the new cell:
								tdzero.innerHTML = "<strong>Total</strong>";

								// Add some bold text in the new cell:
								tdfour.innerHTML = "<strong>"+tdfourtotal+"</strong>";
								tdfive.innerHTML = "<strong>"+tdfivetotal+"</strong>";
								tdsix.innerHTML = "<strong>"+tdsixtotal+"</strong>";
								tdseven.innerHTML = "<strong>"+tdseventotal+"</strong>";
								tdeight.innerHTML = "<strong>"+tdeighttotal+"</strong>";
								tdnine.innerHTML = "<strong>"+tdninetotal+"</strong>";
								tdten.innerHTML = "<strong>"+tdtentotal+"</strong>";
								tdeleven.innerHTML = "<strong>"+tdeleventotal+"</strong>";
        		}
			});
//alert("aaa");

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sysadmin/school/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("sysadminsch-ajax-data-table");
								for(d in data.sysadminsch){

										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var tdthree = row.insertCell(3);
										var tdfour = row.insertCell(4);
										var tdfive = row.insertCell(5);
										var tdsix = row.insertCell(6);
										var tdseven = row.insertCell(7);
										var tdeight = row.insertCell(8);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.sysadminsch[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.sysadminsch[d]["schname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.sysadminsch[d]["id"]);
										link.text = data.sysadminsch[d]["location"];
										tdone.appendChild(link);
										tdthree.innerHTML = data.sysadminsch[d]["encryped_acc_no"];
										tdfour.innerHTML = data.sysadminsch[d]["noofmerchants"];
										tdfive.innerHTML = data.sysadminsch[d]["schfeesbalance"];
										tdsix.innerHTML = data.sysadminsch[d]["pocketmoneybalance"];
										tdseven.innerHTML = data.sysadminsch[d]["savingsbalance"];
										tdeight.innerHTML = data.sysadminsch[d]["phonenumber"];
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/studentsports/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("studentsports-ajax-data-table");
								for(d in data.studentsports){

										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studentsports[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studentsports[d]["studentprofiles__admno"]+" "+data.studentsports[d]["studentprofiles__firstname"]+" "+data.studentsports[d]["studentprofiles__secondname"]+" "+data.studentsports[d]["studentprofiles__lastname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studentsports[d]["id"]);
										link.text = data.studentsports[d]["sport"];
										tdone.appendChild(link);
									
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/studentclubs/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("studentclubs-ajax-data-table");
								for(d in data.studentclubs){

										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studentclubs[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studentclubs[d]["studentprofiles__admno"]+" "+data.studentclubs[d]["studentprofiles__firstname"]+" "+data.studentclubs[d]["studentprofiles__secondname"]+" "+data.studentclubs[d]["studentprofiles__lastname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studentclubs[d]["id"]);
										link.text = data.studentclubs[d]["club"];
										tdone.appendChild(link);
									
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/holidayjobs/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("holidayjobs-ajax-data-table");
								for(d in data.holidayjobs){

										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.holidayjobs[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.holidayjobs[d]["studentprofiles__admno"]+" "+data.holidayjobs[d]["studentprofiles__firstname"]+" "+data.holidayjobs[d]["studentprofiles__secondname"]+" "+data.holidayjobs[d]["studentprofiles__lastname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.holidayjobs[d]["id"]);
										link.text = data.holidayjobs[d]["job"];
										tdone.appendChild(link);
									
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/discipline/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("disciplinecases-ajax-data-table");
								for(d in data.disciplinecases){

										//alert("data.entryyear "+data.schools);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var tdtwo = row.insertCell(3);
										var tdthree = row.insertCell(4);
										var tdfour = row.insertCell(5);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.disciplinecases[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.disciplinecases[d]["studentprofiles__admno"]+" "+data.disciplinecases[d]["studentprofiles__firstname"]+" "+data.disciplinecases[d]["studentprofiles__secondname"]+" "+data.disciplinecases[d]["studentprofiles__lastname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.disciplinecases[d]["id"]);
										link.text = data.disciplinecases[d]["job"];
										tdone.innerHTML=data.disciplinecases[d]["blacklist"];
										tdtwo.innerHTML=data.disciplinecases[d]["blacklistdate"];
										tdthree.innerHTML=data.disciplinecases[d]["whitelist"];
										tdfour.innerHTML=data.disciplinecases[d]["whitelistdate"];
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/studentsupplies/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("studentsupplies-ajax-data-table");
								for(d in data.studentsupplies){

										//alert("data.studentsupplies "+data.studentsupplies);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var tdtwo = row.insertCell(3);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.studentsupplies[d]["id"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.studentsupplies[d]["studentprofiles__admno"]+" "+data.studentsupplies[d]["studentprofiles__firstname"]+" "+data.studentsupplies[d]["studentprofiles__secondname"]+" "+data.studentsupplies[d]["studentprofiles__lastname"]));
										id.appendChild(label);
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.studentsupplies[d]["id"]);
										link.text = data.studentsupplies[d]["supply"];
										tdone.appendChild(label);
										tdtwo.innerHTML = data.studentsupplies[d]["category"];
										//alert("data.entryyear ");
								}
        		}
			});

       $.ajax({
            type: "GET",
						cache: false,
            url: "/sch_portal/books/",
            success: function(data) {
								/*schools*/
								var table = document.getElementById("books-ajax-data-table");
								for(d in data.books){

										//alert("data.books "+data.books);
										var count = table.rows.length;
										var row = table.insertRow(parseInt(count));
										var tdzero = row.insertCell(0);
										var id = row.insertCell(1);
										var tdone = row.insertCell(2);
										var tdtwo = row.insertCell(3);
										var tdthree = row.insertCell(4);
										var tdfour = row.insertCell(5);
										var checkbox = document.createElement('input');
										checkbox.type = "checkbox";
										checkbox.id = "scsch"+data.books[d]["bookname"];
										tdzero.appendChild(checkbox);
										var label = document.createElement('label');
										label.htmlFor = "id";
										label.appendChild(document.createTextNode(data.books[d]["bookname"]));
										id.appendChild(label);
										id.innerHTML = data.books[d]["bookname"];
										var link = document.createElement("a");
										link.setAttribute("href", "/pos_portal/pos_transactions/"+data.books[d]["id"]);
										link.text = data.books[d]["author"];
										tdone.appendChild(link);
										tdtwo.innerHTML = data.books[d]["category"];
										tdthree.innerHTML = data.books[d]["boughtsponsored"];
										tdfour.innerHTML = data.books[d]["amount"];
										//alert("data.entryyear ");
								}
        		}
			});
//alert("end");
});
