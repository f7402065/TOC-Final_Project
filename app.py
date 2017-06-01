import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '375541027:AAFvLkySNkMSGgOl7PtsPIsJgnxophQpllQ'
WEBHOOK_URL = 'https://a140f4ad.ngrok.io/show-fsm'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11',
        'state12',
        'state13',
        'state14',
        'state15'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_from_state0_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state4',
            'conditions': 'is_going_from_state3_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state5',
            'conditions': 'is_going_from_state4_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_from_state5_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state7',
            'conditions': 'is_going_from_state5_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state8',
            'conditions': 'is_going_from_state4_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state9',
            'conditions': 'is_going_from_state8_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state8',
            'conditions': 'is_going_from_state6_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state8',
            'conditions': 'is_going_from_state7_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state5',
            'conditions': 'is_going_from_state9_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state10',
            'conditions': 'is_going_from_state9_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state10',
            'conditions': 'is_going_from_state6_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state10',
            'conditions': 'is_going_from_state7_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state11',
            'conditions': 'is_going_from_state8_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state10',
            'conditions': 'is_going_from_state11_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state5',
            'conditions': 'is_going_from_state11_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state12',
            'conditions': 'is_going_from_state8_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state10',
            'conditions': 'is_going_from_state12_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state5',
            'conditions': 'is_going_from_state12_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state13',
            'conditions': 'is_going_from_state8_to_state13'
        },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state10',
            'conditions': 'is_going_from_state13_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state5',
            'conditions': 'is_going_from_state13_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state14',
            'conditions': 'is_going_from_state8_to_state14'
        },
        {
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state10',
            'conditions': 'is_going_from_state14_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state5',
            'conditions': 'is_going_from_state14_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state15',
            'conditions': 'is_going_from_state8_to_state15'
        },
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state10',
            'conditions': 'is_going_from_state15_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state5',
            'conditions': 'is_going_from_state15_to_state5'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state10'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
