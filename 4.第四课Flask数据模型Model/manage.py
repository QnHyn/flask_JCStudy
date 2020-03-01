from flask_script import Manager
from App import create_app
from flask_migrate import MigrateCommand
import os


# 这样做的好处是，在开发的电脑上就是开发环境。在测试电脑上就是测试环境。
# 前提需要配置环境变量的值FLASK_ ENV。
env = os.environ.get("FLASK_ ENV", "develop")

app = create_app(env)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
