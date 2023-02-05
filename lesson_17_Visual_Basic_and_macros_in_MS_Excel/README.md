# Visual Basic и макросы в MS Excel.
## Функции VBA

    Function <имяФункции>
        (<аргумент1> <аргумент2>, ...)
        <операторVB1>
        <операторVB2>

        <Имя функции>=
        <возвращаемоеЗначение>

Программа может состоять(и обычно состоит) из многих процедур и фу-йи, ко-ые могут распологаться в одном или нескольких *модулях*.Модули группируются в *проекты*, при этом в одном проекте могут мирно сосуществовать несколько различных программ, исп-их общие модули или процедуры.

Каждая из процедур, находящихся в одном модуле, должна иметь уникальное имя, однако в проекте может содержаться несколько различных модулей.
    
+ Если в проекте содержиться несколько различных процедур с одним и темже именем, необходимо для уточнения имени исп-ть при вызове процедуры следующий синтаксис:

<имяМодуля>.<имяПроцедуры>

+ Если при этом имя модуля состоит из нескольких слов

[Графический модуль].Процедура

+ Допускаетсмя и такое

<имяПроекта>.<имяМодуля>.<имяПроцедуры>

## Переменные, константы и типы данных

Объявление переменных

    Dim<имяПеременной>[As<типДанных>]

Пример:
    
    Dim x As integer, y As Integer
    Dim z As Double

### Типы данных

+ Array     
+ Boolean
+ Currency
+ Date
+ Double
+ Intefer
+ Long
+ Object
+ Single
+ String
+ Variant