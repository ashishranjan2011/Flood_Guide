
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var saver_no;
var Name;
var app = {
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    
    onDeviceReady: function() { 
        // alert("hey");
       var query = window.location.search.substring(1);
       // alert(query);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == "saver_no"){saver_no=pair[1];}
               if(pair[0] == "name"){Name=pair[1];}
       }

       $("button").click(function() {
            var URL="http://192.168.0.16:8000/users/"+String(saver_no);
            //alert("click");
            $.getJSON(URL).done( function(data) {
                var name=data["name"];
                var req_no=data["req_no"];
                var no_of_person = data["no_of_person"];
                var no_of_severe_person = data["no_of_severe_person"];
                var lat=data["lat"];
                var lng=data["lng"];
                var url="navigator.html?"+"name="+String(name)+"&req_no="+String(req_no)+"&no_of_person="+String(no_of_person)+"&no_of_severe_person="+String(no_of_severe_person)+"&lat="+String(lat)+"&lng="+String(lng)+"&Name="+String(Name)+"&saver_no="+String(saver_no);
                 //alert(url);
                window.location.href = url;
            }).fail(function() {
                alert("Error:Check your internet settings");
                // alert("failed");
            });

       })
    },
};

app.initialize();
