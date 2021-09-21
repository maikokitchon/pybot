from builtins import dict

attachments = [{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a date for the deadline."
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick the hour for the deadline"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "10",
							"emoji": False
						},
						"value": "10"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "11",
							"emoji": False
						},
						"value": "11"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "12",
							"emoji": False
						},
						"value": "12"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "13",
							"emoji": False
						},
						"value": "13"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "14",
							"emoji": False
						},
						"value": "14"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick the minute for the deadline"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "10",
							"emoji": False
						},
						"value": "10"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "11",
							"emoji": False
						},
						"value": "11"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "12",
							"emoji": False
						},
						"value": "12"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "13",
							"emoji": False
						},
						"value": "13"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "14",
							"emoji": False
						},
						"value": "14"
					}
				]
			}
		}
	]
}]

def test_datetimepicker():
    data = dict()
    data['method'] = 'chat_postMessage'
    data['attachments'] = attachments
    data['text'] = f"Botkit testing POC for custom datetime picker."
    return data