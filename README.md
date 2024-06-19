# MLOps_project
## Как это выглядит:
![screen1](https://github.com/kcherenkovv/MLOps_project/blob/main/scrins/example_of_work.png)
## Версионирования датасета на удалённом репозитории в googleDrive:
![screen1](https://github.com/kcherenkovv/MLOps_project/blob/main/scrins/dvc_example.png)

Проект выполнен согласно заданию: 

1. Проект оркестируется с помощью ci/cd (jenkins).
2. Датасеты версионируются с помощью dvc и синхронизируются с удалённым хранилищем.
3. Разработка возможностей приложения проводится в отдельных ветках, наборы фичей и версии данных тоже.
4. В конвеере запускаются не только модульные тесты, но и проверка тестами на качество данных.
5. Итоговое приложение реализуется в виде образа docker. Сборка образа происходит в конвеере.
