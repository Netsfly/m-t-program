library_books = {
    "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
    "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
}

def calculate_fines(library_books):
    total_fine = 0
    borrower_fines = {}
    for book_id, book_info in library_books.items():
        days_overdue = book_info["due_date"]
        fine_rate = book_info["fine_rate"]
        fine = 0
        status = "Доступна"
        if book_info["borrower"]:
            if days_overdue > 0:
                status = "В срок"
            elif days_overdue < 0:
                status = "Просрочена"
                fine = abs(days_overdue) * fine_rate
                total_fine += fine
                borrower_fines[book_info["borrower"]] = borrower_fines.get(book_info["borrower"], 0) + fine
        else:
            status = "Доступна"
            fine = 0
        print(f"Книга {book_id}: {book_info['title']}, Заемщик: {book_info['borrower'] or 'Нет'}, Статус: {status}, Штраф: ${fine:.2f}")
    
    max_borrower = max(borrower_fines, key=borrower_fines.get, default=None)
    if max_borrower:
        print(f"Заемщик с наибольшими штрафами: {max_borrower}, Общий штраф: ${borrower_fines[max_borrower]:.2f}")

calculate_fines(library_books)
