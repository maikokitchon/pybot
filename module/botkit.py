from builtins import dict

attachments = [{
	"blocks": [
		{
			"type": "action",
			"block_id": "actionblock1",
			"elements": [
				{
					"type": "datepicker",
					"action_id": "datepickeraction1",
					"initial_date": "2021-01-01",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					}
				},
				{
					"type": "timepicker",
					"action_id": "timepickeraction1",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item",
						"emoji": True
					}
				},
				{
					"type": "datepicker",
					"action_id": "datepickeraction2",
					"initial_date": "2021-01-01",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					}
				},
				{
					"type": "timepicker",
					"action_id": "timepickeraction2",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item",
						"emoji": True
					}
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit"
					},
					"value": "click_me_1",
					"action_id": "submitbtn1"
				}
			]
		}
	]
}]

def test_datetimepicker():
    data = dict()
    data['method'] = 'chat_postMessage'
    data['attachments'] = attachments
    data['text'] = f"Botkit testing POC for custom datetime picker."
    return data