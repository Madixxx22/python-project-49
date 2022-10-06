install: # Установка poetry
	poetry install

brain-games: # Запуск brain_games
	poetry run brain-games

build: # Собрать poetry проект 
	poetry build

publish: # Опубликовать poetry проект
	poetry publish --dry-run

package-istall: # Установка пакета
	python -m pip install --user dist/*.whl