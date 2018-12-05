function create_bot_div() {
	var chat_bot = document.createElement('div');
	chat_bot.setAttribute('class','chat-log-bot');
	$('#chat-talk-area').append(chat_bot);
	return chat_bot;
}

function chat_render(chatter,data) {
	if (chatter=='user') {
		var chatLog = document.createElement('div');
		chatLog.setAttribute('class', 'chat-log-user');
		$('#chat-talk-area').append(chatLog);
		
		var chat = document.createElement('p');
		chat.innerHTML=data['text'];
		chatLog.appendChild(chat);

	}
	else {
		renderBotLog(data);
	}
	
}

// 데이터 종류에 따라 보여줄 것에 대한 업데이트 필요
function renderBotLog(data) {

	var chatLog = create_bot_div();
	var text = data['output']['text'];
	var chatText = document.createElement('p');
	chatText.innerHTML=text;
	chatLog.appendChild(chatText);


	if(data['context'] && data['context']['render']) {
		
		for (var cnt in data['context']['render']) {
			var render = data['context']['render'][cnt];
			switch (render['type']) {
				case 'img':
					if(!render['urls'])
						continue;
					for (var cnt in render['urls']) {
						url = render['urls'][cnt];
						var img = document.createElement('img');
						img.setAttribute('src',url);
						chatLog.appendChild(img);
					}
					break;
				case 'list':
					if(!render['textlist'])
						continue;
					for (var cnt in render['textlist']) {
						text = render['textlist'][cnt];
						var list = document.createElement('button');
						list.setAttribute('class', 'btn btn-outline-secondary');
						list.setAttribute('id', 'chat-log-bot-list');
						list.innerHTML=text;
						$('#chat-talk-area').append(list);
					}
					break;

			}
			data['context']['render']=null;
		}
		
	}
	
}