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
		return renderBotLog(data);
	}
	
}

// bot rendering function
function renderBotLog(data) {

	/*
	rendering message example which is from server.
	"context": {
		"render": [
		  {
			"type": "list",
			"textlist": [
			  "대한항공",
			  "아시아나",k
			  "델타항공"
			]
		  },
		  {
			"type": "img",
			"urls": [
			  "{url1}",
			  "{url2}",
			  "{url3}"
			]
		  },		  
		]
	},
	*/


	var chatLog = create_bot_div();
	var text = data['output']['text'];
	var chatText = document.createElement('p');
	chatText.innerHTML=text;
	chatLog.appendChild(chatText);
	
	var eventCandidate = false;


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
											
					eventCandidate = {'type':'list', 'list':[]};
					for (var cnt in render['textlist']) {
						text = render['textlist'][cnt];
						var list = document.createElement('button');
						list.setAttribute('class', 'btn btn-outline-secondary');
						list.setAttribute('id', 'chat-log-bot-list');
						list.innerHTML=text;
						$('#chat-talk-area').append(list);

						eventCandidate['list'].push(list);
					}
					//console.log(eventCandidate);
					break;

			}
			data['context']['render']=null;
		}
		
	}
	
	return eventCandidate;
}

	
