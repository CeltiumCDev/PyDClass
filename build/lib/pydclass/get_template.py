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
        </style>

        
    </head>
    <body>
        <div class="header" id="myHeader">
            <h2>PyDClass <span id="module_info">Module loaded: {{module}}</span></h2>
        </div>
        <div class="content">
        
        <div id="svg">
        {{svg}}
        </div>
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