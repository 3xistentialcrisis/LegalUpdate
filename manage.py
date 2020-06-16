from flask_script import Manager, Server
from app.models import User,Role
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

#Create App Instance
app = create_app('development')
manager = Manager(app)
manager.add_command("server", Server)

# Initialise Migrate Class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Create Flask-script shell
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

#Tests
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)


if __name__ == "__main__":
    manager.run()
