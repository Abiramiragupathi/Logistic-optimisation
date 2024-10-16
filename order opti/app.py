from flask import Flask, render_template, request, redirect, url_for
from warehouse_optimizer import optimize_warehouse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        order_details = request.form.to_dict()
        return redirect(url_for('process_order', **order_details))
    return render_template('index.html')

@app.route('/process_order', methods=['GET'])
def process_order():
    order_details = request.args.to_dict()
    
    # Add checks to handle missing data
    if not order_details.get('products'):
        return "Error: No products provided."
    
    warehouse_info = optimize_warehouse(order_details)
    return render_template('result.html', warehouse=warehouse_info)

if __name__ == '__main__':
    app.run(debug=True)
