# onlineStore

Информационная система интернет-магазина сладостей и десертов, использующего веб-интерфейс.

Техническое задание и структуру базы данных можно посмотреть в гугл документе: https://docs.google.com/document/d/1CgTWYPhBhRjBsovumg0innl_QWNw5akjn84FwWaWiOw/edit?usp=sharing

1 Краткое техническое задание на построение информационной системы, использующей веб-интерфейс

1.1  Цель проекта
В качестве информационной системы (ИС) необходимо разработать веб-приложение интернет-магазина сладостей и десертов. Целью данного проекта является решение задач бизнеса с помощью веб-интерфейса.

1.2 Целевая аудитория и группы пользователей 
Основной целевой аудиторией проекта являются дети и люди пожилого возраста.
Всех пользователей ИС можно разделить на следующие группы исходя из различных прав доступа к ИС: гость, покупатель, продавец, владелец магазина, системный администратор.

1.3 Основные функции разрабатываемой системы
Информационная система предоставляет следующий функционал для гостей магазина:
- просмотр каталога магазина;
- просмотр информации о товаре;
- добавление товара в корзину;
- оформление заказа.
Зарегистрированные покупатели дополнительно могут просматривать историю заказов. Регистрация в системе также избавляет покупателя от заполнения своих данных при оформлении каждого заказа: данные заполняются один раз во время регистрации.

1.4 Распределение прав доступа к информационной системе
Гость — это незарегистрированный пользователь, основной целью которого является ознакомление с продукцией и её заказ. У гостя есть права на просмотр каталога товаров и информации о товарах, добавления товара в корзину и оформление заказа.
Покупатель — авторизованный пользователь, предварительно прошедший процедуру регистрации. У покупателя есть все права Гостя. Дополнительно покупатель может просматривать свою историю заказов. Покупателю не нужно заполнять свои данные при оформлении заказа: данные заполняются автоматически из базы данных, в которую они были предварительно внесены при регистрации покупателя.
Продавец — авторизованный пользователь, который размещает товары в магазине и фиксирует факт оплаты заказа покупателем. Продавец имеет право добавлять товары в каталог, удалять их, изменять информацию о товарах, изменять статус заказа с «оформлен» на «оплачен».
Владелец магазина — авторизованный пользователь, юридический владелец магазина. У него есть права на просмотр отчета о прибыли магазина и рейтинга товаров в рамках заданного временного диапазона.
Системный администратор — человек, занимающийся поддержкой технического и программного обеспечения информационной системы. У него есть физический доступ к серверу, а также полный доступ к базе данных и исходному коду программ информационной системы.

1.6 Требования к структуре информационной системы
Структура информационной системы должна представлять собой совокупность прикладных подсистем (модулей). Каждый модуль должен отвечать за исполнение определенной функции системы и/или хранения определенных данных. 
В состав ИС должны входить следующие модули:
1) модуль регистрации и авторизации. Модуль выполняет следующие функции: 
- регистрация — сбор данных пользователя, проверка их на корректность и добавления записи пользователя в БД при условии, что пользователя с таким же логином не существует в БД;
- аутентификация — проверка подлинности пользователя путём сравнения введённого им логина и пароля с данными, сохранёнными в БД;
- авторизация — предоставление пользователю разрешения или отказа на вход в учетную запись в системе на основе результатов процедуры аутентификации, предоставление аутентифицированному пользователю соответствующих прав;
- деавторизация — осуществление выхода пользователя из учетной записи в системе и лишение его прав, предоставленных ранее.
2) модуль каталога. Данный модуль необходим для отображения товаров, полученных из БД, и информации о них конечным покупателям;
3) модуль корзины. Модуль предоставляет следующий функционал:
- добавление товара в корзину;
- удаление ранее добавленного товара из корзины;
- изменение количество товара в корзине;
- просмотр корзины;
- оформление заказа;
4) модуль учетной записи предназначен для осуществления взаимодействия пользователя с БД системы в зависимости от его принадлежности определённой группе пользователей.

1.7 Требования к дизайну
Для ИС предъявляются следующие требования к дизайну:
- главный акцент в дизайне должен быть сделан на товаре;
- каталог должен располагаться на главной странице;
- ИС должна предоставлять пользователю удобные средства просмотра товара и его добавления в корзину;
- количество шагов для совершения целевого действия (покупки товара) должно быть минимальным;
- размер шрифта основного текста должен быть не менее 16 пикселей;
- навигация приложения должна располагаться в верхней части экрана в виде вкладок;
- в форме регистрации и покупки товара количество полей для заполнения должно быть минимальным;
- пользовательский интерфейс должен быть интуитивно понятным.

1.8 Требования к технической документации на проект
Необходимо разработать инструкцию по работе с системой для системного администратора.
Инструкция для системного администратора включает в себя:
- описание файловой структуры ИС (дерево каталогов и назначение всех каталогов и файлов);
- описание структуры БД в соответствии с шаблоном, изображенным на рисунке 1;
- описание программных модулей и функций;
- листинг программ с комментариями.

При разработке ИС использовать только открытое свободное программное обеспечение:
- на стороне сервера язык программирования Python, фреймворк Django;
- на стороне клиента язык программирования JavaScript.
В качестве системы управления базой данных (СУБД) использовать SQLite.

ER-диаграмма связи таблиц БД:

![(веб2) er-диаграмма drawio](https://github.com/ICallMyGitHairyHarry/onlineStore/assets/51024214/65d27e47-8439-48f3-997b-9f9492611011)

