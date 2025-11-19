# Числа с произвольной системой счисления 
## Общая информация
Сейчас репозиторий не представляет актуальной версии кода, однако в перспективе создания библиотеки, позволяющей работать с числами в различных позиционных системах счисления, не переводя их в другие системы счисления, для наглядности принципа работы таких чисел. Планируется так же и реализации визуализации работы всех функций внутри реализованных классов.
В перспективе предполагается создание следующих классов:
1. Целые числа с позиционными натуральными системами счисления
2. Целые числа с позиционными целыми системами счисления
3. Целые числа с позиционными рациональными системами счисления
4. Целые числа с позиционными иррациональными системами счисления (с ограниченной точностью)
Так же планируется создание 4х классов для чисел типа float, 4х классов для чисел типа Fractions.
## Структура
### main
В ветке main будут выкладываться актуальные версии после релиза, которые готовы к использованию. Сейчас ветка пустая, так как нет ни одной достоверно работающей версии проекта.
### master
В ветке master сейчас разработка наиболее проверенной и протестированной версии, ближайшей к версии предполагаемой версии с минимальным функционалом. Последующее использование ветки master предполагает, что именно здесь будет находиться версия, находящаяся в разработке. 
### reliably_true
В ветке reliably_true сейчас разработка проверенной версии, однако реализация исключительно класса натуральных чисел. После реализации этого класса, будет первая релизная версия и ветка потеряет свою актуальность.
### pre-alfa
В ветке pre-alfa сейчас находится основа версии, которая далее будет использоваться для разработки, однако сейчас структура файлов и программ не представляет возможным их исправление или тестирование. Ветку ждёт рефакторинг, а далее слияние с функционалом ветки main.
## Минимальная версия релиза
Предполагает в себя включение следующее:

1 Класс целых чисел с позиционным натуральными системами счисления

1.1 Алфавит ограничен: "0123456789abcdefghijklmnopqrstuvwxyz", соответственно ограничен максимальное значение разряда (10 для 10-тиричной и 2 для двоичной)

1.2 Разделитель между двумя символами одного числа отсутствует

1.3 Визуализация отсутствует, просмостр за изменениями в числе возможен только во время дебага

1.4 Реализованы арифметические операции и операции сравнения (только между объектами этого класса)

## Вопросы сотрудничества
Сотрудничество допускается и приветствуется, в случае желания прошу писать в тг: @dmitriyisaychev или на почту: physmatitdmisaychev@gmail.com для выдачи вам прав и дальнейшей коммуникации.
Переводом занимался яндекс переводчик, прошу глубочайшее прощение за ошибки, при потребности пояснения прошу писать на те же контактные данные. 



# Numbers with an arbitrary number system 
## General information
Currently, the repository does not provide an up-to-date version of the code, however, in the future, a library will be created that allows you to work with numbers in various positional number systems without converting them to other number systems, to illustrate the principle of operation of such numbers. It is also planned to implement visualization of the work of all functions inside the implemented classes.
The following classes are expected to be created in the future:
1. Integers with positional natural number systems
2. Integers with positional integers
3. Integers with positional rational number systems
4. Integers with positional irrational number systems (with limited precision)
It is also planned to create 4 classes for float type numbers, 4 classes for Fractions type numbers.
## Structure
### main
The main branch will contain the latest versions after the release, which are ready for use. The branch is currently empty, as there is not a single reliably working version of the project.
### master
The master branch is currently developing the most proven and tested version, the closest to the version of the intended version with minimal functionality. Subsequent use of the master branch assumes that this is where the version under development will be located.
### pre-alfa
The pre-alfa branch currently contains the basis of the version that will be used for development, but now the structure of files and programs does not make it possible to fix or test them. The branch is waiting for refactoring, and then merging with the functionality of the main branch.
### reliably_true
A proven version is currently being developed in the reliably_true branch, but the implementation is exclusively for the natural numbers class. After the implementation of this class, the first release version will be released and the branch will lose its relevance.
## Minimum release version
It involves the inclusion of the following:

1 The class of integers with positional natural number systems
  
1.1 The alphabet is limited: "0123456789abcdefghijklmnopqrstuvwxyz", respectively, the maximum digit value is limited (10 for decimal and 2 for binary)

1.2 There is no separator between two characters of the same number

1.3 There is no visualization, viewing changes in the number is possible only during the debug

1.4 Arithmetic and comparison operations are implemented (only between objects of this class)
## Cooperation issues
Cooperation is allowed and welcome, if you wish, please write to tg: @dmitriyisaychev or by email: physmatitdmisaychev@gmail.com for granting you rights and further communication.
Yandex Translator handled the translation, I apologize profoundly for any mistakes, and if necessary, please provide explanations using the same contact information.
