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
				botData = {'output':{'text':data['welcomeMsg']}};
				chat_render('bot',botData);
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
	
	var sendMessage = function(sender, reqData) {
		console.log(reqData);
		// Ajax - send message to server.
		return $.ajax({
			url: 'assistant/sendMessage',
			type: 'POST',
			//contentType: 'application/json',
			data: reqData,
			dataType: 'json',
			async: false,
			success: function(response) {
				chat_render(sender, response);
				dialogContext = JSON.stringify(response['context']);
			},
			error: function(xhr){
				var err = JSON.parse(xhr.responseText);
				alert('Error : ' + err.Message);
			}
		});
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
				msgData = {'text':msg};
				chat_render('user', msgData);
				//set request Data
				reqData = {'text':msg, 'context':dialogContext};
				sendMessage('user', reqData);

				document.getElementById('chat-body').scrollTo(0, 9999);
			}
		}
	});
	
	// Add Event Listener on chat-bot-list response.
	$(document).on("click",".btn btn-outline-secondary", (function(listData){
	
		var msg = listData['input_text']
		var msgData = {'text':msg};
		chat_render('user',msgData);
		
		reqData = {'text':msg, 'context':dialogContext};
		sendMessage('user', reqData);
	}));
});