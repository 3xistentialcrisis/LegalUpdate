from flask_script import Manager, Server
from app.models import Lawyers, Case, Status
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

#Create App Instance
app = create_app('production')
manager = Manager(app)
manager.add_command("server", Server)

# Initialise Migrate Class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Create Flask-script shell
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Lawyers=Lawyers, Case = Case, Status = Status)

#Tests
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)


if __name__ == "__main__":
    # Set the secret key to some random bytes. Keep this really secret!
    manager.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    manager.run()
