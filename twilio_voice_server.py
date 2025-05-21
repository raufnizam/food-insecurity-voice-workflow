from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    resp.say("Hello. This is a test. If you hear this, the call is working.")
    resp.pause(length=3)
    resp.say("This confirms that the Twilio call can play audio successfully.")
    resp.hangup()
    return Response(str(resp), mimetype='application/xml')


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    digits = request.values.get('Digits')

    if digits is None:
        gather = Gather(input='dtmf', timeout=10, num_digits=1, action="/q2")
        gather.say(
            "Hi, this is the Baylor Scott Nutrition Team. "
            "In the last 12 months, have you worried whether your food would run out before you had money to buy more? "
            "Press 1 for Yes, or 2 for No."
        )
        resp.append(gather)
        resp.say("We did not receive your response. Goodbye.")
        resp.hangup()
    else:
        resp.redirect('/q2')

    return Response(str(resp), mimetype='application/xml')


@app.route("/q2", methods=['GET', 'POST'])
def q2():
    digits = request.values.get('Digits', '')
    print(f"[DEBUG] Answer to Q1: {digits}")
    resp = VoiceResponse()

    if digits == '1':
        gather = Gather(input='dtmf', timeout=10, num_digits=1, action="/next_steps")
        gather.say(
            "In the last 12 months, did the food you bought just not last, and you didn’t have money to get more? "
            "Press 1 for Yes, or 2 for No."
        )
        resp.append(gather)
        resp.say("We did not receive your response. Goodbye.")
        resp.hangup()
    else:
        resp.say("Thank you for your time. Goodbye.")
        resp.hangup()

    return Response(str(resp), mimetype='application/xml')


@app.route("/next_steps", methods=['GET', 'POST'])
def next_steps():
    digits = request.values.get('Digits', '')
    print(f"[DEBUG] Answer to Q2: {digits}")
    resp = VoiceResponse()

    if digits == '1':
        resp.say("Thank you. We’ll now follow up with more questions via SMS or a care team member.")
    else:
        resp.say("Thank you for your time.")
    resp.hangup()

    return Response(str(resp), mimetype='application/xml')


if __name__ == "__main__":
    app.run(port=5000)
