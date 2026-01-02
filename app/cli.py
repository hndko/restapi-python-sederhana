import click
from flask.cli import with_appcontext
from .extensions import db
from .models.user import User
from .models.person import Person
from werkzeug.security import generate_password_hash

@click.command('seed')
@with_appcontext
def seed_command():
    """Mengisi database dengan data awal (Seeder)."""

    # 1. Seed User
    click.echo('Seeding Users...')
    if not User.query.filter_by(username='admin').first():
        user = User(username='admin')
        user.set_password('admin123')
        db.session.add(user)
        click.echo(' - Created user: admin / admin123')
    else:
        click.echo(' - User admin already exists.')

    if not User.query.filter_by(username='user').first():
        user = User(username='user')
        user.set_password('user123')
        db.session.add(user)
        click.echo(' - Created user: user / user123')
    else:
        click.echo(' - User user already exists.')

    # 2. Seed Person
    click.echo('Seeding People...')
    people_data = [
        {"nama": "Budi Santoso", "umur": 25, "alamat": "Jl. Sudirman No. 1, Jakarta"},
        {"nama": "Siti Aminah", "umur": 28, "alamat": "Jl. Thamrin No. 10, Jakarta"},
        {"nama": "Andi Wijaya", "umur": 35, "alamat": "Jl. Gatot Subroto No. 5, Bandung"},
        {"nama": "Dewi Lestari", "umur": 22, "alamat": "Jl. Malioboro No. 3, Yogyakarta"},
        {"nama": "Rudi Hartono", "umur": 40, "alamat": "Jl. Pahlawan No. 8, Surabaya"},
    ]

    for data in people_data:
        # Cek duplikasi based on nama untuk demo
        if not Person.query.filter_by(nama=data['nama']).first():
            person = Person(
                nama=data['nama'],
                umur=data['umur'],
                alamat=data['alamat']
            )
            db.session.add(person)
            click.echo(f" - Created person: {data['nama']}")
        else:
            click.echo(f" - Person {data['nama']} already exists.")

    db.session.commit()
    click.echo('Database seeded successfully!')
