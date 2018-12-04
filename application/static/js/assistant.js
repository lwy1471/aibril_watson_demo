$(document).ready(function () {
	var dialogContext = '';
	
	// Get Service Credential Function.
	$('#sc-request').click(function(){

		username = $('#assistUsername').val();
		password = $('#assistPass').val();
		workspaceId = $('#workspaceId').val();
		
		$.ajax({
			url: 'assistant/initService',
			type: 'POST',
			data: {
				'username':username,
				'password':password,
				'workspaceId':workspaceId
			},
			dataType: 'json',
			success : function(data) {
				// change chat-body CSS
				$('#chat-body').attr('class', 'chat-body');
				$('#input_message').removeAttr('disabled');
				$('#chat-input').attr('class', 'chat-input-enabled');

				resText = data['text'];
				alert(resText);
				botChat = {'output':{'text':data['welcomeMsg']}};
				renderBotLog(botChat);
			},
			error: function(xhr){
				var err = JSON.parse(xhr.responseText);
				// change chat-body CSS
				$('#chat-body').attr('class', 'chat-body-disabled');
				$('#input_message').attr('disabled', true);
				$('#chat-input').attr('class', 'chat-input-disabled');
				
				alert('Error : ' + err.err);
			}
		});
		
	});
	
	// Rendering Chatting Log.
	function renderUserLog(msg) {
		var chat = document.createElement('p');
		chat.innerHTML=msg;
		var chatLog = document.createElement('div');
		chatLog.setAttribute('class', 'chat-log-user')
		chatLog.appendChild(chat)

		$('#chat-talk-area').append(chatLog)
	}
	
	function renderBotLog(response) {
		var text = response['output']['text'];
		var chat = document.createElement('p');
		chat.innerHTML=text;
		var chatLog = document.createElement('div');
		chatLog.setAttribute('class', 'chat-log-bot')
		chatLog.appendChild(chat)

		$('#chat-talk-area').append(chatLog)
		
	}
	
	
	
	// Enter key function
	$('#input_message').keydown(function(key) {
		if (key.keyCode == 13) {
			var msg = $('#input_message').val().trim();
			
			if(msg == null || msg == '') {
				//console.log('Input text is nothing');
				return null;
			}
			else {
				//console.log('Enter pressed: '+msg);
				$('#input_message').val('');
				//render chat log
				renderUserLog(msg);
				
				//set request Data
				reqData = {'text':msg, 'context':dialogContext};
				
				// Ajax - send message to server.
				$.ajax({
					url: 'assistant/sendMessage',
					type: 'POST',
					//contentType: 'application/json',
					data: reqData,
					dataType: 'json',
					success: function(data) {
						renderBotLog(data);
						dialogContext = JSON.stringify(data['context']);
						document.getElementById('chat-body').scrollTo(0, 9999)
					},
					error: function(xhr){
						var err = JSON.parse(xhr.responseText);
						alert('Error : ' + err.Message);
					}
				});
				
			}
		}
	});



});