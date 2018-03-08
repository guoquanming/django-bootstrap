window.onload=function(){
	$(".navbar-nav>li>a").hover(function(){
		//alert("dsd");
		$(this).css("background","rgb(148, 148, 148)").css("color","rgb(255, 136, 0)");
	},function(){
		$(this).css("background","rgb(180, 180, 180)").css("color","white");
	});
	$(".dropdown-menu>li>a").hover(function(){
		//alert("dsd");
		$(this).css("background","rgb(148, 148, 148)").css("color","white");
	},function(){
		$(this).css("background","rgb(165, 165, 165)");
	});
	
	$(".pagination > li > a").hover(function(){
		$(this).css("font-weight","bold").css("color","white").css("background","rgb(255, 136, 0)");
	},function(){
		$(this).css("color","#000").css("background","white").css("font-weight","normal");
	});
	
	//----------------------------------------------------------------------------------------------------
	
	var rating = (function(){	
		//点亮
			var lightOn = function($item,num){
				var numInt = parseInt(num);
				if(numInt<num){
					$item.each(function(index){
					if(index<numInt){
						$(this).css("background-position","0-31px");	
					}
					else if(index == numInt){
						$(this).css("background-position","0-62px");
					}		
					else if(index > numInt){
						$(this).css("background-position","0 0");
					}});	
				}else{
					$item.each(function(index){
					if(index<num){
						$(this).css("background-position","0-31px");	
					}		
					else{
						$(this).css("background-position","0 0");
					}});
				}			
			};	
		var init = function(el,num,el1){
			var $rating = $(el);
			$item=$rating.find(el1);						
			//初始化
			lightOn($item,num);
		};
		return {
			init:init
		};	
	})();
	rating.init("#rating",$("#totaleval .score").text(),".rating-item");
	//--------------------------------------------------------------------------------------------------
	var rating1 = (function(){	
		//点亮
			var lightOn = function($item,num){
				var numInt = parseInt(num);
				if(numInt<num){
					$item.each(function(index){
					if(index<numInt){
						$(this).css("background-position","0-17px");	
					}
					else if(index == numInt){
						$(this).css("background-position","0-36px");
					}		
					else if(index > numInt){
						$(this).css("background-position","0 0");
					}});	
				}else{
					$item.each(function(index){
					if(index<num){
						$(this).css("background-position","0-17px");	
					}		
					else{
						$(this).css("background-position","0 0");
					}});
				}			
			};	
		var init = function(el,num,el1){
			var $rating = $(el);
			$item=$rating.find(el1);						
			//初始化
			lightOn($item,num);
			//事件绑定
		};
		return {
			init:init
		};	
	})();
	//正式和后台接触可以用for循环来进行动态添加
	rating1.init("#rating1",$(".totaleval2-1-3").text(),".rating-item1");
	rating1.init("#rating2",$(".totaleval2-2-3").text(),".rating-item2");
	rating1.init("#rating3",$(".totaleval2-3-3").text(),".rating-item3");
	rating1.init(".ratingall",$(".hiddeneva").val(),".rating-itemall");
	//线性增长class=ratingall的id
	$(".ratingall").each(function(index,value){
		$(this).attr("id","ratingall"+index);
	});
	$(".hiddeneva").each(function(index,value){
		rating1.init("#ratingall"+index,value.value,".rating-itemall");
	});
	$("#row3-8-6>a").on("click",function(){
		//alert($(".ratingall").length);
		if($(".ratingall").length>3){
			$("#row3-8-6").css("height","900px");
		}else{
			alert("多于三条评论才会展开");
		}		
	});

	//------------------------------------------百度地图代码---------------------------------------------------------
	//创建和初始化地图函数：
    function initMap(){
      createMap();//创建地图
      setMapEvent();//设置地图事件
      addMapControl();//向地图添加控件
      addMapOverlay();//向地图添加覆盖物
    }
    function createMap(){ 
      map = new BMap.Map("map"); 
      map.centerAndZoom(new BMap.Point(104.072727,30.555159),15);
    }
    function setMapEvent(){
      map.enableScrollWheelZoom();
      map.enableKeyboard();
      map.enableDragging();
      map.enableDoubleClickZoom()
    }
    function addClickHandler(target,window){
      target.addEventListener("click",function(){
        target.openInfoWindow(window);
      });
    }
    function addMapOverlay(){
      var markers = [
        {content:"我的备注",title:"我的标记",imageOffset: {width:0,height:3},position:{lat:30.552795,lng:104.075098}}
      ];
      for(var index = 0; index < markers.length; index++ ){
        var point = new BMap.Point(markers[index].position.lng,markers[index].position.lat);
        var marker = new BMap.Marker(point,{icon:new BMap.Icon("http://api.map.baidu.com/lbsapi/createmap/images/icon.png",new BMap.Size(20,25),{
          imageOffset: new BMap.Size(markers[index].imageOffset.width,markers[index].imageOffset.height)
        })});
        var label = new BMap.Label(markers[index].title,{offset: new BMap.Size(25,5)});
        var opts = {
          width: 200,
          title: markers[index].title,
          enableMessage: false
        };
        var infoWindow = new BMap.InfoWindow(markers[index].content,opts);
        marker.setLabel(label);
        addClickHandler(marker,infoWindow);
        map.addOverlay(marker);
      };
    }
    //向地图添加控件
    function addMapControl(){
      var scaleControl = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_LEFT});
      scaleControl.setUnit(BMAP_UNIT_IMPERIAL);
      map.addControl(scaleControl);
      var navControl = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_LARGE});
      map.addControl(navControl);
      var overviewControl = new BMap.OverviewMapControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT,isOpen:true});
      map.addControl(overviewControl);
    }
    var map;
      initMap();
}