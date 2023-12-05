import time
import random


def test_szybkiego_pisania():
    zdania = [
        "Podczas zachodu słońca, kiedy niebo przybiera odcienie różu, a chmurki malują się odcieniami fioletu, czuje się spokój, który otula duszę jak ciepła kołdra z miękkiego puchu.",
"Z wiosennym porankiem przychodzi również obietnica nowego dnia, gdzie kwiaty otwierają swe płatki, a słońce delikatnie wymyka się zza horyzontu, rozświetlając świat promieniami złotej energii.",
"Gdy krople deszczu tańczą na powierzchni jeziora, rozbłyskując w blasku promieni słonecznych, natura ukazuje swą magiczną moc, tworząc malowniczy pejzaż, który oczarowuje każdego obserwatora.",
"Słychać szmer liści, gdy lekki wiatr przemyka przez gałęzie drzew, a ptaki śpiewają swoje pieśni, tworząc harmonię dźwięków, która przenika serce każdego, kto otwiera się na piękno natury.",
"W miękkim blasku księżyca, gdy gwiazdy migoczą na niebie jak diamenty, noc staje się magicznym czasem, kiedy marzenia zakradają się do naszych serc, snując niezwykłe opowieści.",
"Ścieżka życia pełna jest zakrętów, gdzie czasem musimy pokonywać górskie szczyty trudu, by odkryć doliny spokoju, gdzie serce odpoczywa w zaciszu spokoju.",
"W tętniącym życiem mieście, gdzie ulice pulsuje energią, a ludzie suną ulicami jak strumienie, czas zdaje się znikać w wirze wydarzeń, tworząc nieustannie zmieniający się krajobraz.",
"Podczas burzy, gdy pioruny rozświetlają niebo, a deszcz uderza w okna jak stukot niewidzialnych palców, czuje się potężną siłę natury, która przywołuje pokorę wobec niezgłębionych tajemnic świata.",
"Kiedy zamykam oczy i oddaje się rytmowi muzyki, czuje, jak dźwięki przenikają głęboko do duszy, wywołując emocje, które unoszą się jak delikatne fale na oceanie uczuć.",
"W społeczeństwie pełnym kontrastów, gdzie tradycja splata się z nowoczesnością, a przeszłość tańczy z teraźniejszością, każdy krok staje się podróżą w głąb historii, której strony wypełnione są różnorodnością doświadczeń.",
    ]

    zdanie = random.choice(zdania)
    print("Przepisz poniższe zdanie jak najszybciej:")
    print(zdanie)
    input("Naciśnij Enter, aby rozpocząć test...")
    start_time = time.time()

    wprowadzone_zdanie = input("Przepisz zdanie: ")

    end_time = time.time()
    czas_wykonania = end_time - start_time

    if wprowadzone_zdanie == zdanie:
        print("Poprawnie!")
        print(f"Czas wykonania: {czas_wykonania:.2f} sekundy, niezły wynik! ;)")
    else:
        print("Błędne przepisanie. Spróbuj ponownie.")

# Uruchomienie testu szybkiego pisania
test_szybkiego_pisania()