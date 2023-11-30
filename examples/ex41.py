from flask import Flask, jsonify, request
from my_utils import dir2

app = Flask(__name__)
# print(dir2(app))

# global list to store customer data
customers = [
    dict(id=1, name='Vinod Kumar', email='vinod@vinod.co', phone='9731424784'),
    {'id': 2, 'name': 'Shyam Sundar', 'email': 'shyam@xmpl.com', 'phone': '8765182731'}
]
next_id = 3


@app.route('/api/customers', methods=['POST'])
def handle_post():
    global next_id, customers
    try:
        new_cust_data = request.get_json()

        if 'name' not in new_cust_data or 'email' not in new_cust_data or 'phone' not in new_cust_data:
            return jsonify({'error': 'name, email and phone are required.'}), 400

        new_cust = {
            'id': next_id,
            'name': new_cust_data.get('name'),
            'email': new_cust_data.get('email'),
            'phone': new_cust_data.get('phone'),
        }
        next_id += 1
        customers.append(new_cust)

        return jsonify(new_cust), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 500


@app.route('/api/customers', methods=['GET'])
def handle_get():
    return jsonify(customers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
