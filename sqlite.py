import sqlite3

conn = sqlite3.connect("mycompany.db")
c = conn.cursor()

def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS employee (
                    employee_id integer PRIMARY KEY,
                    username text NOT NULL,
                    name text NOT NULL,
                    role text NOT NULL,
                    password text NOT NULL
                    ) ''')

    # method one of inserting values into the table
    employees = [(1, 'mtirr', 'Matt Tirrell', 'Poolboy','password'),
    (2, 'jfran', 'Jon Francis', 'Cool guy','password'), 
    (3, 'sharv', 'Steve Harvey', 'Elder','password')]
    c.executemany('INSERT INTO employee VALUES (?,?,?,?,?)', employees)

    emp_usernames = ('mhun','ctheiss','mmetz','rmetz',
    'mholz','dpicc','mschall','kschmid',
    'sbrown','cmart','aoberr','oendriss',
    'adq','pschild','vcatana','demard',
    'hfvogt', 'mdreher','kaafloy','epein',
    'pbeut','wmichaels','mkrufky','tjacobs',
    'jfthibs','klapray')

    # https://www.kernel.org/doc/html/v4.14/media/dvb-drivers/contributors.html
    emp_names = ('Michael Hunold','Christian Theiss','Marcus Metzler','Ralph Metzler',
    'Michael Holzt','Diego Picciani','Martin Schaller','Klaus Schmidinger',
    'Steve Brown','Christoph Martin','Andreas Oberritter','Oliver Endriss',
    'Andrew de Quincey','Peter Schildmann','Vadim Catana','Davor Emard',
    'Hans-Frieder Vogt', 'Michael Dreher','Kenneth Aafløy','Ernst Peinlich',
    'Peter Beutner','Wilson Michaels','Michael Krufky','Taylor Jacob',
    'Jean-Francois Thibert','Kirk Lapray')

    # fake job roles
    emp_roles = ('COO','CIO','CTO','CEO (empathy officer)','Intern','Ballroom dance enthusiast',
    'Cleaner', 'Deskclerk','Scribe','Dance party MC','Special effects officer','Firefighter',
    'Politician', 'Ragamuffin', 'Developer', 'QA Engineer', 'Site Engineer', 'Field Engineer',
    'Towel boy', 'Water boy', 'Cheerleader', 'Mafioso', 'Mod', 'Boss', 'Paleontologist','Layabout')

    emp_passwords = ('password')

    #method two of inserting values into the table
    for i in range(0,len(emp_names)):
            c.execute('INSERT INTO employee VALUES ('+str(i+4)+', "'+ emp_usernames[i] +'", "'+ emp_names[i] +'", "'+ emp_roles[i] +'", "'+ emp_passwords +'")')

    conn.commit()

def viewAllRows(dbtable):
    try:
        for row in c.execute("SELECT * FROM "+dbtable):
            print(row)
    except:
        print(dbtable+" is not defined. Add a "+ dbtable+ " first!")

def getTableLength(dbtable):
    c.execute("SELECT * FROM "+dbtable)
    next_id = len(c.fetchall()) + 1
    return next_id

def addUser():
    try:
        userid = getTableLength("employee")
        print("ADD NEW USER")
        username = input("Enter your username: ")
        name = input("Enter your name: ")
        role = input("Enter your job title: ")
        password = input("Enter your password: ")
        c.execute('INSERT INTO employee VALUES ('+str(userid)+', "'+username+'", "'+name+'", "'+role+'", "' +password+'")')
        print("user ",username," added to database.")
        conn.commit()
    except:
        print("Sorry, we had to create the table first")
        createTable()
        addUser()

def searchUser():
    val = input("Enter username: ")
    print(val)
    user = (val, )
    for row in c.execute('SELECT * FROM employee WHERE username=?',user):
        print(row)

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    myuser =  c.execute("SELECT * FROM employee WHERE username = '%s' AND password = '%s'" % (username, password))
    temporal_row = myuser.fetchone()
    if temporal_row == None:
        print("No user found or incorrect password.")
    else:
        print(temporal_row)
        message = input("Write your message: ")
        message = message.replace("'",r" ")
        message = message.replace('"',r" ")
        sendMessage(username, message)

def sendMessage(username, message):
    print()
    print("sendMessage function")
    print(username, message)
    userinfo = c.execute("SELECT * FROM employee WHERE username=?", (username, ))
    temporal_user = userinfo.fetchone() 

    c.execute('''CREATE TABLE IF NOT EXISTS messages (
            message_id integer PRIMARY KEY,
            message_text text NOT NULL,
            username text NOT NULL,
            name text NOT NULL,
            role text NOT NULL,
            password text NOT NULL,
            employee_id interger NOT NULL
            ) ''')

    message_id = getTableLength("messages")
    c.execute("INSERT INTO messages VALUES ("+str(message_id)+",'"+message+"','"+username+"','"+temporal_user[2]+"','"+temporal_user[3]+"','"+temporal_user[4]+"','"+str(temporal_user[0])+"')")
    conn.commit()
    print("success, '" + message + "' inserted into messages " + " from " + username)

def getMessagesByUser():
    employee_id = input("Enter employee_id: ")
    get_messages = c.execute('SELECT * FROM messages WHERE employee_id=?', (employee_id,))

    for message in get_messages:
        print(message)
    
def menu():
    print()
    print("~~Welcome to the mycompany database~~")
    print("Would you like to: ")
    print("V = View all users")
    print("M = View all messages")
    print("A = Add a user")
    print("Q = Query a user")
    print("L = Test login")
    print()
    val = input("Enter a choice:").upper()

    if (val == 'V'):
        viewAllRows("employee")
    if (val == 'M'):
        viewAllRows("messages")        
    if val == 'A':
        addUser()
    if val == 'Q':
        searchUser()
    if val == 'L':
        login()

    #special secret value if you need to re-create the employee table.
    if val == 'C':
        createTable()
    #another secret value. still working out the kinks.
    if val == 'UM':
        getMessagesByUser()

menu()
conn.close()