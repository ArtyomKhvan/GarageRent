Сайт по аренде автомобилей

Алгоритм действий:
1 Модели:
	
    1 Отзывы
	2 Авто
	3 Фото автомобилей
	4 Платформа
	5 Профиль 
	6 Заявка от клиента

2 Группы:
	
    1 Админ
	2 Посетитель 

3 Страницы:

1 Страница “Главная”:
	
    1 header который идёт за скролом страницы: (base.html)
		1 всплывающее меню:
			1 О компании
			2 Наши услуги перенос на пункт ниже 3
			3 Автопарк
			4 Контакты
		2 Эмблема ссылка на главную страницу
		3 Контактный номер, Email, Кнопка - Задать вопрос, поменять язык Казахский
	2 Карусель с видео перевозки на газели
	3 Наши услуги:
		1 Аренда без водителя
		2 Аренда с водителем
		3 Межгородские услуг
		4 Услуги эвакуатора
	4 Заказать бесплатную консультацию ---------
	5 Преимущества: (partial)
		“Всплывающие окна”:
		1 Собственный автопарк
		2 Квалифицированный персонал
		3 Система мониторинга транспорта
		4 Полная документальная и юридическая безопасность
		5 Полностью оснащенная материально-техническая база СТО
	6 Футер: (base.html)
		1 c в кружке название организации
		2 значки: телеграм, инста, вк, ватсап

2 Страница “О компании”:
	
    1 Хедер (base.html)
	2 Фото наших газелей, поверх название компании(partial)
	3 описание компании
	4 преимущества (partial)
	5 Футер (base.html)

3 Страница “Наши услуги”
	
    1 Хедер (base.html)
	2 Фото наших газелей, поверх название компании(partial)
	3 Форма для расчёта цены ”Расчитать стоимость аренды”:
		1 Срок аренды календарь, с - по 
		2 select всплывающий чтоб выбрать 1 модель
		3 select город - межгород, задаток 30 000 - 50 000
		4 select с водителем или без
		5 кнопка “Расчёт”
	4 Контакты (parthial)
	5 Футер (base.html)

4 Страница “Автопарк”

    1 Хедер (base.html)
	2 Фото наших газелей, поверх название компании(partial)
	3 список авто “фото с годом и видом топлива”
	4 футер

5 Страница CRUD “Просмотр Авто”
	
    1 Хедер (base.html)
	2 Фото Авто во всю ширину
	3 Стоимость “от” (без водителя, с водителем), мелким шрифтом ”окончательная стоимость формируется по договоренности”
	4 Фото авто подробно
	5 Характеристики
	6 Оставить отзыв
	7 Список отзывов *сортировать по дате ”Пагинации, поиск”
		1 Имя
		2 Фамилия
		3 дата
		4 отзыв
		5 удалить “если автор”
	8 Футер (base.html)

View Страница “Отзывы клиентов”
	
    1 Хедер (base.html)
	2 Фото наших газелей, поверх “Отзывы”(partial)
	
	4 Футер (base.html)

6 Страница “Контакты”
	
    1 Хедер (base.html)
	2 Фото наших газелей, поверх название компании(partial)
	3 Реквизиты компании
	4 Телефоны, Емайл
	5 Часы работы
	6 Карта с местоположением
	7 Футер (base.html)


**

Порядок действий при запуске проекта:

    1 virtualenv venv
    2 . venv/bin/activate
    3 pip install -r requirements.txt
    4 python manage.py migrate
    5 python manage.py loaddata fixtures/auth_dump.json
    6 python manage.py runserver
**

