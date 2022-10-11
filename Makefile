brain-games: # Запуск brain_game
	poetry run brain-games

brain-even: # Запуск even_game
	poetry run brain-even

brain-calc: # Запуск cacl_game
	poetry run brain-calc

brain-gcd: # Запуск gcd_game
	poetry run brain-gcd

brain-progression: # Запуск proggression_game
	poetry run brain-progression
	
install: # Установка poetry
	poetry install

build: # Собрать poetry проект 
	poetry build

publish: # Опубликовать poetry проект
	poetry publish --dry-run

package-install: # Установка пакета
	python -m pip install --user dist/*.whl

lint: #Проверка кода линтером
	poetry run flake8 brain_games