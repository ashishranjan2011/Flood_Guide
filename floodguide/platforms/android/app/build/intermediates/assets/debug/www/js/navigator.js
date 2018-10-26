
var req_no;
var name;
var no_of_person;
var no_of_severe_person;
var lat;
var lng;
var Name;
var saver_no;
var app = {
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    onDeviceReady: function() { 
        alert("hey");
       var query = window.location.search.substring(1);
       alert(query);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == "req_no"){req_no=pair[1];}
               if(pair[0] == "name"){name=pair[1];}
               if(pair[0] == "no_of_person"){no_of_person=pair[1];}
               if(pair[0] == "no_of_severe_person"){no_of_severe_person=pair[1];}
               if(pair[0] == "lat"){lat=pair[1];}
               if(pair[0] == "lng"){lng=pair[1];}
               if(pair[0] == "Name"){Name=pair[1];}
               if(pair[0] == "saver_no"){saver_no=pair[1];}
                      
       }
       alert(req_no);
       alert(name);
       //document.getElementById("display_location").innerHTML="Rescue next!";
       directions.navigateTo(Number(lat),Number(lng));
       $("#cancel").click(function() {
            $.ajax({
                    type:"PUT",  //Request type
                    url: "http://192.168.0.16:8000/users/"+String(req_no)+"/",   
                    data:{
                      "pickup" : 0,
                    },
                    cache:false,
                    success:function() {
                        alert("success for cancel");
                        var url="next.html?"+"Name="+String(Name)+"&saver_no="+String(saver_no);
                        window.location.href = url;
                    },
                    error:function(){
                        alert("error for cancel");
                        var url="next.html?"+"Name="+String(Name)+"&saver_no="+String(saver_no);
                        window.location.href = url;
                    }
                })
       })
       $("#end").click(function() {
            $.ajax({
                type:"DELETE",  //Request type
                url: "http://192.168.0.16:8000/delete/"+String(req_no)+"/",
                success:function(){
                    alert("success_delete");
                    var url="next.html?"+"Name="+String(Name)+"&saver_no="+String(saver_no);
                    window.location.href = url;    
                },
                error:function(){
                    alert("error_delete");
                    var url="next.html?"+"Name="+String(Name)+"&saver_no="+String(saver_no);
                    window.location.href = url;    
                }
            })
       })
    },
};

app.initialize();
