window.onload=function(){
	$(".navbar-nav>li>a").hover(function(){
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
	$("#myTab>li>a").on("click",function(){
		$("#myTab>li>a").css("border-bottom","1px solid white").css("font-size","16px");
		$(this).css("border-bottom","2px solid #000").css("font-size","16px");
	});
//	$("#huodong>a").click(function(){
//		 $("#row9").slideToggle(200);
//	});
	
	$("#row5 .col-md-11").hover(
			function(){
				$(this).css("cursor","pointer");
			},
			function(){
				
			}
	);
	
	
	$("#row5 .row11").each(function(index,value){
		var topl = (index)*0;
		$(this).css("top",topl+"px");
	});
	
	$("#row5 .row11").hover(function(){
		$(this).css("border-top","1px solid rgb(180, 180, 180)").css("border-bottom","1px solid rgb(180, 180, 180)").css("border-left","1px solid rgb(180, 180, 180)")
		$(this).find(".tanchukuang").css("display","block").css("border","1px solid rgb(180, 180, 180)");
	},function(){
		$(this).css("border","1px solid white");
		$(this).find(".tanchukuang").css("display","none").css("border","1px solid white");
	});
	
	$("#row5 .row11 .tanchukuang").each(function(index,value){
		$(this).find("div a").each(function(index,value){
			if(index<3){
				$(this).css("color","#00FF99");
			}
		});
	});
}