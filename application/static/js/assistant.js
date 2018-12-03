$(document).ready(function () {
	
	// Get Service Credential Function.
	$("#sc-request").click(function(){

		username = $("#assistUsername").val();
		password = $("#assistPass").val();
		workspaceId = $("#workspaceId").val();
		
		$.ajax({
			url: "assistant/initService",
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
				$("#chat-input").attr('class', 'chat-input-enabled');
				
				console.log(typeof(data));
				resText = data['text'];
				console.log(resText);
				alert('Success : '+resText);
				renderBotLog(resText);
			},
			error: function(xhr){
				var err = JSON.parse(xhr.responseText);
				// change chat-body CSS
				$("#chat-body").attr('class', 'chat-body-disabled');
				$("#input_message").attr('disabled', true);
				$("#chat-input").attr('class', 'chat-input-disabled');
				
				alert('Error : ' + err.Message);
			}
		});
		
	});
	
	// Rendering Chatting Log.
	function renderUserLog(msg) {
		var chat = document.createElement('p');
		chat.innerHTML=msg;
		var chatLog = document.createElement('div');
		chatLog.setAttribute('class', 'chat-user-log')
		chatLog.appendChild(chat)

		$('#chat-talk-area').append(chatLog)
	}
	
	function renderBotLog(response) {
		var msg = response.text;
		
		var chat = document.createElement('p');
		chat.innerHTML=msg;
		var chatLog = document.createElement('div');
		chatLog.setAttribute('class', 'chat-bot-log')
		chatLog.appendChild(chat)

		$('#chat-talk-area').append(chatLog)
	}
	
	
	
	// Enter key function
	$("#input_message").keydown(function(key) {
		if (key.keyCode == 13) {
			var msg = $("#input_message").val().trim();
			
			if(msg == null || msg == '') {
				//console.log("Input text is nothing");
				return null;
			}
			else {
				//console.log("Enter pressed: "+msg);
				$("#input_message").val('');
				// render chat log
				renderUserLog(msg);

				// Ajax - send message to server.
				$.ajax({
					url: "assistant/sendMessage",
					type: 'POST',
					data: {"text":msg},
					dataType: 'html',
					success: function(data) {
						renderBotLog(data);
					},
					error: function(xhr){
						var err = JSON.parse(xhr.responseText);
						alert('Error : ' + err.Message);
					}
				});
				
			}
			$("#chat-body").scrollTop(9999);
		}
	});



});