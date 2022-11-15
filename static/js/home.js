var str_srv_url = window.location.href;

//refresh handle
var g_instance_refresh_clock;

//timer function to update system info
function update_system_info()
{   
    
}

//show status error
function show_error(content)
{
    var statusCtl = document.getElementById('statusContentCtl');
    statusCtl.style.display = "block";
    var statusShow = document.getElementById('statusShowCtl');
    statusShow.innerHTML=content;
    
}


//hide status panel
function hide_error()
{
    var statusCtl = document.getElementById('statusContentCtl');
    statusCtl.style.display = "none";
}

//update system infromation of dashboard
function get_system_info()
{
    //query system information
    var http_request;
    if (window.XMLHttpRequest)
    {
        http_request=new XMLHttpRequest();
    }
    else
    {
        http_request=new ActiveXObject("Microsoft.XMLHTTP");
    }
    http_request.onreadystatechange=function()
    {
        if(http_request.readyState==4 && http_request.status==200)
        {
            //update ui
            var str_json = eval('(' + http_request.responseText + ')');
            var systemNameCtl = document.getElementById("systemNameCtl")
            systemNameCtl.innerHTML = str_json["info"]["systemName"]+"<span>("+ str_json["info"]["systemVersion"]+")</span>" 
               + "&nbsp;&nbsp;"+str_json["info"]["systemArch"][0]
            
            var pythonVersionCtl = document.getElementById("pythonVersionCtl");
            pythonVersionCtl.innerHTML = str_json["info"]["pythonVersion"];

            var cudnnVersionCtl = document.getElementById("cudnnVersionCtl");
            cudnnVersionCtl.innerHTML = str_json["info"]["cudnnVersion"];

            var cudaVersionCtl = document.getElementById("cudaVersionCtl");
            cudaVersionCtl.innerHTML = str_json["info"]["cudaVersion"];

            var paddleVersionCtl = document.getElementById("paddleVersionCtl");
            paddleVersionCtl.innerHTML = "PaddlePaddle:" + "&nbsp;&nbsp;" + str_json["info"]["paddleVersion"];

            // "Python Version:"+"&nbsp;&nbsp;"+

            //hide status panel
            hide_error();
        }
        else
        {
            show_error("get system information error, please check that the server is running normally");
        }
    }
    http_request.open("GET",str_srv_url + "system",true);
    http_request.send(null);

    // //start timer to update GPU status frequently
    // g_instance_refresh_clock = self.setInterval("update_system_info()",10000);
}