@echo on
chdir /d D:\CourseDirectory\BuildTool
py CreateCourseDirectory.py
set /p confirmClose=Press any key to close...
exit