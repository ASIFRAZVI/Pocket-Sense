
echo Please Wait Process Started
echo off

call color 05

echo :::-:-::: Starting Employee management system Backend :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo 

@REM Activate the virtual environment
echo activating the virtual environments
call venv\Scripts\activate.bat
echo :::-:-::: activated :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======

@REM rem Install requirements
@REM echo Installing the all requirements
@REM echo :::-:-::: Installing.... :::-:-:::
@REM echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
@REM pip install -r requirements.txt
@REM echo :::-:-::: Installed :::-:-:::
@REM echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======


@REM  Run Django migrations
@REM python manage.py makemigrations
@REM echo :::-:-::: migrating the DB.... :::-:-:::
@REM python manage.py migrate
@REM echo :::-:-::: Ohoo! DB migrated!.... :::-:-:::

@REM  Start the Django development server
echo :::-:-::: starting The Server.... :::-:-:::
echo :::-:-::: Server started .... :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo :::-:-::: Happy Coding! .... :::-:-:::
python manage.py runserver 8002
pause
