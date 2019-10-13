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

    onDeviceReady: function() {
        // alert("saver ka pehla page is READY");
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
        var id,name;
        $("#1").click(function() {
            name=document.getElementById("name").value;
            $.ajax({
                type:"POST",  //Request type
                url: "http://mitnashu000.pythonanywhere.com/saver/",   
                data:{
                    "name": name,
                    "lat": mylat,
                    "lng": mylng,
                },
                cache:false,
                success:function(result) {
                    id=result["saver_no"];
                    var url="next.html"+"?"+"saver_no="+String(id)+"&name="+String(name);
                    window.location.href = url;
                },
                error:function(){
                    alert("Error: Check your internet settings");
                }
            })
        })

        
/*        var URL="http://192.168.0.16:8000/users/";
        $.getJSON(URL).done( function(data) {
                for(var x in data){
                    var stlat=x["lat"];
                    var stlng=x["lng"];
                    var timeurl = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + String(mylat) + "," + String(mylng) + "&destinations=" + String(stlat) + "," + String(stlng) + "&key=AIzaSyDPqTSybe-1GK--Pw4F3Dxhnd0Prd1p-ig";
                    $.getJSON(timeurl).done(function(data1){
                        dist=Number(data1["rows"][0]["elements"][0]["duration"]["value"]);
                    }).fail(function(){

                    });
                }
                var temp=data[0]["lat"];
                    alert(temp);

            }).fail(function() {
                cordova.plugins.notification.local.schedule({
                            title: 'Network Connection Problem',
                            text: 'Contact your service provider',
                            foreground: true
                });
            });
*/
            // $.ajax({
            //         type:"PUT",  //Request type
            //         url: "http://192.168.0.16:8000/saver/1/",   
            //         data:{
            //             "name": "ash",
            //             "lat": "87",
            //             "lng": "98",
            //             "is_free": 1,
            //             "next_destination": "",
            //             "saver_no": 1,
            //         },
            //         cache:false,
            //         success:function() {
            //             alert("success");
            //         },
            //         error:function(){
            //             alert("error");
            //         }
            //     })
        /*var temp;
        var URL="http://192.168.0.16:8000/users/";
            $.getJSON(URL).done( function(data) {
                    temp=data[0]["req_no"];
                    var nam=data[0]["name"];
                    alert(temp+" name");
            }).fail(function() {
                cordova.plugins.notification.local.schedule({
                            title: 'Network Connection Problem',
                            text: 'Contact your service provider',
                            foreground: true
                });
            });*/
        /*$.ajax({
                type:"DELETE",  //Request type
                url: "http://192.168.0.16:8000/deletesaver/1/",
                success:function(){
                    alert("success_saver");
                },
                error:function(){
                    alert("error_saver");
                }
            })    */   
    },
};

app.initialize();
