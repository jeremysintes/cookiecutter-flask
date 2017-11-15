@echo off
if "%1" == "" GOTO start
if "%1" == "make" GOTO make_all
if "%1" == "delete" GOTO delete_all
if "%1" == "make_trello" GOTO make_trello
if "%1" == "delete_trello" GOTO delete_trello

:start
    start cmd /c lets_work make
    GOTO end
:make_all
    python builder.py
    GOTO end
:delete_all
    python destroyer.py
    GOTO end
:make_trello
    python builder.py
    GOTO end
:destroy_trello
	python destroyer.py
	GOTO end
:end