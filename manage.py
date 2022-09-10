from flask.cli import FlaskGroup

from app import app, db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('status')
def status():
    print(db.engine.url)
    print('Ok')


if __name__ == "__main__":
    cli()
