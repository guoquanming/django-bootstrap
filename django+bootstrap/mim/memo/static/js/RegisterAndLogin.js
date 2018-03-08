window.onload=function(){
	//-----------------------------------------------滚动广告-------------------------------------------------------------------------------------------	
	
	  $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
	
  //------------------------------------------------------------加载背景图片--------------------------------------------------------------    
    $("#row2").css("background-image","url(images/register2.png)");
//------------------------------------------------------------注册登录选项卡-----------------------------------------------------------------
	$("#tabbutton1").on("click",function(){
		$("#tabbutton1 a").css("color","rgb(255, 136, 0)");
		$(this).css("background","white");
		$(this).css("border-bottom","2px solid rgb(255, 136, 0)");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
		//----------------------------------------------
		$("#tabbutton2 a").css("color","#000");
		$("#tabbutton2").css("border-bottom","1px solid white");
		$("#tabbutton2").css("border-top","1px solid white");
		$("#tabbutton2").css("border-left","1px solid white");
		$("#tabbutton2").css("border-right","1px solid white");
	});
	$("#tabbutton2").on("click",function(){
		$("#tabbutton1 a").css("color","rgb(255, 136, 0)");
		$(this).css("background","white");
		$(this).css("border-bottom","2px solid rgb(255, 136, 0)");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
		//----------------------------------------------
		$("#tabbutton1 a").css("color","#000");
		$("#tabbutton1").css("border-bottom","1px solid white");
		$("#tabbutton1").css("border-top","1px solid white");
		$("#tabbutton1").css("border-left","1px solid white");
		$("#tabbutton1").css("border-right","1px solid white");
	});
	
//------------------------------------------------------------------------------------------------------------------------------
	$("#tabbutton1 a").hover(function(){
		$(this).css("background","white");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
	},function(){
		$(this).css("background","white");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
	});
	$("#tabbutton2 a").hover(function(){
		$(this).css("background","white");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
	},function(){
		$(this).css("background","white");
		$(this).css("border-top","1px solid white");
		$(this).css("border-left","1px solid white");
		$(this).css("border-right","1px solid white");
	});
//-------------------------去除表单输入框发光效果---------------------------------
$("input").on("focus",function(){
		$(this).css("border","1px solid white").css("outline","none");
		
});
//--------------------------------------------------------------------------------
$(".register").on("click",function(){
	$(".div1 p").text("立即注册");
});
$(".login").on("click",function(){
	$(".div1 p").text("立即登录");
});
}
