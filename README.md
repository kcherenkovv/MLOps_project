![screen1](https://github.com/kcherenkovv/MLOps_project/blob/main/scrins/example_of_work.png)


**Команда:**

Кирилл Реченков 

Николай Шешин

Серафим Загородний

Екатерина Таратута

Михиал Симаков




**Версионирования датасета на удалённом репозитории в googleDrive:**
![screen1](https://github.com/kcherenkovv/MLOps_project/blob/main/scrins/dvc_example.png)





**Датасет** 

https://drive.google.com/drive/folders/1AFZ7-dMZLfXwDyBfSURczp8jpYz2qf-p





**Проект выполнен согласно поставленному заданию и включает следующие основные компоненты и функциональности:**


**Оркестрация с помощью CI/CD (Jenkins)**

  Для оркестрации процессов разработки и развертывания использован инструмент CI/CD - Jenkins.
  
  Jenkins автоматизирует сборку, тестирование и развертывание нашего приложения, обеспечивая непрерывность и надежность процессов.
  
**Версионирование данных с использованием DVC**

  Для управления версиями данных в проекте используется инструмент версионирования данных DVC.
  
  Датасеты версионируются, синхронизируются с удаленным хранилищем и обеспечивают возможность восстановления данных в прошлых версиях.
  
**Разработка функциональных возможностей в отдельных ветках**

  Разработка новых функций и обновлений приложения проводится в отдельных ветках репозитория.
  
  Наборы фичей и версии данных также управляются в рамках соответствующих веток, обеспечивая структурированный и удобный процесс разработки.
  
**Запуск модульных тестов и проверка данных на качество**

  В рамках нашего CI/CD конвейера запускаются как модульные тесты приложения, так и проверка качества данных.
  
  Это позволяет обеспечить высокое качество кода и данных, а также быструю обратную связь разработчикам.
  
**Реализация итогового приложения в виде Docker образа**

  Итоговое приложение реализовано в виде Docker образа, что обеспечивает удобство и портабельность при развертывании.
  
  Сборка Docker образа происходит в рамках нашего CI/CD конвейера, автоматизируя процесс развертывания.

  Создание контейнера Docker, в котором будет запускаться приложение на Python с использованием библиотеки Streamlit, происходит так:

FROM python:3.9-slim: Указывает базовый образ, который будет использоваться для создания контейнера. В данном случае используется образ с Python версии 3.9 в урезанной версии slim, что позволяет уменьшить размер итогового образа.
Команда COPY: Копирует необходимые файлы из локальной директории внутрь контейнера. В данном случае копируются файлы image_processing.py, main.py и requirements.txt в директорию /app контейнера.
WORKDIR /app: Устанавливает рабочую директорию внутри контейнера для последующих команд.
RUN pip install -r requirements.txt: Устанавливает необходимые зависимости, указанные в файле requirements.txt, используя менеджер пакетов pip.
CMD ["streamlit", "run", "main.py"]: Эта команда задает, что при запуске контейнера будет выполнена команда streamlit run main.py, что запускает приложение Streamlit, основное управление которого будет обеспечиваться файлом main.py.
Таким образом, данный Dockerfile определяет окружение контейнера с необходимыми зависимостями, копирует файлы приложения, устанавливает команду для запуска приложения на Streamlit через файл main.py.
