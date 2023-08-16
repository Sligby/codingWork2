import requests
from flask import Flask, render_template
app = Flask(__name__)
def fav_number_fact(fav_number):
    url = f"http://numbersapi.com/{fav_number}?json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return f"Failed to retrieve a fact for number {fav_number}."

@app.route('/one_of_many')
def batch_num_facts():
    numbers = [7, 42, 99, 123]
    base_url = "http://numbersapi.com/"
    query_params = ",".join(str(number) for number in numbers)
    response = requests.get(f"{base_url}{query_params}?json=true")

    if response.status_code == 200:
        data = response.json()
        facts = [data[str(number)]['text'] for number in numbers]
    else:
        facts = []

    return render_template('number_facts.html', facts=facts)

if __name__ == '__main__':
    app.run()

@app.route('/many_on_one')
def get_number_facts():
    number = 8
    base_url = "http://numbersapi.com/"
    query_params = ",".join(str(number) for _ in range(4))
    response = requests.get(f"{base_url}{query_params}?json=true")

    if response.status_code == 200:
        data = response.json()
        facts = [data[str(number)]['text'] for _ in range(4)]
    else:
        facts = []

    return render_template('number_facts.html', facts=facts)

if __name__ == '__main__':
    app.run()