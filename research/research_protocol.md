# 1. Cel badania

Celem badania jest ilościowa analiza wpływu informacji dostarczanych
przez sztuczną inteligencję na proces podejmowania decyzji przez
człowieka, ze szczególnym uwzględnieniem zjawiska nadmiernego polegania
na odpowiedziach AI (AI overreliance).

Badanie ma na celu określenie, w jakim stopniu cechy sytuacji
decyzyjnej oraz cechy respondenta są związane z prawdopodobieństwem
przyjęcia rekomendacji AI, w szczególności w sytuacji, gdy rekomendacja
AI jest błędna.

Dodatkowym celem jest określenie, czy wykorzystanie informacji
dostarczanych przez AI prowadzi do poprawy czy pogorszenia jakości
podejmowanych decyzji.

Szczególna uwaga zostanie poświęcona wpływowi takich czynników jak:

- poziom wiedzy lub znajomości zagadnienia,
- presja czasu,
- deklarowany przez sztuczną inteligencję poziom pewności odpowiedzi,
- poziom pewności respondenta co do własnej decyzji,
- cechy demograficzne respondenta, w szczególności wiek i poziom
  wykształcenia.

Dodatkowym celem badania jest identyfikacja cech respondentów oraz
warunków sytuacji decyzyjnej związanych z większym prawdopodobieństwem
wystąpienia AI overreliance oraz konstrukcja modelu umożliwiającego
predykcję tego prawdopodobieństwa.

# 2. Problemy badawcze

## 2.1. Czy poziom wiedzy respondenta w zakresie badanego zagadnienia
wpływa na prawdopodobieństwo zastosowania się do błędnej rekomendacji AI?

## 2.2. Czy presja czasu wpływa na prawdopodobieństwo zastosowania się
do błędnej rekomendacji AI?

## 2.3. Czy deklarowany przez AI poziom pewności odpowiedzi wpływa na
prawdopodobieństwo zastosowania się respondenta do błędnej rekomendacji?

## 2.4. Czy poziom pewności respondenta co do własnej decyzji jest
związany z prawdopodobieństwem przyjęcia błędnej rekomendacji AI?

## 2.5. Czy wiek respondenta jest związany z prawdopodobieństwem
zastosowania się do błędnej rekomendacji AI?

## 2.6. Czy poziom wykształcenia jest związany z prawdopodobieństwem
zastosowania się do błędnej rekomendacji AI?

## 2.7. Czy przedstawienie respondentowi rekomendacji AI po podjęciu
przez niego pierwotnej decyzji wpływa na prawdopodobieństwo zmiany
tej decyzji?

## 2.8. Czy przedstawienie respondentowi rekomendacji AI wpływa na
jakość podejmowanej przez niego decyzji?

## 2.9. Czy wpływ rekomendacji AI na decyzję zależy od tego, czy
rekomendacja AI jest poprawna czy błędna?

# 3. Hipotezy badawcze

## H1. 

Wyższy poziom rzeczywistej wiedzy respondenta w zakresie badanego
zagadnienia zmniejsza prawdopodobieństwo zastosowania się do błędnej
rekomendacji AI.

## H2.

Wyższa presja czasu zwiększa prawdopodobieństwo zastosowania się do
błędnej rekomendacji AI.

## H3.

Wyższy deklarowany przez AI poziom pewności błędnej rekomendacji
zwiększa prawdopodobieństwo jej przyjęcia przez respondenta.

## H4.

Niższy poziom pewności respondenta co do pierwotnej decyzji zwiększa
prawdopodobieństwo zmiany tej decyzji po przedstawieniu rekomendacji AI.

## H5.

Prawdopodobieństwo zastosowania się do błędnej rekomendacji AI różni
się pomiędzy grupami wiekowymi respondentów.

## H6.

Wyższy poziom wykształcenia jest związany z niższym prawdopodobieństwem
zastosowania się do błędnej rekomendacji AI.

## H7.

Przedstawienie rekomendacji AI zwiększa prawdopodobieństwo zmiany
pierwotnej decyzji respondenta.

## H8.

Przyjęcie poprawnej rekomendacji AI zwiększa, a przyjęcie błędnej
rekomendacji AI zmniejsza jakość decyzji respondenta.

# 4. Koncepcja badania

Badanie będzie miało charakter eksperymentalny i będzie polegało na
obserwacji zachowania respondentów podejmujących serię decyzji
w kontrolowanych sytuacjach decyzyjnych.

W każdym zadaniu respondent najpierw podejmie decyzję samodzielnie,
bez dostępu do rekomendacji AI. Następnie otrzyma rekomendację
wygenerowaną przez sztuczną inteligencję wraz z deklarowanym przez AI
poziomem pewności odpowiedzi. Po zapoznaniu się z rekomendacją
respondent będzie miał możliwość podtrzymania lub zmiany swojej
pierwotnej decyzji.

Wynik każdej decyzji będzie możliwy do obiektywnego określenia na
podstawie wcześniej zdefiniowanych zasad danego zadania.

Szczegółowa konstrukcja scenariuszy, sposób określania wyniku oraz
parametry eksperymentalne zostaną opisane w osobnym dokumencie
`experiment_design.md`.

# 5. Jednostka obserwacji

Badanie będzie przeprowadzane na próbie M respondentów. Każdy
respondent wykona N zadań decyzyjnych.

Podstawową jednostką obserwacji w części analitycznej będzie decyzja
respondenta podjęta w ramach konkretnego zadania.

W przypadku pełnego wykonania badania przez wszystkich respondentów
liczba obserwacji wyniesie:

M × N

Powtarzane obserwacje pochodzące od tego samego respondenta zostaną
uwzględnione na etapie konstrukcji modelu ekonometrycznego.

# 6. Zjawisko AI overreliance

Na potrzeby badania AI overreliance będzie rozumiane jako nadmierne
poleganie na rekomendacji sztucznej inteligencji w sytuacji, w której
rekomendacja ta jest błędna.

Szczególnie istotnym przypadkiem będzie sytuacja, w której:

1. respondent przed przedstawieniem rekomendacji AI podejmuje
   prawidłową decyzję,
2. AI przedstawia błędną rekomendację,
3. respondent zmienia swoją decyzję zgodnie z rekomendacją AI,
4. zmiana prowadzi do pogorszenia jakości decyzji.

Ostateczna operacjonalizacja zmiennej AI overreliance zostanie ustalona
po doprecyzowaniu konstrukcji eksperymentu.

# 7. Jakość decyzji

Jednym z elementów badania będzie obiektywna ocena jakości decyzji.

W zależności od charakteru scenariusza jakość decyzji będzie określana
na podstawie wcześniej zdefiniowanej funkcji celu lub innych
jednoznacznych kryteriów oceny.

Ze względu na możliwość występowania scenariuszy o różnej konstrukcji
i różnej skali wyników, w analizie rozważane jest wykorzystanie
względnej miary jakości decyzji, wspólnej dla wszystkich scenariuszy.

W szczególności rozważana jest normalizacja wyniku decyzji do skali
0–100.

Pozwoli to analizować zarówno:

- jakość decyzji początkowej,
- jakość decyzji końcowej,
- zmianę jakości decyzji po przedstawieniu rekomendacji AI,
- różnicę pomiędzy decyzją respondenta a decyzją optymalną.

Szczegółowy sposób konstrukcji wyniku zostanie określony w
`experiment_design.md`.

# 8. Pomiar pewności

Respondent będzie proszony o określenie poziomu pewności co do swojej
decyzji, np. w skali od 0% do 100%.

Pomiar może zostać przeprowadzony zarówno po podjęciu decyzji
pierwotnej, jak i po podjęciu decyzji końcowej.

Pozwoli to analizować zależność pomiędzy pewnością respondenta
a jego podatnością na wpływ rekomendacji AI.

Rozważane jest również wykorzystanie zmiennej opisującej zmianę
pewności respondenta:

zmiana pewności = pewność końcowa − pewność początkowa

# 9. Manipulacja eksperymentalna

W badaniu rozważane jest kontrolowane różnicowanie wybranych cech
sytuacji decyzyjnej.

W szczególności mogą one obejmować:

- poprawność rekomendacji AI,
- deklarowany poziom pewności AI,
- poziom presji czasu,
- charakter oraz trudność zadania.

Szczegółowy sposób manipulacji tymi czynnikami zostanie określony
w `experiment_design.md`.

# 10. Dane gromadzone podczas eksperymentu

Na obecnym etapie zakłada się rejestrowanie co najmniej:

### Informacje o respondencie

- identyfikator respondenta,
- wiek lub grupa wiekowa,
- poziom wykształcenia,
- ewentualne dodatkowe cechy demograficzne.

### Informacje o zadaniu

- identyfikator zadania,
- typ scenariusza,
- parametry eksperymentalne,
- prawidłowe lub optymalne rozwiązanie.

### Decyzja pierwotna

- decyzja respondenta,
- czas podjęcia decyzji,
- poziom pewności respondenta,
- wynik decyzji.

### Rekomendacja AI

- rekomendacja AI,
- poprawność rekomendacji,
- deklarowany poziom pewności AI.

### Decyzja końcowa

- decyzja końcowa,
- czas podjęcia decyzji,
- poziom pewności respondenta,
- informacja o zmianie decyzji,
- wynik decyzji końcowej.

# 11. Planowana analiza ilościowa

Po zakończeniu zbierania danych planowana jest analiza zależności
pomiędzy cechami respondentów, parametrami sytuacji decyzyjnej,
informacjami przedstawionymi przez AI oraz zachowaniem respondentów.

Głównym przedmiotem analizy będzie prawdopodobieństwo wystąpienia
AI overreliance.

Dodatkowo analizowany może być wpływ rekomendacji AI na zmianę decyzji
oraz na jakość decyzji mierzoną wynikiem uzyskanym przez respondenta.

W zależności od ostatecznej konstrukcji zmiennych oraz eksperymentu
rozważane jest wykorzystanie modeli dla zmiennej binarnej, w
szczególności modeli logitowych lub probitowych.

W przypadku wykorzystania wielu zadań dla każdego respondenta
konieczne będzie uwzględnienie zależności pomiędzy obserwacjami
pochodzącymi od tego samego respondenta.

Szczegółowa specyfikacja modeli, dobór zmiennych kontrolnych oraz
sposób uwzględnienia powtarzanych obserwacji zostaną określone po
ustaleniu ostatecznej konstrukcji eksperymentu.

# 12. Otwarte kwestie badawcze

Na obecnym etapie wymagają doprecyzowania w szczególności:

- ostateczny charakter scenariuszy eksperymentalnych,
- liczba zadań przypadających na jednego respondenta,
- liczba respondentów,
- sposób doboru respondentów,
- sposób konstrukcji zadań,
- sposób zapewnienia obiektywnej oceny jakości decyzji,
- sposób pomiaru rzeczywistej wiedzy respondenta,
- sposób pomiaru pewności respondenta,
- zakres i sposób manipulowania poziomem pewności AI,
- sposób wprowadzania błędnych rekomendacji AI,
- sposób manipulowania presją czasu,
- sposób konstrukcji i normalizacji wyniku decyzji,
- kolejność prezentacji zadań,
- potencjalny efekt uczenia się respondenta pomiędzy zadaniami,
- ostateczna definicja zmiennej AI overreliance,
- ostateczne zmienne zależne w modelach ekonometrycznych,
- sposób uwzględnienia powtarzanych obserwacji dla tego samego respondenta,
- zakres danych demograficznych zbieranych od respondentów.