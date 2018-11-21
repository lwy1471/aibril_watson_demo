$(document).ready(function () {
	$("#sc-request").click(function(){

		username = $("#assistUsername").val();
		password = $("#assistPass").val();
		workspaceId = $("#workspaceId").val();
		
		$.ajax({
			url: "assistant/InitService",
			type: 'POST',
			data: {
				"username":username,
				"password":password,
				"workspaceId":workspaceId
			},
			dataType: 'html',
			success : function(data) {
				// change chat-body CSS
				$("#chat-body").attr('class', 'chat-body');
				$("#input_message").removeAttr("disabled");
				alert('Success : '+data);
			},
			error: function(xhr){
				var err = JSON.parse(xhr.responseText);
				// change chat-body CSS
				$("#chat-body").attr('class', 'chat-body-disabled');
				$("#input_message").attr('disabled', true);
				alert('Error : ' + err.Message);
			}
		});
		
	});
	
	$("#input_message").keydown(function(key) {
		if (key.keyCode == 13) {
			var msg = $("#input_message").val().trim();
			
			if(msg == null || msg == '') {
				//console.log("Input text is nothing");
			}
			else {
				//console.log("Enter pressed: "+msg);
				$("input_message").val()=null;
			}
			
		}
	});



});