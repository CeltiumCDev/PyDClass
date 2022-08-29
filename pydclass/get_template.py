INDEX = """<!DOCTYPE html>
<html>
    <head>
        <title>Welcome - PyDClass</title>
        <meta charset="UTF-8"/>
        <meta http-equiv="refresh" content="5">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>

        <script>

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("myHeader");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
} 
        </script>
        <style>
             /* Style the header */
.header {
  padding: 10px 16px;
  background: #555;
  color: #f1f1f1;
}

/* Page content */
.content {
  padding: 16px;
}

/* The sticky class is added to the header with JS when it reaches its scroll position */
.sticky {
  position: fixed;
  top: 0;
  width: 100%
}

/* Add some top padding to the page content to prevent sudden quick movement (as the header gets a new position at the top of the page (position:fixed and top:0) */
.sticky + .content {
  padding-top: 102px;
} 
.content {
    text-align: center;
}

a {
    font-size: 10pt;
    color: black;
    text-decoration: none;
    font-family: Arial, Helvetica, sans-serif;

}
body {
    font-family: Arial, Helvetica, sans-serif;

}
h2 {
    color: orange;

}
#module_info {
    color: white;
    font-size: 15px;
    margin-left: 20px;
}
TR {
    margin: 100px;
}
        </style>

        
    </head>
    <body>
        <div class="header" id="myHeader">
            <h2>PyDClass <span id="module_info">Module loaded: {{module}}</span></h2>
        </div>
        <div class="content">
        
        <div id="svg" style="overflow:scroll">
        {{svg}}
        </div>
        <p>PyDClass is a fully opensource project.</p>
        </div>
    </body>
</html>"""
CHANGEMODULE = """<html lang="en">
    <head>
        <title>Change module - PyDClass</title>
        <meta charset="utf-8"/>
        <style>
            body {
                text-align: center;
                font-family: Arial, Helvetica, sans-serif;
            }
            input {
                border: 0;
                padding: 5px;
            }

            form {
                border: 1px solid black;
                display: inline-block;
            }
            .Input {
                width: 100px;
            }
        </style>
    </head>
    <body>
        <h2>Change module</h2>
        <p style="color: red"><b>Warning! </b>Not supported. Why? Beacause when you editing the new file, you don't look the new file but the old file. </p>
        <form method="GET" action="/module/form">
            <input id="Input" type="text" name="module" value="Not supported - That isn't an error" width="100" required="required" title="Not supported. Please go in our GitHub. "disabled/>
            <input type="submit" title="You can't send. Not supported. "disabled></input>
        </form>
    </body>
</html>"""
ERROR_404 = """<html>
    <head>
        <title>404 - PyDClass</title>
        <meta charset="utf-8"/>
        <script>


document.addEventListener("DOMContentLoaded",function(){
  
  var body=document.body;
   setInterval(createStar,100);
   function createStar(){
     var right=Math.random()*500;
     var top=Math.random()*screen.height;
     var star=document.createElement("div");
  star.classList.add("star")
   body.appendChild(star);
   setInterval(runStar,10);
     star.style.top=top+"px";
   function runStar(){
     if(right>=screen.width){
       star.remove();
     }
     right+=3;
     star.style.right=right+"px";
   }
   } 
 })
 
 
        </script>
        <style>
body{
  margin:0;
  padding:0;
  font-family: 'Tomorrow', sans-serif;
  height:100vh;
background-image: linear-gradient(to top, #2e1753, #1f1746, #131537, #0d1028, #050819);
  display:flex;
  justify-content:center;
  align-items:center;
  overflow:hidden;
}
.text{
  position:absolute;
  top:10%;
  color:#fff;
  text-align:center;
}
h1{
  font-size:50px;
}
.star{
  position:absolute;
  width:2px;
  height:2px;
  background:#fff;
  right:0;
  animation:starTwinkle 3s infinite linear;
}
.astronaut img{
  width:100px;
  position:absolute;
  top:55%;
  animation:astronautFly 6s infinite linear;
}
@keyframes astronautFly{
  0%{
    left:-100px;
  }
  25%{
    top:50%;
    transform:rotate(30deg);
  }
  50%{
    transform:rotate(45deg);
    top:55%;
  }
  75%{
    top:60%;
    transform:rotate(30deg);
  }
  100%{
    left:110%;
    transform:rotate(45deg);
  }
}
@keyframes starTwinkle{
  0%{
     background:rgba(255,255,255,0.4);
  }
  25%{
    background:rgba(255,255,255,0.8);
  }
  50%{
   background:rgba(255,255,255,1);
  }
  75%{
    background:rgba(255,255,255,0.8);
  }
  100%{
    background:rgba(255,255,255,0.4);
  }
}
        </style>
    </head>
    <body>


<!-- about -->
 <!-- end about -->
 
 

<div class="text">
    <div>ERROR</div>
    <h1>404</h1>
    <hr>
    <div>Page Not Found</div>
  </div>
  
  <div class="astronaut">
    <img src="https://images.vexels.com/media/users/3/152639/isolated/preview/506b575739e90613428cdb399175e2c8-space-astronaut-cartoon-by-vexels.png" alt="" class="src">
  </div>
  
  
 
 
    </body>
</html>"""

ERROR_500 = """<html>
    <head>
        <title>500 - PyDClass</title>
        <meta charset="utf-8"/>
        <script>


document.addEventListener("DOMContentLoaded",function(){
  
  var body=document.body;
   setInterval(createStar,100);
   function createStar(){
     var right=Math.random()*500;
     var top=Math.random()*screen.height;
     var star=document.createElement("div");
  star.classList.add("star")
   body.appendChild(star);
   setInterval(runStar,10);
     star.style.top=top+"px";
   function runStar(){
     if(right>=screen.width){
       star.remove();
     }
     right+=3;
     star.style.right=right+"px";
   }
   } 
 })
 
 
        </script>
        <style>
body{
  margin:0;
  padding:0;
  font-family: 'Tomorrow', sans-serif;
  height:100vh;
background-image: linear-gradient(to top, #2e1753, #1f1746, #131537, #0d1028, #050819);
  display:flex;
  justify-content:center;
  align-items:center;
  overflow:hidden;
}
.text{
  position:absolute;
  top:10%;
  color:#fff;
  text-align:center;
}
h1{
  font-size:50px;
}
.star{
  position:absolute;
  width:2px;
  height:2px;
  background:#fff;
  right:0;
  animation:starTwinkle 3s infinite linear;
}
.astronaut img{
  width:100px;
  position:absolute;
  top:55%;
  animation:astronautFly 6s infinite linear;
}
@keyframes astronautFly{
  0%{
    left:-100px;
  }
  25%{
    top:50%;
    transform:rotate(30deg);
  }
  50%{
    transform:rotate(45deg);
    top:55%;
  }
  75%{
    top:60%;
    transform:rotate(30deg);
  }
  100%{
    left:110%;
    transform:rotate(45deg);
  }
}
@keyframes starTwinkle{
  0%{
     background:rgba(255,255,255,0.4);
  }
  25%{
    background:rgba(255,255,255,0.8);
  }
  50%{
   background:rgba(255,255,255,1);
  }
  75%{
    background:rgba(255,255,255,0.8);
  }
  100%{
    background:rgba(255,255,255,0.4);
  }
}
a {
  text-decoration: none;
  color: white;
}
        </style>
    </head>
    <body>


<!-- about -->
 <!-- end about -->
 
 

<div class="text">
    <div>ERROR</div>
    <h1>500</h1>
    <hr>
    <div>It's the fault of the developers! It wasn't supposed to happen... <br> Please go on GitHub and report that. <br><a href="https://github.com/CeltiumCDev/PyDClass">Click here for go to our GitHub</a></div>
  </div>
  
  <div class="astronaut">
    <img src="https://images.vexels.com/media/users/3/152639/isolated/preview/506b575739e90613428cdb399175e2c8-space-astronaut-cartoon-by-vexels.png" alt="" class="src">
  </div>
  
  
 
 
    </body>
<<<<<<< HEAD
</html>"""

