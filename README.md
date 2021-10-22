## Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

* `p` – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
* `s` – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;  
*Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ*.
* `l`– list – команда, которая выведет список всех документов в формате `passport "2207 876234" "Василий Гупкин"`;
* `a` – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. *Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку*.

**Внимание**: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

## Задача №2. Дополнительная (не обязательная)
* `d` – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. *Предусмотрите сценарий, когда пользователь вводит несуществующий документ*;
* `m` – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. *Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку*;
* `as` – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. *Предусмотрите случай, когда пользователь добавляет полку, которая уже существует*.;