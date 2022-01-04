<!DOCTYPE html>
<html>
    <head>
        <title>Tìm kiếm thông tin</title>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="index.css"/>
    </head>
    <body>
        <div class="main" id="main">
            <img class="main-logo" src="logo.png">
            <div class="form">
                <img class="search-icon" src="search.png">
                <input id="content" class="search" type="text" placeholder="Nhập nội dung cần tìm kiếm">
                <p class="note">*Trang web tìm kiếm tin tức. Chỉ sử dụng trong phạm vi môn học Tìm kiếm thông tin</p>
            </div>
            
        </div>
    </body>
    <script>
        var main = document.getElementById("main");
        main.addEventListener("keypress", function(e){
            if(e.keyCode == 13){
                var input = document.getElementById("content");
                var query = input.value;
                if(query != "" && query != null){
                    query = query.split(' ').join('-');
                    document.location.assign('main.php?q='+query);
                }
            }
        })
    </script>
</html>