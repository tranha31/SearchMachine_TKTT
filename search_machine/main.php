<?php
use Elasticsearch\ClientBuilder;
require "vendor/autoload.php";
$hosts = [
    [
        'host'=>'localhost',
        'port'=>'9200',
        'scheme'=>'http',
        'user'=>'elastic',
        'pass'=>'admin1234'
    ]
];
$defaultHandler = ClientBuilder::defaultHandler();
$client = ClientBuilder::create()->setHosts($hosts)->setHandler($defaultHandler)->build();

if(isset($_GET['q'])){
    $q = $_GET['q'];
    $query = join(" ", explode('-', $_GET['q']));
}
else{
    $q = "";
    $query = "";
}

if(isset($_GET['page'])){
    $page = $_GET['page'];
}
else{
    $page = 1;
}

$start = ($page-1)*10;

$data = null;
$total_records = 0;
$total_pages = 0;
$time = 0;

if($query != ""){
    $params = [
        'index' => 'search_machine',
        'size' => 10,
        'from' => $start,
        'track_total_hits' => true, 
        'body' => [
            'query' => [
                'bool' => [
                    'should' => [
                        ['match' => ['title' => $query]],
                        ['match' => ['content' => $query]]
                    ]
                ]
            ],
            "highlight" => [
                "pre_tags" => ["<b>"],
                "post_tags" => ["</b>"],
                "fields" => [
                    "content" => new stdClass()
                ]
            ]
        ]
    ];

    $result = $client->search($params);

    $total_records = $result['hits']['total']['value'];
    $time = $result['took'];
    $time = $time / 1000;
    if($total_records > 0){
        $total_pages = ceil($total_records / 10);
        $data = $result['hits']['hits'];
    }

    
    
}

function maxString($string_arr): string{
    if(count($string_arr) > 3){
        return "...".$string_arr[0]."...".$string_arr[1]."...".$string_arr[2]."...";
    }
    else{
        $x = "...";
        foreach($string_arr as $s){
            $x = $x.$s."...";
        }
        return $x;
    }
}

?>
<!DOCTYPE HTML>
<html>
    <head>
        <title>Tìm kiếm thông tin</title>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="index.css"/>
        <link rel="stylesheet" href="main.css"/>
    </head>
    <body>
        <div id="main" class="container" page="<?php echo $page;?>">
            <div class="header">
                <img class="logo" src="logo.png"/>
                <div class="form" id="form">
                    <img style="top:unset" class="search-icon" src="search.png" >
                    <input id="content" type="text" value="<?php echo $query;?>" >
                </div>
            </div>
            <div class="content">
                <p>Có khoảng <?php echo $total_records; ?> kết quả (<?php echo $time; ?>s)</p>
                
                <?php
                if($data != null){
                    foreach($data as $d){
                        $date = $d['_source']['time'];
                        $url = $d['_source']['path'];
                        $title = $d['_source']['title'];
                        $high_light = $d['highlight']['content'];

                        $content = maxString($high_light);

                        ?>
                        <div class="news">
                            <a href=<?=$url?> target="_blank" class="url"><?=$url?></a>
                            <a href=<?=$url?> target="_blank" class="title"><?=$title?></a>
                            <p class="time"><?=$date?></p>
                            <p class="excerpt"><?=$content?></p>
                        </div>
                        <?php
                    }
                }
                ?>

            </div>

            <div class="navigation">
                <?php
                echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\" href='main.php?q=".$q."&page=1'>"."Trang đầu"."</a>";
                if($page <= 1){
                        echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href=#>Trước</a>";
                }
                else{
                    echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".($page-1)."'>"."Trước"."</a>";
                }

                if($total_pages <= 5){    
                    for($i=1; $i<=$total_pages; $i++){
                        echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".$i."'>".$i."</a>";
                    }

                }
                else{
                    if($page <= 3){
                        for($i=1; $i<=5; $i++){
                            echo "<a id=\"page-$i\" class=\"nav-btn\" style=\"margin-left:5px; margin-right:5px; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".$i."'>".$i."</a>";
                        }
                        echo "...";
                    }
                    else if($page > $total_pages-3){
                        echo "...";
                        for($i=$total_pages-4; $i<=$total_pages; $i++){
                            echo "<a id=\"page-$i\" class=\"nav-btn\" style=\"margin-left:5px; margin-right:5px; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".$i."'>".$i."</a>";
                        }
                    }
                    else{
                        echo "...";
                        for($i=$page-2; $i<=$page+2; $i++){
                            echo "<a id=\"page-$i\" class=\"nav-btn\" style=\"margin-left:5px; margin-right:5px; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".$i."'>".$i."</a>";
                        }
                        echo "...";
                    }
                }
                if($page >= $total_pages){
                        echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href=#>Sau</a>";
                }
                else{
                    echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".($page+1)."'>"."Sau"."</a>";
                }

                echo "<a style=\"margin-left:5px; margin-right:5px; display:block; position: relative; z-index:7;\"  href='main.php?q=".$q."&page=".$total_pages."'>"."Trang cuối"."</a>";

                ?>
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
        });
        var page = "page-" + main.getAttribute("page");
        var navBtn = document.querySelectorAll(".nav-btn");
        navBtn.forEach(e=>{
            if(e.id == page){
                e.classList.add("active");
            }
            else{
                e.classList.remove("active");
            }
        })
    </script>
</html>