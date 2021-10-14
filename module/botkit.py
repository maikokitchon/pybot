from builtins import dict
from datetime import datetime

attachments = [{
	"blocks": [
		{
			"type": "actions",
			"block_id": "actionblock1",
			"elements": [
				{
					"type": "datepicker",
					"action_id": "datepickeraction1",
					"initial_date": f"{datetime.today().strftime('%Y-%m-%d')}",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date"
					}
				},
				{
					"type": "timepicker",
					"action_id": "timepickeraction1",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
					}
				},
				{
					"type": "datepicker",
					"action_id": "datepickeraction2",
					"initial_date": f"{datetime.today().strftime('%Y-%m-%d')}",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date"
					}
				},
				{
					"type": "timepicker",
					"action_id": "timepickeraction2",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
					}
				},
				{
					"type": "static_select",
					"action_id": "selectappaction1",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an environment"
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "gst"
							},
							"value": "GST"
						}
					]
				},
				{
					"type": "static_select",
					"action_id": "selectenvaction1",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an environment"
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "dev7"
							},
							"value": "DEV7"
						}
					]
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

def process_datetimepicker(args):
	print(args)
	return "Data has been received."