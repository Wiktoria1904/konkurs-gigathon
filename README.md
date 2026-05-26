# Symulator Wyprawy Łazika

Witaj w symulatorze wyprawy łazika po dwuwymiarowym świecie! Twoim zadaniem jest dotarcie do celu, zarządzając ograniczonymi zasobami paliwa i stawiając czoła nieprzewidywalnym zdarzeniom.

## Opis Gry

Gra jest symulacją, w której sterujesz łazikiem na kwadratowej mapie. Musisz dotrzeć do losowo wygenerowanego celu, unikając przeszkód i zbierając paliwo.

### Funkcje:
- **Wizualizacja:** Śledź ruch łazika w czasie rzeczywistym dzięki modułowi `turtle`.
- **Zdarzenia losowe:** Uważaj na burze magnetyczne i korzystaj z dobrej pogody.
- **Interakcje:** Zbieraj paliwo (⛽), unikaj trudnego terenu (💥) i korzystaj ze skrótów (🌀).
- **Zarządzanie paliwem:** Każdy ruch i obrót zużywa cenne paliwo.

## Wymagania

Do uruchomienia gry potrzebujesz:
- Python 3.12 lub nowszy.
- Biblioteka `tkinter` (zazwyczaj dołączona do standardowej instalacji Pythona, niezbędna dla modułu `turtle`).

## Uruchamianie Gry

Aby rozpocząć symulację, wykonaj poniższe kroki:

1. Upewnij się, że wszystkie pliki projektu znajdują się w jednym folderze.
2. Otwórz terminal lub wiersz poleceń w tym folderze.
3. Uruchom główny skrypt gry:
   ```bash
   python main.py
   ```

## Sterowanie

Po uruchomieniu gry będziesz mógł wydawać polecenia w konsoli:
- `M` - **Ruch naprzód:** Podaj dystans, o jaki ma się przesunąć łazik.
- `O` - **Obrót:** Podaj kąt (w stopniach), o jaki ma się obrócić łazik (dodatni w lewo, ujemny w prawo).
- `Q` - **Koniec:** Przerwanie symulacji.

## Struktura Projektu

- `main.py` - Główny skrypt uruchamiający grę i pętlę symulacji.
- `rover.py` - Logika łazika (ruch, paliwo).
- `world.py` - Definicja świata, współrzędnych i elementów mapy.
- `events.py` - Zarządzanie zdarzeniami losowymi i interakcjami.
- `constants.py` - Parametry konfiguracyjne gry.
- `turtle_view.py` - Obsługa graficznej wizualizacji.

---
Powodzenia w misji! 🚀
