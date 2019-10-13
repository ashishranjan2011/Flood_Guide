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
 var mylat,mylng;
var app = {
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                mylat = pos["lat"];
                mylng = pos["lng"];
            });
        }
        $("button").click(function() {
            var Name=document.getElementById("name").value;
            var count_tot=document.getElementById("totalperson").value;
            var count_vul=document.getElementById("vulnerable").value;
            // alert(count_tot);
            // alert(count_vul);
            // alert(mylat);
            // alert(mylng);
            var URL="http://mitnashu000.pythonanywhere.com/users/";
                
            $.ajax({
                    type:"POST",  //Request type
                    url: URL,   
                    data:{
                        "name": Name,
                        "lat": mylat,
                        "lng": mylng,
                        "no_of_person": count_tot,
                        "no_of_severe_person": count_vul,
                    },
                    cache:false,
                    success:function() {
                        window.location.href = "victim_success.html" ;
                    },
                    error:function(){
                        alert("Error: Check your network settings");
                    }
                })
        })        
    },
};

app.initialize();
































