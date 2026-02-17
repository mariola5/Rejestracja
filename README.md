System rezerwacji sal

1. Opis projektu
Aplikacja webowa napisana w Django umożliwiająca rezerwację sal.
System pozwala użytkownikom tworzyć rezerwacje bez konfliktów czasowych oraz zarządzać swoimi rezerwacjami.

2. Wymagania
a) Python 3.14+
b) Django 6+
c) Git
3. Instrukcja uruchomienia projektu lokalnie
a) Sklonuj repozytorium
git clone https://github.com/mariola5/Rejestracja.git
cd Rejestracja
b) Utwórz i aktywuj środowisko wirtualne
python -m venv .venv
.venv\Scripts\activate
c) Zainstaluj zależności
pip install django
d) Wykonaj migracje
python manage.py migrate
e) Utwórz administratora 
python manage.py createsuperuser
f) Uruchom serwer
python manage.py runserver
g) Panel administratora będzie dostępny pod adresem:
http://127.0.0.1:8000/admin/
4. Funkcjonalności. 
4.1 Użytkownik może:
a) Zalogować się do systemu
b) Zobaczyć listę rezerwacji
c) Filtrować rezerwacje:
po sali, tylko swoje, przyszłe
d) Utworzyć rezerwację
e) Otrzymać komunikat o:
sukcesie, konflikcie czasowym, błędach formularza
f) Usunąć tylko swoje rezerwacje 
4.2 Administrator może:
a) Logować się do panelu admina
b) Tworzyć użytkowników
c) Dodawać i edytować sale
d) Przeglądać wszystkie rezerwacje
f) Usuwać rezerwacje
5. Walidacja i bezpieczeństwo. System blokuje:
a) Rezerwacje w przeszłości
b) Rezerwacje z datą końcową wcześniejszą niż początkowa
c) Nakładające się rezerwacje tej samej sali
d) Usuwanie cudzych rezerwacji

6. Instrukcja użytkowania
6.1 Dla zwykłego użytkownika:
a) Zaloguj się.
b) Wybierz salę.
c) Podaj datę rozpoczęcia i zakończenia.
d) Dodaj tytuł i opcjonalny opis.
e) Kliknij „Zarezerwuj”.
f) W razie konfliktu pojawi się komunikat błędu.
g) Możesz usunąć swoją rezerwację przyciskiem „Usuń”.
6.2 Dla administratora:
a) Zaloguj się do /admin.
b) Dodaj sale (nazwa, pojemność, lokalizacja).
c) Twórz użytkowników.
d) Zarządzaj rezerwacjami.