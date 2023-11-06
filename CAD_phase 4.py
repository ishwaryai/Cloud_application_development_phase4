from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize variables for disaster recovery plan
disaster_recovery_plan = {
    "RTO": None,
    "RPO": None,
    "priority": None,
    "backup_tool": None
}

# Initialize variables for virtual servers, DB2, object storage, and Watson Assistant
virtual_servers = []
db2_servers = []
object_storage = []
watson_assistant = []

# Initialize variables for backups
backup_schedule = []


@app.route('/')
def index():
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/update_plan', methods=['POST'])
def update_plan():
    disaster_recovery_plan['RTO'] = request.form['RTO']
    disaster_recovery_plan['RPO'] = request.form['RPO']
    disaster_recovery_plan['priority'] = request.form['priority']
    disaster_recovery_plan['backup_tool'] = request.form['backup_tool']
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/add_server', methods=['POST'])
def add_server():
    server_name = request.form['server_name']
    virtual_servers.append(server_name)
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/add_db2', methods=['POST'])
def add_db2():
    db2_name = request.form['db2_name']
    db2_servers.append(db2_name)
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/add_storage', methods=['POST'])
def add_storage():
    storage_name = request.form['storage_name']
    object_storage.append(storage_name)
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/add_assistant', methods=['POST'])
def add_assistant():
    assistant_name = request.form['assistant_name']
    watson_assistant.append(assistant_name)
    return render_template('index.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)




# ... Previous code ...


@app.route('/view_plan')
def view_plan():
    return render_template('view_plan.html', plan=disaster_recovery_plan,
                           servers=virtual_servers, db2=db2_servers,
                           storage=object_storage, assistant=watson_assistant,
                           backups=backup_schedule)


@app.route('/update_priority', methods=['POST'])
def update_priority():
    server_name = request.form['server_name']
    priority = request.form['priority']

    for server in virtual_servers:
        if server == server_name:
            disaster_recovery_plan['priority'] = priority
            break

    return redirect('/view_plan')

# ... Existing code ...
# ... Previous code ...


@app.route('/add_backup', methods=['POST'])
def add_backup():
    backup_name = request.form['backup_name']
    backups.append(backup_name)
    return redirect('/view_plan')

# ... Existing code ...
# ... Previous code ...

# Error handling


@app.errorhandler(404)
def page_not_found(e):
    return "404 Page Not Found", 404

# Data persistence


def save_data():
    with open('data.txt', 'w') as file:
        file.write(f"{disaster_recovery_plan}\n")
        file.write(f"{virtual_servers}\n")
        file.write(f"{db2_servers}\n")
        file.write(f"{object_storage}\n")
        file.write(f"{watson_assistant}\n")
        file.write(f"{backup_schedule}\n")


def load_data():
    try:
        with open('data.txt', 'r') as file:
            data = file.readlines()
            if data:
                global disaster_recovery_plan, virtual_servers, db2_servers, object_storage, watson_assistant, backup_schedule
                disaster_recovery_plan = eval(data[0])
                virtual_servers = eval(data[1])
                db2_servers = eval(data[2])
                object_storage = eval(data[3])
                watson_assistant = eval(data[4])
                backup_schedule = eval(data[5])
    except FileNotFoundError:
        pass



# Load data on application startup
load_data()


@app.route('/save_plan')
def save_plan():
    save_data()
    return "Data saved successfully"


def save_data():
    with open('data.txt', 'w') as file:
        file.write(f"{disaster_recovery_plan}\n")
        file.write(f"{virtual_servers}\n")
        file.write(f"{db2_servers}\n")
        file.write(f"{object_storage}\n")
        file.write(f"{watson_assistant}\n")
        file.write(f"{backup_schedule}\n")
def load_data():
    try:
        with open('data.txt', 'r') as file:
            data = file.readlines()
            global disaster_recovery_plan, virtual_servers, db2_servers, object_storage, watson_assistant, backup_schedule
            disaster_recovery_plan = eval(data[0])
            virtual_servers = eval(data[1])
            db2_servers = eval(data[2])
            object_storage = eval(data[3])
            watson_assistant = eval(data[4])
            backup_schedule = eval(data[5])
    except FileNotFoundError:
        pass

def reset_data():
    global disaster_recovery_plan, virtual_servers, db2_servers, object_storage, watson_assistant, backup_schedule
    disaster_recovery_plan = {
        "RTO": None,
        "RPO": None,
        "priority": None,
        "backup_tool": None
    }
    virtual_servers = []
    db2_servers = []
    object_storage = []
    watson_assistant = []
    backup_schedule = []

# ... Previous code ...
@app.route('/reset_data')
def reset_saved_data():
    reset_data()
    return redirect('/view_plan')

@app.route('/reset_success')
def reset_success():
    return "Data reset successfully. <a href='/'>Go back</a>."
if __name__ == '__main__':
    app.run(debug=True)