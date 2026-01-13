from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Create sample books for testing'

    def handle(self, *args, **options):
        books_data = [
            {
                'title': 'Война и мир',
                'author': 'Лев Толстой',
                'category': 'Классическая литература',
                'description': 'Роман-эпопея, описывающий русское общество в эпоху войн против Наполеона.',
                'pages': 1225,
            },
            {
                'title': '1984',
                'author': 'Джордж Оруэлл',
                'category': 'Антиутопия',
                'description': 'Роман о тоталитарном обществе, где государство контролирует все аспекты жизни граждан.',
                'pages': 328,
            },
            {
                'title': 'Мастер и Маргарита',
                'author': 'Михаил Булгаков',
                'category': 'Фантастика',
                'description': 'Мистический роман о визите дьявола в советскую Москву.',
                'pages': 480,
            },
            {
                'title': 'Преступление и наказание',
                'author': 'Фёдор Достоевский',
                'category': 'Классическая литература',
                'description': 'Психологический роман об убийстве и его последствиях.',
                'pages': 671,
            },
            {
                'title': 'Гарри Поттер и философский камень',
                'author': 'Дж. К. Роулинг',
                'category': 'Фэнтези',
                'description': 'История о юном волшебнике и его приключениях в Хогвартсе.',
                'pages': 223,
            },
            {
                'title': 'Властелин колец',
                'author': 'Дж. Р. Р. Толкин',
                'category': 'Фэнтези',
                'description': 'Эпическое фэнтези о путешествии для уничтожения Кольца Всевластия.',
                'pages': 1216,
            },
            {
                'title': 'Маленький принц',
                'author': 'Антуан де Сент-Экзюпери',
                'category': 'Детская литература',
                'description': 'Философская сказка о маленьком принце и его путешествиях.',
                'pages': 96,
            },
            {
                'title': 'О дивный новый мир',
                'author': 'Олдос Хаксли',
                'category': 'Антиутопия',
                'description': 'Роман о будущем обществе, где люди генетически запрограммированы.',
                'pages': 311,
            },
            {
                'title': 'Алиса в Стране чудес',
                'author': 'Льюис Кэрролл',
                'category': 'Детская литература',
                'description': 'Сказка о приключениях девочки Алисы в волшебном мире.',
                'pages': 192,
            },
            {
                'title': 'Дюна',
                'author': 'Фрэнк Герберт',
                'category': 'Научная фантастика',
                'description': 'Научно-фантастический роман о планете Арракис и борьбе за специю.',
                'pages': 688,
            }
        ]

        created_count = 0
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Создана книга: {book.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Книга уже существует: {book.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {created_count} книг')
        )
